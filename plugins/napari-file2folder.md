
[![License MIT](https://img.shields.io/pypi/l/napari-file2folder.svg?color=green)](https://github.com/GuignardLab/napari-file2folder/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-file2folder.svg?color=green)](https://pypi.org/project/napari-file2folder)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-file2folder.svg?color=green)](https://python.org)
[![tests](https://github.com/jules-vanaret/napari-file2folder/workflows/tests/badge.svg)](https://github.com/jules-vanaret/napari-file2folder/actions)
[![codecov](https://codecov.io/gh/jules-vanaret/napari-file2folder/branch/main/graph/badge.svg)](https://codecov.io/gh/jules-vanaret/napari-file2folder)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-file2folder)](https://napari-hub.org/plugins/napari-file2folder)

<img src="https://github.com/GuignardLab/tapenade/blob/main/imgs/tapenade3.png" width="100">

A plugin to inspect bioimages (e.g. .tif, .czi, .nd2, .lsm...) and save them as individual .tif files in a folder.

`napari-file2folder` is a [napari] plugin that is part of the [Tapenade](https://github.com/GuignardLab/tapenade) project. Tapenade is a tool for the analysis of dense 3D tissues acquired with deep imaging microscopy. It is designed to be user-friendly and to provide a comprehensive analysis of the data.

If you use this plugin for your research, please [cite us](https://github.com/GuignardLab/tapenade/blob/main/README.md#how-to-cite).

## Overview

<img src="imgs/napari-file2folder-demo.gif"/>

This plugin allows you to inspect (possibly large) bioimages by displaying their shape (number of elements in each dimension), and allowing you to save each element along a chosen dimension as a separate .tif file in a folder. This is useful when you have a large movie or stack of images and you want to save each frame or slice as a separate file. Optionally, the plugin allows the user to visualize the middle element of a given dimension to help the user decide which dimension to save as separate files.

The plugin currently supports the following file formats:
- .tif
- .ome.tiff
- .zarr
- .ome.zarr
- .nd2
- .lsm
- .czi

This plugin leverages [tifffile], [bioio], and [zarr] to circumvent loading the entire images in memory, which allows inspection of very large images.

> [!CAUTION]
> When inspecting the middle element of a dimension, or when saving one element of a dimension as a separate file, the plugin loads the element in memory, which means that at least this lone element must fit in memory.

## Installation

The plugin obviously requires [napari] to run. If you don't have it yet, follow the instructions [here](https://napari.org/stable/tutorials/fundamentals/installation.html).

The simplest way to install `napari-file2folder` is via the [napari] plugin manager. Open Napari, go to `Plugins > Install/Uninstall Packages...` and search for `napari-file2folder`. Click on the install button and you are ready to go!

You can install `napari-file2folder` via [pip]:

    pip install napari-file2folder




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-file2folder" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[tifffile]: https://github.com/cgohlke/tifffile
[bioio]: https://github.com/bioio-devs/bioio
[zarr]: https://github.com/zarr-developers/zarr-python
