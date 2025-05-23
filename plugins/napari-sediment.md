
[![License BSD-3](https://img.shields.io/pypi/l/napari-sediment.svg?color=green)](https://github.com/guiwitz/napari-sediment/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-sediment.svg?color=green)](https://pypi.org/project/napari-sediment)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-sediment.svg?color=green)](https://python.org)
[![tests](https://github.com/guiwitz/napari-sediment/workflows/tests/badge.svg)](https://github.com/guiwitz/napari-sediment/actions)
[![codecov](https://codecov.io/gh/guiwitz/napari-sediment/branch/main/graph/badge.svg)](https://codecov.io/gh/guiwitz/napari-sediment)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-sediment)](https://napari-hub.org/plugins/napari-sediment)

This napari plugin is designed to hpyerspectral images of sediment cores. It is composed of three interfaces allowing the user to:

- import HDR images
- normalize the images using white and dark references
- mask unwanted regions
- perform spectral dimensionality reduction via minimum noise fraction analysis
- perform spatial dimensionality reduction based on pixel purity indices
- identify representative end-members by clustering pure pixels
- select relevant regions in spectra to compute absorption indices and create absorption maps 

### Pre-processing: Sediment widget

The sediment widget allows the user to import an HDR image and to normalize it using white and dark references. The widget also allows the user to mask unwanted regions of the images.

## Documentation

You can find a detailed documentation [here](https://guiwitz.github.io/napari-sediment).
## Installation

Create a conda environment and activate it. We highly recommend to use the new conda version called mamba to speed up the installation process. You can install it from [here](https://github.com/conda-forge/miniforge#mambaforge). If you don't use mamba, replace the mamba command by conda in the following instructions:

    mamba create -n sediment python=3.9 napari pyqt -c conda-forge
    mamba activate sediment

Then you can install `napari-sediment` use:

    pip install git+https://github.com/guiwitz/napari-sediment.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-sediment" is free and open source software

## Authors

This plugin has been developed by Guillaume Witz at the Data Science Lab of the University of Bern in collaboration with Petra Zahajská, Institue of Geography of the University of Bern. Funding for development was provided by Prof. Martin Grosjean, Institute of Geography of the University of Bern.

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

[file an issue]: https://github.com/guiwitz/napari-sediment/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
