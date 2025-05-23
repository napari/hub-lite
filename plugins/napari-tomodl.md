
[![License MIT](https://img.shields.io/pypi/l/napari-tomodl.svg?color=green)](https://github.com/marcoso96/napari-tomodl/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tomodl.svg?color=green)](https://pypi.org/project/napari-tomodl)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tomodl.svg?color=green)](https://python.org)
[![tests](https://github.com/marcoso96/napari-tomodl/workflows/tests/badge.svg)](https://github.com/marcoso96/napari-tomodl/actions)
[![codecov](https://codecov.io/gh/marcoso96/napari-tomodl/branch/main/graph/badge.svg)](https://codecov.io/gh/marcoso96/napari-tomodl)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-tomodl)](https://napari-hub.org/plugins/napari-tomodl)

A plugin for optical projection tomography reconstruction with model-based neural networks.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->
## Introduction and usage

ToMoDL allows users to reconstruct tomography images from its raw projections juts from uploading them as an ordered stack of files into the napari viewer.

1 - Load ordered stack: Click File -> Open Files as Stack... and load the angular projections for parallel beam optical tomography reconstruction.

![plot](https://raw.githubusercontent.com/marcoso96/ToMoDL/main/napari-tomodl/figures/fig3.png)

2 - Select the current volume in the dropdown menu with the button 'Select image layer'. Notice that the projections should be in grayscale and more than one slide in the stack.

![plot](https://raw.githubusercontent.com/marcoso96/ToMoDL/main/napari-tomodl/figures/fig4.png)

3 - If the axis is not correctly aligned in acquisition time, we provide an algorithm to do so by clicking on 'Align axis'. This will align the sinogram respect to the center of the detector in order to maximise the variance of the reconstructions. See Walls et al. 

4 - Reshape the reconstructed volume to a desired size. This can be useful to prevent exhausting your computing capabilities.

5 - Clip to circle should be False by default.

6 - Choose if filtering should be used. By the moment we only allow using ramp filtering for FBP only (both CPU and GPU).

7 - Choose the correct order of the axis of the projections (T -> Theta axis, Q -> Detector axis)

8 - Reconstruct! A new Layer should be created on top of the projections stack containing the reconstructed volume.

![plot](https://raw.githubusercontent.com/marcoso96/ToMoDL/main/napari-tomodl/figures/fig2.png)

## Installation

This package requires [torch-radon] for optimized GPU tomographic reconstruction:

    pip install 'torch-radon @ https://rosh-public.s3-eu-west-1.amazonaws.com/radon-v2/cuda-11.1/torch-1.8/torch_radon-2.0.0-cp38-cp38-linux_x86_64.whl'

and `PyTorch == 1.8.0` via wheel, which can be downloaded and installed with: 

    pip install 'torch @ https://download.pytorch.org/whl/cu111/torch-1.8.0%2Bcu111-cp38-cp38-linux_x86_64.whl'

You can install `napari-tomodl` via [pip]:

    pip install napari-tomodl




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-tomodl" is free and open source software

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
[torch-radon]: https://github.com/matteo-ronchetti/torch-radon
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
