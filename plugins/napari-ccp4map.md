
[![License](https://img.shields.io/pypi/l/napari-ccp4map.svg?color=green)](https://github.com/biberger/napari-ccp4map/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-ccp4map.svg?color=green)](https://pypi.org/project/napari-ccp4map)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-ccp4map.svg?color=green)](https://python.org)
[![tests](https://github.com/biberger/napari-ccp4map/workflows/tests/badge.svg)](https://github.com/biberger/napari-ccp4map/actions)
[![codecov](https://codecov.io/gh/biberger/napari-ccp4map/branch/master/graph/badge.svg)](https://codecov.io/gh/biberger/napari-ccp4map)

Enables napari to read .map files in the ccp4 format.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-ccp4map` via [pip]:

    pip install napari-ccp4map

## Usage
If the plugin was installed correctly, it will pop up in a napari window under Plugins->Install/Uninstall Plugins.
You can either drag&drop filed into the window to read them, or search for a folder/file using Ctrl+O.

## How it works
This plugin simply reads a file and allows [gemmi](https://github.com/project-gemmi/gemmi) to interact with it. Then, numpy turns the file into an array.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-ccp4map" is free and open source software

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

[file an issue]: https://github.com/biberger/napari-ccp4map/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


