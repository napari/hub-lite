
[![License](https://img.shields.io/pypi/l/bbii-decon.svg?color=green)](https://github.com/gdellaire/bbii-decon/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/bbii-decon.svg?color=green)](https://pypi.org/project/bbii-decon)
[![Python Version](https://img.shields.io/pypi/pyversions/bbii-decon.svg?color=green)](https://python.org)
[![tests](https://github.com/gdellaire/bbii-decon/workflows/tests/badge.svg)](https://github.com/gdellaire/bbii-decon/actions)
[![codecov](https://codecov.io/gh/gdellaire/bbii-decon/branch/main/graph/badge.svg)](https://codecov.io/gh/gdellaire/bbii-decon)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/bbii-decon)](https://napari-hub.org/plugins/bbii-decon)

Projected Barzilai-Borwein Image Deconvolution with Infeasible Iterates (BBii-Decon)


The projected Barzilai-Borwein method of image deconvolution utilizing infeasible iterates (BBii-Decon), utilizes Barzilai-Borwein (BB) or projected BB (PBB) method and enforces a nonnegativity constraint, but allows for infeasible iterates between projections. This algorithm (BBii) results in faster convergence than the basic PBB method, while achieving better quality images, with reduced background than the unconstrained BB method (1). 

The code represented is based on the original BBii algorithm written in MatLab by Kathleen Fraser and Dirk Arnold, which was ported to python 3.8 by Graham Dellaire, Dirk Arnold and Kathleen Fraser for non-commercial use.

The first implementation shown here is for 2D deconvolution using a known 2D PSF of 256 X 256 pixels, and images of at least 256 pixels in one dimension. One file implements just the deconvolution of a blurred image, while the second file contains a modification of the BBii-Decon algorithm that has a built in heuristic for measuring image reconstruction error relative to a ground truth image. For general 2D deconvolution, either a theoretical 2D PSF (if you know the optical properties of your system) or the central in focus image of a fluorescent bead taken with the same imaging setup (lens, magnification, camera) can produce a suitable PSF.

### GPU-acceleration

For most 2D deconvolution, optimal results are obtained with 10 iterations of the algorithm. However, if processing takes too long, acceleration using graphics processing units (GPUs) may make sense, especially for processing larger images with >10 iterations or 3D images. (Note: At this time BBii-Decon is optimized for 2D deconvolution, with a 3D implementation planned in future). 

This plugin supports accelerated processing using the [cupy](https://cupy.dev) library. To make use of it, please follow 
[the instructions](https://docs.cupy.dev/en/stable/install.html#installing-cupy-from-conda-forge) to install cupy. 
Installation may look like this:
```
conda create --name cupy_p38 python=3.8
conda activate cupy_p38
conda install -c conda-forge cupy cudatoolkit=10.2
```

If cupy installation worked out, you will find another checkbox in the user interface. By activating it, processing 
should become faster by factor 5-10, depending on processed image data and use GPU hardware.

![img.png](https://github.com/gdellaire/BBii-Decon/raw/main/demo/use_GPU_checkbox.png)

## Usage - napari

You can use the BBii deconvolution from within napari by clicking the menu `Plugins > bbii-decon > bbii deconvolution`. 
In the dialog, select the PSF, the image to process (a) and click on `Run`. After a moment, the deconvolved image (b) 
will show up.

![img.png](https://github.com/gdellaire/BBii-Decon/raw/main/demo/screenshot_napari.png)

## Usage from python

You can also call the function from python. There is a full working example in [this notebook](demo/BBii_Decon_2D_2021.ipynb).

```
from bbii_decon import bbii

bbii(PSF, image, number_of_iterations = 15, tau = 1.0e-08, rho = 0.98)
```


## Citation
1) [Kathleen Fraser, Dirk V. Arnold, and Graham Dellaire (2014). Projected Barzilai-Borwein
method with infeasible iterates for nonnegative least-squares image deblurring. In Proceedings
of the Eleventh Conference on Computer and Robot Vision (CRV 2014), Montreal, Canada, pp.
189--194.](https://ieeexplore.ieee.org/abstract/document/6816842)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You can install `bbii-decon` via [pip]:

    pip install bbii-decon


## Installation for developers

Clone the github repository:

```
conda install git

git clone https://github.com/gdellaire/BBii-Decon.git

cd BBii-Decon

pip install -e .
```

## Deployment to pypi

For deploying the plugin to the python package index (pypi), one needs a [pypi user account](https://pypi.org/account/register/) 
first. For deploying the plugin to pypi, one needs to install some tools:

```
python -m pip install --user --upgrade setuptools wheel
python -m pip install --user --upgrade twine
```

The following command allows us to package the souce code as a python wheel. Make sure that the 'dist' and 'build' folders are deleted before doing this:

```
python setup.py sdist bdist_wheel
```

This command ships the just generated to pypi:

```
python -m twine upload --repository pypi dist/*
```

[Read more about distributing your python package via pypi](https://realpython.com/pypi-publish-python-package/#publishing-to-pypi).


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"bbii-decon" is free and open source software

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

[file an issue]: https://github.com/gdellaire/bbii-decon/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


