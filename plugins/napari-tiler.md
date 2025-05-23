
[![License](https://img.shields.io/pypi/l/napari-tiler.svg?color=green)](https://github.com/tdmorello/napari-tiler/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tiler.svg?color=green)](https://pypi.org/project/napari-tiler)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tiler.svg?color=green)](https://python.org)
[![tests](https://github.com/tdmorello/napari-tiler/workflows/tests/badge.svg)](https://github.com/tdmorello/napari-tiler/actions)
[![codecov](https://codecov.io/gh/tdmorello/napari-tiler/branch/main/graph/badge.svg)](https://codecov.io/gh/tdmorello/napari-tiler)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-tiler)](https://napari-hub.org/plugins/napari-tiler)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/napari-tiler.svg)](https://pypistats.org/packages/napari-tiler)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Development Status](https://img.shields.io/pypi/status/napari-tiler.svg)](https://github.com/tdmorello/napari-tiler)

N-dimensional tiling and merging support for napari

This plugin allows the user to split an image into a stack of tiles and subsequently merge the tiles to reconstruct the orignal image.
See [Tiler](https://pypi.org/project/tiler/) by [@thelay](https://github.com/the-lay) for more details.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

### Option 1 (recommended)

You can install `napari-tiler` from the napari plugin manager. Go to `Plugins -> Install/Uninstall Package(s)`, then search for `napari-tiler`. Click `Install`.

### Option 2

You can also install `napari-tiler` via [pip]:

    pip install napari-tiler

To install latest development version:

    pip install git+https://github.com/tdmorello/napari-tiler.git

## Quick Start

1. Open a file in napari. The file may have any number of dimensions (e.g. z-stack, time series, ...)
2. Start the plugin ( `Plugins -> napari-tiler: make_tiles` )
3. Select the input layer from the dropdown box
4. Select parameters for tiling
5. Click `Run`

## Contributing

This project uses [Poetry](https://github.com/python-poetry/poetry) for dependency management.
To set up the development environment, it is recommended to use:

    conda env create -f environment.yaml

Contributions are very welcome. Tests can be run with [tox], please ensure the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-tiler" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

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

[file an issue]: https://github.com/tdmorello/napari-tiler/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

