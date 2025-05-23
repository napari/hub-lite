
[![License MIT](https://img.shields.io/pypi/l/napari-argos-archive-reader.svg?color=green)](https://github.com/dioptic/napari-argos-archive-reader/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-argos-archive-reader.svg?color=green)](https://pypi.org/project/napari-argos-archive-reader)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-argos-archive-reader.svg?color=green)](https://python.org)
[![tests](https://github.com/dioptic/napari-argos-archive-reader/workflows/tests/badge.svg)](https://github.com/dioptic/napari-argos-archive-reader/actions)
[![codecov](https://codecov.io/gh/dioptic/napari-argos-archive-reader/branch/main/graph/badge.svg)](https://codecov.io/gh/dioptic/napari-argos-archive-reader)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-argos-archive-reader)](https://napari-hub.org/plugins/napari-argos-archive-reader)

A plugin to read Dioptic ARGOS archive files

----------------------------------

This repo contains a reader plugin for [DIOPTIC ARGOS](https://www.dioptic.de/en/argos-en/) Archive files, which
have `.zip` file extension.
Individual ARGOS layers are grouped into napari layer with stacks according to
their illumination, stage XY position and Z-stack information.

The plugin implements delayed reading using `dask.delayed` so that one can quickly
see the contents even for large archives with many layers. Note!: switching to
volume rendering or swapping axes can trigger the loading of all ARGOS layers, which
can take a long time for large archives.

[ARGOS](https://www.dioptic.de/en/argos-en/) is an automated system
for surface inspection according to ISO 10110-7.

This plugin is still experimental and does not support all features of ARGOS archives.

Currently, the plugin

* can read Argos matrix archives containing regular image layers including:
  * ✅ segmentation masks
  * ✅ Z-stack metadata
  * ✅ Illumination metadata
  * ✅ proper scaling and affine transformation of layers
* can read ❔✅ Argos line scan (polar) archives with minimal support (no metadata parsing)
This has not been tested on many archives.

Not supported are:

* ❌ annotated archives
* ❌ pyramid image structures
* ❌ Line segmentation metadata
* ❌ color metadata
* ❌ ...

## Usage

### Opening files

Simply drag and drop an ARGOS Archive `.zip` file onto the napari canvas or use `File->Open` to open it.

### Synchronizing contrast limits

By default, after reading an archive, each napari layer will have their own contrast limits, so you can
adjust these contrast limits individually.

The reader plugin registers a custom key binding after reading an ARGOS archive. Pressing the `s` key will allow
you to synchronize the contrast limits for a set of layers:

* If you select _a single_ napari layer corresponding to an image/stack from an ARGOS archive, all napari image
layers that were loaded from this archive now have their contrast limits synchronized, i.e. changing the
contrast limits of _any_ of them will adjust the contrast limits of _all_ of the layers belonging to the same
archive.
* If you select _multiple_ napari layers and press `s` all of these and only these napari layers will have
their contrast limits synchronized, regardless of whether they belong to the same ARGOS archive or not.

## Installation

If you have napari installed you can install the plugin from the napari hub through the `Plugins -> Plugin Manger` menu
entry. After waiting a short while for napari to retrieve the plugins available from the hub, simply enter "argos" in
the filter line entry field at the top to narrow down the plugin list and click install.

You can install `napari-argos-archive-reader` via [pip]:

    pip install napari-argos-archive-reader

To install latest development version :

    pip install git+https://github.com/dioptic/napari-argos-archive-reader.git

## License

Distributed under the terms of the [MIT] license,
"napari-argos-archive-reader" is free and open source software

[MIT]: http://opensource.org/licenses/MIT
[pip]: https://pypi.org/project/pip/
