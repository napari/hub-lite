 # napari-bigfish

[![License MIT](https://img.shields.io/pypi/l/napari-bigfish.svg?color=green)](https://github.com/MontpellierRessourcesImagerie/napari-bigfish/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-bigfish.svg?color=green)](https://pypi.org/project/napari-bigfish)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-bigfish.svg?color=green)](https://python.org)
[![tests](https://github.com/MontpellierRessourcesImagerie/napari-bigfish/workflows/tests/badge.svg)](https://github.com/MontpellierRessourcesImagerie/napari-bigfish/actions)
[![codecov](https://codecov.io/gh/MontpellierRessourcesImagerie/napari-bigfish/branch/main/graph/badge.svg)](https://codecov.io/gh/MontpellierRessourcesImagerie/napari-bigfish)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-bigfish)](https://napari-hub.org/plugins/napari-bigfish)

A napari-plugin providing an alternative GUI for [Big-FISH](https://github.com/fish-quant/big-fish). Big-FISH is a python package for the analysis of smFISH images.

The plugin provides a graphical user interface for some of the functionality in Big-FISH. Currently implemented are:

 * Gaussian-background subtraction
 * FISH-spot detection with 
	* Elimination of duplicates
	* Auto-detection of threshold
* Dense-region decomposition

The plugin further implements by itself:

* Counting of spots per cell, inside and outside of the nucleus
* Batch processing on a list of images


You can find the user and the api-documentation of napari-bigfish [here](https://montpellierressourcesimagerie.github.io/napari-bigfish/).
 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `napari-bigfish` via [pip]:

    pip install napari-bigfish


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.


## License

Distributed under the terms of the [MIT] license,
"napari-bigfish" is free and open source software


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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
