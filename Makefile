BUILDDIR := ./_build
PYTHON ?= python

.PHONY: all clean prep fetch-data create-html serve-local

all:
	$(PYTHON) ./build_site.py all --build-dir $(BUILDDIR)

clean:
	$(PYTHON) ./build_site.py clean --build-dir $(BUILDDIR)

prep:
	$(PYTHON) ./build_site.py prep --build-dir $(BUILDDIR)

fetch-data:
	$(PYTHON) ./build_site.py fetch-data --build-dir $(BUILDDIR)

create-html:
	$(PYTHON) ./build_site.py create-html --build-dir $(BUILDDIR)

serve-local:
	$(PYTHON) ./build_site.py serve-local --build-dir $(BUILDDIR)
