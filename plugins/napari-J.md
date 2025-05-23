
[![License](https://img.shields.io/pypi/l/napari-J.svg?color=green)](https://github.com/MontpellierRessourcesImagerie/napari-J/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-J.svg?color=green)](https://pypi.org/project/napari-J)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-J.svg?color=green)](https://python.org)
[![tests](https://github.com/MontpellierRessourcesImagerie/napari-J/workflows/tests/badge.svg)](https://github.com/MontpellierRessourcesImagerie/napari-J/actions)
[![codecov](https://codecov.io/gh/MontpellierRessourcesImagerie/napari-J/branch/master/graph/badge.svg)](https://codecov.io/gh/MontpellierRessourcesImagerie/napari-J)

A plugin to exchange data with FIJI and to use FIJI image analysis from napari.
Current features are:

 * get the active image from FIJI
 * send a screenshot to FIJI
 * get a set of points from the FIJI results table
 * filter the points in napari
 * send the filtered points back to FIJI
 
Known problems:

* Crashes on linux  when the file-dialog is opened. Workaround: Set the option ``Use JFileChooser to open/save`` from the ``Edit>Options>Input/Output`` menu.
* 03.05.2022 - Currently you need to have the range of the quality values for point between 0 and 255, in the new version they can have any range, but we are waiting for the bug in napari 0.4.15 to be fixed to release this. 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-J` via [pip]:

    pip install napari-J

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-J" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/MontpellierRessourcesImagerie/napari-J/issues) along with a detailed description.

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
[file an issue]: https://github.com/MontpellierRessourcesImagerie/napari-J/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
