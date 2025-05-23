### A napari plugin for restoration and enhancement of Cryo-FIB/SEM images

[![License Apache 2.0](https://img.shields.io/pypi/l/napari-cryofibsem-imgpro.svg?color=green)](https://github.com/EMCRUMC/napari-cryofibsem-imgproc/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-cryofibsem-imgpro.svg?color=green)](https://pypi.org/project/napari-cryofibsem-imgpro)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-cryofibsem-imgpro.svg?color=green)](https://python.org)
[![tests](https://github.com/shainatorumc/napari-cryofibsem-imgpro/workflows/tests/badge.svg)](https://github.com/shainatorumc/napari-cryofibsem-imgpro/actions)
[![codecov](https://codecov.io/gh/shainatorumc/napari-cryofibsem-imgpro/branch/main/graph/badge.svg)](https://codecov.io/gh/shainatorumc/napari-cryofibsem-imgpro)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-cryofibsem-imgpro)](https://napari-hub.org/plugins/napari-cryofibsem-imgpro)

----------------------------------

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation
It is recommended to create a fresh [conda] environment with Python 3.12 and napari:

    conda create -n imgpro_env -c conda-forge python=3.12.0 napari pyqt
    
Activate the environment and upgrade napari:

    conda upgrade napari

You can install `napari-cryofibsem-imgpro` via [pip]:

    pip install napari-cryofibsem-imgpro

To install latest development version :

    pip install git+https://github.com/shainatorumc/napari-cryofibsem-imgpro.git

## Usage 
Cryo-FIB/SEM Image Processing offers 5 functions: curtaining artifact removal, charging artifact removal, noise reduction, contrast enhancement, and uneven stack brightness correction. Using the widgets, the user can choose the input image or stack, set the function parameters, and call the function. These functions can be used in combination with each other or individually, depending on the image processing requirements. 

![widget.png](docs%2Fimages%2Fwidget.png)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-cryofibsem-imgpro" is free and open source software

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

[file an issue]: https://github.com/shainatorumc/napari-cryofibsem-imgpro/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[conda]: https://docs.conda.io/en/latest/

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.
