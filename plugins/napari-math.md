
[![License](https://img.shields.io/pypi/l/napari-math.svg?color=green)](https://github.com/zacsimile/napari-math/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-math.svg?color=green)](https://pypi.org/project/napari-math)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-math.svg?color=green)](https://python.org)
[![tests](https://github.com/zacsimile/napari-math/workflows/tests/badge.svg)](https://github.com/zacsimile/napari-math/actions)
[![codecov](https://codecov.io/gh/zacsimile/napari-math/branch/main/graph/badge.svg)](https://codecov.io/gh/zacsimile/napari-math)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-math)](https://napari-hub.org/plugins/napari-math)

This package provides a GUI interfrace for simple mathematical operations on image, point and surface layers.

- addition
- subtraction
- multiplication
- division
- logical and, or, xor
- z-projection (mean and sum)

Operations can be peformed on a single layer or between Image layers (functionaly pending for Surface and Point layers), 
for example adding one layer to another.

When performing operations on two images of different sizes, the result will be the size of the smallest
of the two images.

----------------------------------

<!--
This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.
-->

## Installation

You can install `napari-math` via [pip]:

    pip install napari-math




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-math" is free and open source software

## Issues

If you encounter any problems, please file an [issue] along with a detailed description.

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


