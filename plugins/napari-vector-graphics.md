
[![License BSD-3](https://img.shields.io/pypi/l/napari-vector-graphics.svg?color=green)](https://github.com/JoOkuma/napari-vector-graphics/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-vector-graphics.svg?color=green)](https://pypi.org/project/napari-vector-graphics)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-vector-graphics.svg?color=green)](https://python.org)
[![tests](https://github.com/JoOkuma/napari-vector-graphics/workflows/tests/badge.svg)](https://github.com/JoOkuma/napari-vector-graphics/actions)
[![codecov](https://codecov.io/gh/JoOkuma/napari-vector-graphics/branch/main/graph/badge.svg)](https://codecov.io/gh/JoOkuma/napari-vector-graphics)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-vector-graphics)](https://napari-hub.org/plugins/napari-vector-graphics)

Helper plugin to export napari viewer content as SVG

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-vector-graphics` via [pip]:

    pip install napari-vector-graphics

If you want to be able to vectorize segmentation layers, you will need `python-opencv-headless`.
To install it, run:

    pip install "napari-vector-graphics[all]"


To install latest development version :

    pip install git+https://github.com/JoOkuma/napari-vector-graphics.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-vector-graphics" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[file an issue]: https://github.com/JoOkuma/napari-vector-graphics/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
