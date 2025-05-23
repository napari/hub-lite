![logo](./docs/_static/logo.png) napari-locan
==================================================

[![License](https://img.shields.io/github/license/super-resolution/napari-locan)](https://github.com/super-resolution/napari-locan/blob/main/LICENSE.md)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-locan)](https://napari-hub.org/plugins/napari-locan)
[![PyPI](https://img.shields.io/pypi/v/napari-locan.svg?color=green)](https://pypi.org/project/napari-locan)
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/napari-locan)](https://anaconda.org/conda-forge/napari-locan)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-locan.svg?color=green)](https://python.org)
[![test-py-matrix](https://github.com/super-resolution/napari-locan/actions/workflows/test_py_matrix.yml/badge.svg)](https://github.com/super-resolution/napari-locan/actions/workflows/test_py_matrix.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/super-resolution/napari-locan/branch/main/graph/badge.svg)](https://codecov.io/gh/super-resolution/napari-locan)
[![Documentation Status](https://readthedocs.org/projects/napari-locan/badge/?version=latest)](https://napari-locan.readthedocs.io/en/latest/?badge=latest)

Load, visualize and analyze single-molecule localization microscopy (SMLM) data.

napari-locan is a napari plugin that implements a subset of methods from [locan],
a python-based library with code for analyzing SMLM data.
Locan provides extended functionality that is better suited for script- or
notebook-based analysis procedures.
napari-locan is well suited for exploratory data analysis within napari.

For details on usage and development of napari-locan please read the [documentation].

## Installation

Make sure to have Qt bindings installed in your python environment of choice.

You can install napari-locan from PyPI:

    pip install napari-locan

or from conda-forge:

    mamba install -c conda-forge napari-locan

Please read the [documentation on installation] for more details.

## Usage

![](https://github.com/super-resolution/napari-locan/raw/main/docs/resources/screenshot_0.png?raw=true)

Please read the [documentation] for details.

## Contributing

Contributions are very welcome.
Please read the [documentation on development] for details.

## Credit

The plugin was developed in the Department of Biotechnology and Biophysics,
Würzburg University, Germany.
It is based on locan. So credit goes to the [locan developers]
and can be [cited](https://github.com/super-resolution/napari-locan/blob/main/CITATION.cff).

## License

Distributed under the terms of the
[BSD-3](http://opensource.org/licenses/BSD-3-Clause)
license, "napari-locan" is free and open source software.
See the [LICENSE](https://github.com/super-resolution/napari-locan/blob/main/LICENSE.md) file for details.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[locan]: https://github.com/super-resolution/locan
[locan developers]: https://github.com/super-resolution/locan

[documentation]: https://napari-locan.readthedocs.io
[documentation on installation]: https://napari-locan.readthedocs.io/en/latest/source/installation.html
[documentation on development]: https://napari-locan.readthedocs.io/en/latest/source/development.html
[file an issue]: https://github.com/super-resolution/napari-locan/issues
