
[![License](https://img.shields.io/pypi/l/napari-pssr.svg?color=green)](https://github.com/pattonw/napari-pssr/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-pssr.svg?color=green)](https://pypi.org/project/napari-pssr)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-pssr.svg?color=green)](https://python.org)
[![tests](https://github.com/pattonw/napari-pssr/workflows/tests/badge.svg)](https://github.com/pattonw/napari-pssr/actions)
[![codecov](https://codecov.io/gh/pattonw/napari-pssr/branch/main/graph/badge.svg)](https://codecov.io/gh/pattonw/napari-pssr)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-pssr)](https://napari-hub.org/plugins/napari-pssr)

A plugin for training and applying pssr

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You can install `napari-pssr` via [pip]:

    pip install napari-pssr

Some libraries need to be updated to the most recent version to get all features.
These will be updated once they are released on pypi
    
    pip install git+https://github.com/bioimage-io/core-bioimage-io-python",
    pip install git+https://github.com/funkey/gunpowder.git@patch-1.2.3",


To install latest development version :

    pip install git+https://github.com/pattonw/napari-pssr.git

## Model download

A sample model can be downloaded from `https://github.com/pattonw/model-specs/tree/main/pssr`. This model comes with some restrictive dependencies. To use follow these steps.
1) install this plugin following the directions provided above
2) install bioimageio.core via `pip install bioimageio.core` or `conda install -c conda-forge bioimageio.core`
3) `pip install fastai==1.0.55 tifffile libtiff czifile scikit-image`
4) `pip uninstall torch torchvision` (may need multiple runs)
5) `conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch`
6) `pip install pillow==6.1.0`

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-pssr" is free and open source software

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

[file an issue]: https://github.com/pattonw/napari-pssr/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
