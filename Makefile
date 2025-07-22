BUILDDIR := ./_build
FETCH_DATA_COMPLETE := $(BUILDDIR)/data/.complete
CREATE_HTML_COMPLETE := $(BUILDDIR)/plugins/.complete

.PHONY: all clean prep fetch-data create-html serve-local

all: prep fetch-data create-html

define check-venv
	@echo "Checking if virtual environment is activated..." && \
	if [ "$$CI" != "true" ] && [ "$$GITHUB_ACTIONS" != "true" ]; then \
		if [ -z "$$VIRTUAL_ENV" ] && [ -z "$$CONDA_DEFAULT_ENV" ]; then \
			echo "Please activate a virtual environment first (venv or conda)."; \
			exit 1; \
		else \
			echo "Virtual environment is activated."; \
		fi \
	else \
		echo "Running in GitHub Actions — skipping virtual environment check."; \
	fi
endef

clean:
	@echo "Cleaning up build directory..."
	rm -rf $(BUILDDIR)
	@echo "Build directory cleaned."

prep: $(BUILDDIR)

$(BUILDDIR):
	@echo "Preparing build directory..."
	mkdir -p $(BUILDDIR)
	mkdir -p $(BUILDDIR)/static
	cp -r ./templates $(BUILDDIR)/templates
	cp -r ./static/images $(BUILDDIR)/static/images
	cp -r ./static/css $(BUILDDIR)/static/css
	cp -r ./static/js $(BUILDDIR)/static/js
	cp ./index.html $(BUILDDIR)/index.html
	cp ./404.html $(BUILDDIR)/404.html

fetch-data: $(FETCH_DATA_COMPLETE)

$(FETCH_DATA_COMPLETE): $(BUILDDIR)
	$(call check-venv)
	@echo "Fetching data..."
	mkdir -p $(BUILDDIR)/data
	python ./fetch_napari_data.py $(BUILDDIR)
	@touch $(FETCH_DATA_COMPLETE)
	@echo "Data fetched and stored in $(BUILDDIR)/data"

create-html: $(CREATE_HTML_COMPLETE)

$(CREATE_HTML_COMPLETE): $(FETCH_DATA_COMPLETE)
	$(call check-venv)
	@echo "Creating HTML files..."
	mkdir -p $(BUILDDIR)/plugins
	python ./create_static_html_files.py $(BUILDDIR)
	@touch $(CREATE_HTML_COMPLETE)
	@echo "HTML files created in $(BUILDDIR)/plugins"

serve-local: $(CREATE_HTML_COMPLETE)
	@echo "Starting server..."
	python3 -m http.server --directory $(BUILDDIR)
