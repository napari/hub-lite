
[![License](https://img.shields.io/pypi/l/napari-labeling.svg?color=green)](https://github.com/tomburke-rse/napari-labeling/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-labeling.svg?color=green)](https://pypi.org/project/napari-labeling)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-labeling.svg?color=green)](https://python.org)
[![tests](https://github.com/tomburke-rse/napari-labeling/workflows/tests/badge.svg)](https://github.com/tomburke-rse/napari-labeling/actions)
[![codecov](https://codecov.io/gh/tomburke-rse/napari-labeling/branch/main/graph/badge.svg)](https://codecov.io/gh/tomburke-rse/napari-labeling)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-labeling)](https://napari-hub.org/plugins/napari-labeling)

This is a napari-plugin based on the [labeling project].

It allows the generation of overlapping labels in one layer, save and load of this layer in a json-based file format and
it contains a widget to explore the overlapping labels layer and select specific segments with a mouse click .

Please note that currently, the widget part only works by adding it through code with:

    from napari_labeling import edit_widget
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(edit_widget)

An example on how to achieve this can be found in the [main.py] on GitHub.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You can install `napari-labeling` via [pip]:

    pip install napari-labeling




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-labeling" is free and open source software

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

[labeling project]: https://github.com/Labelings/Labeling
[main.py]: https://github.com/Labelings/Labeling/blob/main/main.py
[file an issue]: https://github.com/Labelings/napari-labeling/issues


