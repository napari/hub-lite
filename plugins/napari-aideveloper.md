
[![License](https://img.shields.io/pypi/l/napari-aideveloper.svg?color=green)](https://github.com/zcqwh/napari-aideveloper/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-aideveloper.svg?color=green)](https://pypi.org/project/napari-aideveloper)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-aideveloper.svg?color=green)](https://python.org)
[![tests](https://github.com/zcqwh/napari-aideveloper/workflows/tests/badge.svg)](https://github.com/zcqwh/napari-aideveloper/actions)
[![codecov](https://codecov.io/gh/zcqwh/napari-aideveloper/branch/main/graph/badge.svg)](https://codecov.io/gh/zcqwh/napari-aideveloper)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-aideveloper)](https://napari-hub.org/plugins/napari-aideveloper)

[napari_aideveloper](https://www.napari-hub.org/plugins/napari-aideveloper) is a napari-plugin derived from [AIDeveloper](https://github.com/maikherbig/AIDeveloper) that allows you to train, evaluate, and apply deep neural nets for image classification within a graphical user-interface (GUI).


<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `napari-aideveloper` via [pip]:

    pip install napari-aideveloper

## Introduction
### Main functions
* [Build](#build)
* [History](#history)

****

### Build 
#### 1. Load data
Drag and drop your data in .rtdc (HDF5) format into the file table and set the class and training/validation.
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/00_Load_data.gif?raw=true)

#### 2. Choose Neural Networks
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/01_choose%20NN.gif?raw=true)

#### 3. Set model storage path
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/02_save_model.gif?raw=true)

#### 4. Start fitting
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/03_start_fitting.gif?raw=true)
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/04_fitting.gif?raw=true)

#### Preview image
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/05_preview.gif?raw=true)

#### Image augmentation
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/main/Tutorial/06_augmentation.gif?raw=true)

****

### History
#### 1. Load meta data
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/development/Tutorial/GIF/History/01_Load_metadata.gif?raw=true)

#### 2. Check model details
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/development/Tutorial/GIF/History/02_model_detail.gif?raw=true)

#### 3. Rolling median & Linear fit
![alt Load_data](https://github.com/zcqwh/napari-aideveloper/blob/development/Tutorial/GIF/History/03_rolling_linear.gif?raw=true)






## Contributing

Contributions are very welcome. You can submit your pull request on [GitHub](https://github.com/zcqwh/napari-aideveloper/pulls). Tests can be run with [tox], please ensure the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-aideveloper" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/zcqwh/napari-aideveloper/issues) along with a detailed description.

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


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.
