# Napari Hub Lite - [napari.org/hub-lite](napari-hub.org)

[![Fetch Data, Build HTML & Deploy](https://github.com/napari/hub-lite/actions/workflows/build_and_deploy.yml/badge.svg)](https://github.com/napari/hub-lite/actions/workflows/build_and_deploy.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/napari/hub-lite/main.svg)](https://results.pre-commit.ci/latest/github/napari/hub-lite/main)

This implementation of the napari hub is developed and managed by the napari team. It is based on an original implementation by Yunha Lee.

The website is deployed daily using GitHub pages and contains plugin information served by [npe2api](https://github.com/napari/npe2api). This GitHub repository contains the Python scripts, javascript, HTML
templates and CSS templates required to build the web pages.

![](./static/images/napari_hub_lite_snapshot.png)

The `fetch_napari_data.py` script queries [npe2api](https://github.com/napari/npe2api) for plugin information including PyPI/conda info and individual plugin manifests.

The `create_static_html_files.py` script uses this data to generate HTML files for each individual plugin page as well as for the plugin listing on the website's homepage.

The `plugin_loading_and_search.js` script contains functions for loading the main plugin list and searching.

The `build_and_deploy.yml` workflow builds the website using the above scripts and deploys it to GitHub pages.

## How the site works

The site is a static build with a small Python-based generator.

1. `build_site.py` orchestrates the local build, copies shared assets into `_build/`, and runs the data and HTML generation steps.
2. `fetch_napari_data.py` fetches plugin data from `npe2api` and PyPI, then writes build data into `_build/data/`.
3. `create_static_html_files.py` reads `_build/data/plugin_page_data.json` and generates:
	- `_build/plugins/*.html` for individual plugin pages
	- `_build/plugins_list.html` for the homepage plugin list
4. `index.html` is the homepage shell and `static/js/plugin_loading_and_search.js` loads the generated plugin list and client-side search behavior.
5. `.github/workflows/build_and_deploy.yml` runs `make all` and publishes `_build/` to GitHub Pages.

The key implementation surfaces are:

- `fetch_napari_data.py`: external data fetching and normalization
- `create_static_html_files.py`: HTML generation and markdown rendering
- `templates/each_plugin_template.html`: plugin detail page template
- `index.html`: homepage structure
- `static/js/plugin_loading_and_search.js`: homepage interactivity
- `static/css/`: copied styling assets used by the generated pages

`build_site.py` is the implementation layer. `pixi` calls it directly from
`pyproject.toml`, and the `Makefile` stays in place as a small compatibility wrapper
for contributors and CI that still expect `make all` or `make serve-local`.

## Local Development

### Recommended: pixi

[Pixi](https://pixi.sh) is the easiest cross-platform way to build the site locally, especially on Windows.

1. [Install pixi](https://pixi.sh/latest/installation/).
2. From the repository root, install the environment:

```sh
pixi install
```

3. Build the site:

```sh
pixi run build
```

4. Serve the generated site locally:

```sh
pixi run serve-local
```

Useful pixi tasks:

- `pixi run clean`
- `pixi run prep`
- `pixi run fetch-data`
- `pixi run create-html`
- `pixi run build`
- `pixi run serve-local`

These pixi tasks intentionally mirror the existing `make` targets so the review surface
stays small, even though they now call the Python build helper directly.

The single source of truth for both Pixi and Python dependencies is now
`pyproject.toml`.

### Alternative: uv

If you prefer a Python-native workflow without Pixi, use `uv` against the same
`pyproject.toml` manifest.

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Sync the development environment:

```sh
uv sync --group dev
```

3. Build the site:

```sh
uv run python build_site.py all
```

4. Serve the generated site locally:

```sh
uv run python build_site.py serve-local
```

This repository is not packaged as an installable Python distribution, so the
intended modern non-Pixi workflow is `uv sync` plus `uv run` rather than a
legacy `requirements.txt` install.

### Building the Website

To build the website locally use:

```sh
# this deletes the `_build` directory and everything inside it
make clean

# this runs the required Python scripts and populates the `_build` directory
make all
```

The main commands are still:

```sh
make clean
make prep
make fetch-data
make create-html
make all
```

Those `make` commands are thin wrappers around:

```sh
python build_site.py clean
python build_site.py prep
python build_site.py fetch-data
python build_site.py create-html
python build_site.py all
```

If you want to inspect or update dependency definitions, edit `pyproject.toml`
rather than a separate `requirements.txt` or `pixi.toml`.

### Serving the Website Locally

To serve the website locally in your browser use:

```sh
make serve-local
```

Or directly:

```sh
pixi run serve-local
```

By default the server runs at `http://127.0.0.1:8000`.

### Acknowledgments

This project makes extensive use of the design and html resources from the original [napari hub](https://github.com/chanzuckerberg/napari-hub/). All resources are used with permission. 
