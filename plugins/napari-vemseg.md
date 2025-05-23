
<img width="250"  src="https://github.com/MatousE/napari-vemseg/blob/main/images/VEMSEG-FINAL.svg"> 

# napari-vemseg


[![License BSD-3](https://img.shields.io/pypi/l/napari-vemseg.svg?color=green)](https://github.com/MatousE/napari-vemseg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-vemseg.svg?color=green)](https://pypi.org/project/napari-vemseg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-vemseg.svg?color=green)](https://python.org)
[![tests](https://github.com/MatousE/napari-vemseg/workflows/tests/badge.svg)](https://github.com/MatousE/napari-vemseg/actions)
[![codecov](https://codecov.io/gh/MatousE/napari-vemseg/branch/main/graph/badge.svg)](https://codecov.io/gh/MatousE/napari-vemseg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-vemseg)](https://napari-hub.org/plugins/napari-vemseg)

A simple plugin to do semi-automated segmentation within napari using vemseg built on
XGBoost.

## Installation
### `conda` Installation and Environment Creation
To start with a conda environment must be created.
```
conda create -n vemseg-env python=3.8
conda activate vemseg-env
```
### `napari` Instillation
We must then install [napari]:

```
pip install "napari[all]"
```
### `napari-vemseg` Instillation
You can finally install `napari-vemseg` via [pip]:
```
conda install pyopencl
pip install napari-vemseg
```
## Usage
### Train VEMClassifier

### Predict Using Pretrained VEMClassifier


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-vemseg" is free and open source software

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
