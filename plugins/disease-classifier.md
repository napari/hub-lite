
[![License](https://img.shields.io/pypi/l/disease-classifier.svg?color=green)](https://github.com/zcqwh/disease-classifier/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/disease-classifier.svg?color=green)](https://pypi.org/project/disease-classifier)
[![Python Version](https://img.shields.io/pypi/pyversions/disease-classifier.svg?color=green)](https://python.org)
[![tests](https://github.com/zcqwh/disease-classifier/workflows/tests/badge.svg)](https://github.com/zcqwh/disease-classifier/actions)
[![codecov](https://codecov.io/gh/zcqwh/disease-classifier/branch/main/graph/badge.svg)](https://codecov.io/gh/zcqwh/disease-classifier)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/disease-classifier)](https://napari-hub.org/plugins/disease-classifier)

A napari plugin for disease classification based on iPAC images.



## Installation

You can install `disease-classifier` via [pip]:

    pip install disease-classifier



To install latest development version :

    pip install git+https://github.com/zcqwh/disease-classifier.git

## Introduction
#### Load data (.rtdc or .bin)
* Drag and drop the data in .rtdc or .bin into the files table.
* Click eye button to preview images.
![](https://github.com/zcqwh/disease-classifier/blob/main/Tutorial/Gif/01_Load_preview.gif?raw=true)


#### Choose model and classify

* Choose the model folder including CNN and RF/PLDA.
* Check the data.
* Click classify.
![](https://github.com/zcqwh/disease-classifier/blob/main/Tutorial/Gif/02_model_classify.gif?raw=true)

#### Preview classification results
* Click the eye button to preview the result.
* Click the header to show all.
![](https://github.com/zcqwh/disease-classifier/blob/main/Tutorial/Gif/03_preview_result.gif?raw=true)


#### Save results
* Click “Add classification to .rtdc file” button to save results.
![](https://github.com/zcqwh/disease-classifier/blob/main/Tutorial/Gif/04_save.gif?raw=true)


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"disease-classifier" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

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

[file an issue]: https://github.com/zcqwh/disease-classifier/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

