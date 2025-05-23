
[![License BSD-3](https://img.shields.io/pypi/l/napari-xgboost.svg?color=green)](https://github.com/haesleinhuepf/napari-xgboost/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-xgboost.svg?color=green)](https://pypi.org/project/napari-xgboost)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-xgboost.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-xgboost/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-xgboost/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-xgboost/branch/main/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-xgboost)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-xgboost)](https://napari-hub.org/plugins/napari-xgboost)

A plugin for pixel classification using [XGBoost](https://xgboost.readthedocs.io/en/stable/), inspired by [Digital Sreeni's Youtube video](https://www.youtube.com/watch?v=yqkNslkzLk4).

Note: This plugin is work-in-progress. Check out the [github issues](https://github.com/haesleinhuepf/napari-xgboost/issues) to see what's currently being worked on.

## Usage

Load an example image into napari. Add a Labels layer by clicking on this button:

![img.png](https://github.com/haesleinhuepf/napari-xgboost/raw/main/docs/images/img.png)

Then, draw a sparse annotation on the image. Try to draw thin lines on background and foreground, e.g. like this:

![img_1.png](https://github.com/haesleinhuepf/napari-xgboost/raw/main/docs/images/img_1.png)

Then click the menu `Layers > Segment > Train Pixel Classifier (XGBoost)`.

![img_2.png](https://github.com/haesleinhuepf/napari-xgboost/raw/main/docs/images/img_2.png)

In the dialog, select the original image and the labels layer. Also enter a filename where the model should be saved. 
Afterwards, click on `Run` to explore the result.

![img_3.png](https://github.com/haesleinhuepf/napari-xgboost/raw/main/docs/images/img_3.png)

## Installation

You can install `napari-xgboost` via [pip]:

    pip install napari-xgboost

To install latest development version :

    pip install git+https://github.com/haesleinhuepf/napari-xgboost.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-xgboost" is free and open source software

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

[file an issue]: https://github.com/haesleinhuepf/napari-xgboost/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
