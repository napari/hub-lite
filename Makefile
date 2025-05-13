mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(dir $(mkfile_path))
BUILDDIR := $(current_dir)_build

all: prep fetch-data create-html

prep:
	@echo "Preparing build directory..."
	rm -rf $(BUILDDIR)
	mkdir -p $(BUILDDIR)
	mkdir -p $(BUILDDIR)/data
	mkdir -p $(BUILDDIR)/plugins
	mkdir -p $(BUILDDIR)/static
	cp -r $(current_dir)templates $(BUILDDIR)/templates
	cp -r $(current_dir)static/images $(BUILDDIR)/static/images
	cp -r $(current_dir)static/css $(BUILDDIR)/static/css
	cp $(current_dir)entire_text_search.js $(BUILDDIR)/entire_text_search.js
	cp $(current_dir)index.html $(BUILDDIR)/index.html

fetch-data:
	@echo "Fetching data..."
	python $(current_dir)fetch_napari_data.py $(BUILDDIR)
	@echo "Data fetched and stored in $(BUILDDIR)/data"

create-html:
	@echo "Creating HTML files..."
	python $(current_dir)create_static_html_files.py $(BUILDDIR)
	@echo "HTML files created in $(BUILDDIR)/plugins"