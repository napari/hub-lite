
[![License BSD-3](https://img.shields.io/pypi/l/napari-biomag-annotator.svg?color=green)](https://github.com/biomag-lab/napari-biomag-annotator/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-biomag-annotator.svg?color=green)](https://pypi.org/project/napari-biomag-annotator)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-biomag-annotator.svg?color=green)](https://python.org)
[![tests](https://github.com/biomag-lab/napari-biomag-annotator/workflows/tests/badge.svg)](https://github.com/biomag-lab/napari-biomag-annotator/actions)
[![codecov](https://codecov.io/gh/biomag-lab/napari-biomag-annotator/branch/main/graph/badge.svg)](https://codecov.io/gh/biomag-lab/napari-biomag-annotator)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-biomag-annotator)](https://napari-hub.org/plugins/napari-biomag-annotator)

An annotator tool collection by the BIOMAG group.

This plugin allows object annotation on 2/3D images using 4 assisted annotation methods arising from two napari plugins:

- [napari-annotatorj](https://github.com/spreka/napari-annotatorj)
- [napari-nD-annotator](https://github.com/bauerdavid/napari-nD-annotator)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-biomag-annotator` via [pip]:

    pip install napari[all]
    pip install napari-biomag-annotator



To install latest development version :

    pip install git+https://github.com/biomag-lab/napari-biomag-annotator.git


On Linux distributions, the following error may arise upon napari startup after the installation of the plugin: `Could not load the Qt platform plugin “xcb” in “” even though it was found`. In this case, the manual install of `libxcb-xinerama0` for Qt is required:

    sudo apt install libxcb-xinerama0

### Bundled napari app
The bundled application version of [napari](https://github.com/napari/napari/releases) allows the pip install of plugins in the .zip distribution. After installation of this release, napari-annotatorj can be installed from the `Plugins --> Install/Uninstall plugins...` menu by searching for its name and clicking on the `Install` button next to it.

### Script
Single-file install is supported on [**Windows**](#windows) and [Linux](#linux) (currently). It will create a virtual environment named `napariAnnotatorEnv` in the parent folder of the cloned repository, install the package via pip and start napari. It requires a valid Python install.

#### Windows
To start it, run in the Command prompt

    git clone https://github.com/biomag-lab/napari-biomag-annotator.git
    cd napari-biomag-annotator
    install.bat

Or download [install.bat](https://github.com/biomag-lab/napari-biomag-annotator/blob/main/install.bat) and run it from the Command prompt.

After install, you can use [startup_napari.bat](https://github.com/biomag-lab/napari-biomag-annotator/blob/main/startup_napari.bat) to activate your installed virtual environment and run napari. Run it from the Command prompt with:

    startup_napari.bat


#### Linux
To start it, run in the Terminal

    git clone https://github.com/biomag-lab/napari-biomag-annotator.git
    cd napari-annotatorj
    install.sh

Or download [install.sh](https://github.com/biomag-lab/napari-biomag-annotator/blob/main/install.sh) and run it from the Terminal.

After install, you can use [startup_napari.sh](https://github.com/biomag-lab/napari-biomag-annotator/blob/main/startup_napari.sh) to activate your installed virtual environment and run napari. Run it from the Terminal with:

    startup_napari.sh

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-biomag-annotator" is free and open source software

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

[file an issue]: https://github.com/biomag-lab/napari-biomag-annotator/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
