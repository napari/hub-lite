
[![License MIT](https://img.shields.io/pypi/l/napari-trackpy.svg?color=green)](https://github.com/rhoitink/napari-trackpy/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-trackpy.svg?color=green)](https://pypi.org/project/napari-trackpy)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-trackpy.svg?color=green)](https://python.org)
[![tests](https://github.com/rhoitink/napari-trackpy/workflows/tests/badge.svg)](https://github.com/rhoitink/napari-trackpy/actions)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-trackpy)](https://napari-hub.org/plugins/napari-trackpy)

Plugin to do [trackpy] particle tracking on 3D microscopy data within [napari]. Currently only tracking of XYZ data is implemented.

## Installation

You can install `napari-trackpy` via [pip]:

    pip install napari-trackpy

To install latest development version :

    pip install git+https://github.com/rhoitink/napari-trackpy.git

## How to use this plugin?
* Load your XYZ data (using [napari-aicsimageio])
* Make sure to split channels into different layers, such that the layer only contains 3D (XYZ) data
* Open the widget for the tracking plugin via `Plugins` > `XYZ particle tracking`
* Optimize the tracking settings for your dataset, for an extensive description of the settings, visit [this tutorial](http://soft-matter.github.io/trackpy/dev/tutorial/tracking-3d.html)
* Save your tracking data into the `.xyz` file format using `Ctrl`+`S` (on the points layer) or via the menu `File` > `Save Selected Layer(s)...`

## Contributing

Contributions are very welcome. Tests can be run with [tox].

## License

Distributed under the terms of the [MIT] license,
"napari-trackpy" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[trackpy]: https://github.com/soft-matter/trackpy
[napari-aicsimageio]: https://github.com/AllenCellModeling/napari-aicsimageio
[MIT]: http://opensource.org/licenses/MIT

[file an issue]: https://github.com/rhoitink/napari-trackpy/issues

[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
