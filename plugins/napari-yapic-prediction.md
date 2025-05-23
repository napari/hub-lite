
[![License](https://img.shields.io/pypi/l/napari-yapic-prediction.svg?color=green)](https://github.com/yapic/napari-yapic-prediction/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-yapic-prediction.svg?color=green)](https://pypi.org/project/napari-yapic-prediction)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-yapic-prediction.svg?color=green)](https://python.org)
[![tests](https://github.com/yapic/napari-yapic-prediction/workflows/tests/badge.svg)](https://github.com/yapic/napari-yapic-prediction/actions)
[![codecov](https://codecov.io/gh/yapic/napari-yapic-prediction/branch/master/graph/badge.svg?token=amah2YwOpx)](https://codecov.io/gh/yapic/napari-yapic-prediction)

A napari widget plugin to perform YAPiC model segmentation prediction in the napari window. 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Description

This napari plugin provides a widget to upload a [YAPiC] trained model and perform segmentation over all the present images in the napari window. The segmentation results are uploaded as napari layers into the viewer automatically with the name structure of *imgename_prediction*.

## Installation

1. Please install either GPU or CPU version of tensorflow that is compatible with your `cuda` and `cudnn` libraries before installing the plugin depending on your system.
One of the plugin dependency is `yapic` that currently has sensitivity to tensorflow versions.

2. You can install `napari-yapic-prediction` via [pip]:

    ```pip install napari-yapic-prediction```

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-yapic-prediction" is free and open source software

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
[file an issue]: https://github.com/yapic/napari-yapic-prediction/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[YAPiC]: https://yapic.github.io/yapic/


