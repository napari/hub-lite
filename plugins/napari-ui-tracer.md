
[![License MIT](https://img.shields.io/pypi/l/napari-ui-tracer.svg?color=green)](https://github.com/dalthviz/napari-ui-tracer/raw/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-ui-tracer.svg?color=green)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/napari-ui-tracer.svg?color=green)](https://pypi.org/project/napari-ui-tracer)
[![PyPI download month](https://img.shields.io/pypi/dm/napari-ui-tracer.svg?color=green)](https://pypi.org/project/napari-ui-tracer/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/napari-ui-tracer.svg?color=blue)](https://anaconda.org/conda-forge/napari-ui-tracer)
[![conda download count](https://img.shields.io/conda/d/conda-forge/napari-ui-tracer.svg?color=blue)](https://anaconda.org/conda-forge/napari-ui-tracer)
[![tests](https://github.com/dalthviz/napari-ui-tracer/workflows/tests/badge.svg)](https://github.com/dalthviz/napari-ui-tracer/actions)
[![codecov](https://codecov.io/gh/dalthviz/napari-ui-tracer/branch/main/graph/badge.svg?token=E6je6vXOSA)](https://codecov.io/gh/dalthviz/napari-ui-tracer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-ui-tracer)](https://napari-hub.org/plugins/napari-ui-tracer)

A plugin to help understand Napari UI components and locate their code definition

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

![GIF showing Napari UI tracer's functionality](https://raw.githubusercontent.com/dalthviz/napari-ui-tracer/main/images/napari-ui-tracer.gif)

## Installation

You can install `napari-ui-tracer` via [pip]:

    pip install napari-ui-tracer

Or via [conda]:

    conda install -c conda-forge napari-ui-tracer

To install latest development version :

    pip install git+https://github.com/dalthviz/napari-ui-tracer.git

## Usage

1. Show the plugin inside the napari interface:

    * You can launch napari with the plugin visible running:

            napari -w napari-ui-tracer

    * Or select it from `Plugins > Napari UI tracer widget`

2. Check the `Enable Qt event filter` checkbox:
    * Use `Ctrl/Cmd + Mouse button right click` to see the information available about any widget inside napari
    * An option to show objects documentation (object class docstring) can be used by checking the `Show object documentation` checkbox

3. Check the `Enable application events logging` checkbox:
    * A log like information with the events generated when interacting with the application will appear
    * Some configuration options are available:
        * `Stack depth`: Stack depth to show. Default to 20
        * `Allowed nested events`: How many sub-emit nesting levels to show (i.e. events that get triggered by other events). Default to 0

4. If you want to explore the related widget or event module source file, click the link in the output section of the plugin (the module file will open if you have a registered program to open such kind of file)

## Contributing

Contributions are very welcome. Pre-commit is used for formatting. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-ui-tracer" is free and open source software

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

[file an issue]: https://github.com/dalthviz/napari-ui-tracer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[conda]: https://docs.conda.io/projects/conda/en/stable/
