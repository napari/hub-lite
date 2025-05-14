BUILDDIR := ./_build

.PHONY: all prep fetch-data create-html

all: prep fetch-data create-html

prep:
	@echo "Preparing build directory..."
	rm -rf $(BUILDDIR)
	mkdir -p $(BUILDDIR)
	mkdir -p $(BUILDDIR)/data
	mkdir -p $(BUILDDIR)/plugins
	mkdir -p $(BUILDDIR)/static
	cp -r ./templates $(BUILDDIR)/templates
	cp -r ./static/images $(BUILDDIR)/static/images
	cp -r ./static/css $(BUILDDIR)/static/css
	cp ./entire_text_search.js $(BUILDDIR)/entire_text_search.js
	cp ./index.html $(BUILDDIR)/index.html

fetch-data:
	@echo "Fetching data..."
	python ./fetch_napari_data.py $(BUILDDIR)
	@echo "Data fetched and stored in $(BUILDDIR)/data"

create-html:
	@echo "Creating HTML files..."
	python ./create_static_html_files.py $(BUILDDIR)
	@echo "HTML files created in $(BUILDDIR)/plugins"