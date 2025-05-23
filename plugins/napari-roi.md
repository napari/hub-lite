
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-roi)](https://napari-hub.org/plugins/napari-roi)
[![PyPI](https://img.shields.io/pypi/v/napari-roi.svg?color=green)](https://pypi.org/project/napari-roi)
[![License](https://img.shields.io/pypi/l/napari-roi.svg?color=green)](https://github.com/BodenmillerGroup/napari-roi/raw/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-roi.svg?color=green)](https://python.org)
[![Issues](https://img.shields.io/github/issues/BodenmillerGroup/napari-roi)](https://github.com/BodenmillerGroup/napari-roi/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/BodenmillerGroup/napari-roi)](https://github.com/BodenmillerGroup/napari-roi/pulls)

Select regions of interest (ROIs) using napari

## Installation

You can install napari-roi via [pip](https://pypi.org/project/pip/):

    pip install napari-roi

Alternatively, you can install napari-roi via [conda](https://conda.io/):

    conda install -c conda-forge napari-roi

## Usage

The *napari-roi* plugin can be opened from within napari (`napari -> napari-roi: regions of interest`) and operates on napari *Shapes* layers.

ROIs can be added to any napari *Shapes* layer, either by drawing a standard napari shape (e.g. rectangle), or by adding a rectangular ROI of specified size using the `Add ROI` functionality in the *napari-roi* widget. Each ROI is associated with a name, a position (X/Y origin), and a size (width/height). The location of the X/Y origin of all ROIs can be chosen in the *napari-roi* widget. Note that any shape supported by napari (e.g. ellipse, rectangle, polygon, line, path) can serve as an ROI; for non-rectangular shapes, *napari-roi* computes rectangular bounding boxes aligned with the napari coordinate system to determine their positions and sizes. ROIs can be edited or deleted by modifying the corresponding shapes in napari, or by editing the corresponding row in the *napari-roi* widget.

All ROIs in the current *Shapes* layer can be saved to a comma-separated values (CSV) file using the `Save` functionality in the *napari-roi* widget. When the `Autosave` option is checked, the file is automatically updated on every ROI change. Note that the selected file is specific to the current *Shapes* layer; ROIs from different *Shapes* layers cannot be saved to the same file. ROIs can be loaded from a previously saved file and added to the current *Shapes* layer by opening the file in the *napari-roi* widget.

CSV files saved using *napari-roi* adhere to the following format:

| Columns | Description |
| --- | --- |
| `Name` | ROI name |
| `X`, `Y` | Position (X/Y origin) |
| `W`, `H` | Size (width/height) |

## Authors

Created and maintained by [Jonas Windhager](mailto:jonas@windhager.io) until February 2023.

Maintained by [Milad Adibi](mailto:milad.adibi@uzh.ch) from February 2023.

## Contributing

[Contributing](https://github.com/BodenmillerGroup/napari-roi/blob/main/CONTRIBUTING.md)

## Changelog

[Changelog](https://github.com/BodenmillerGroup/napari-roi/blob/main/CHANGELOG.md)

## License

[MIT](https://github.com/BodenmillerGroup/napari-roi/blob/main/LICENSE)
