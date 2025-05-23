
[![License BSD-3](https://img.shields.io/pypi/l/napari-merge-stardist-masks.svg?color=green)](https://github.com/gatoniel/napari-merge-stardist-masks/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-merge-stardist-masks.svg?color=green)](https://pypi.org/project/napari-merge-stardist-masks)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-merge-stardist-masks.svg?color=green)](https://python.org)
[![tests](https://github.com/gatoniel/napari-merge-stardist-masks/workflows/tests/badge.svg)](https://github.com/gatoniel/napari-merge-stardist-masks/actions)
[![codecov](https://codecov.io/gh/gatoniel/napari-merge-stardist-masks/branch/main/graph/badge.svg)](https://codecov.io/gh/gatoniel/napari-merge-stardist-masks)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-merge-stardist-masks)](https://napari-hub.org/plugins/napari-merge-stardist-masks)

This is the [napari] plugin for [StarDist OPP]. Checkout our [paper] for more information.

----------------------------------

## Usage

Read the [tutorial] and download pre-trained models from our [Zenodo repository].

In PowerShell, when you do not have sufficient GPU support, run napari without CUDA support, i.e.,:
```
$env:CUDA_VISIBLE_DEVICES=-1; napari
```


## Installation

You can install `napari-merge-stardist-masks` via [pip]:

    pip install napari-merge-stardist-masks



To install latest development version :

    pip install git+https://github.com/gatoniel/napari-merge-stardist-masks.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-merge-stardist-masks" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## How to cite
```bibtex
@article{https://doi.org/10.1111/mmi.15064,
author = {Jelli, Eric and Ohmura, Takuya and Netter, Niklas and Abt, Martin and Jiménez-Siebert, Eva and Neuhaus, Konstantin and Rode, Daniel K. H. and Nadell, Carey D. and Drescher, Knut},
title = {Single-cell segmentation in bacterial biofilms with an optimized deep learning method enables tracking of cell lineages and measurements of growth rates},
journal = {Molecular Microbiology},
volume = {n/a},
number = {n/a},
pages = {},
keywords = {3D segmentation, biofilm, deep learning, image analysis, image cytometry, Vibrio cholerae},
doi = {https://doi.org/10.1111/mmi.15064},
url = {https://onlinelibrary.wiley.com/doi/abs/10.1111/mmi.15064},
eprint = {https://onlinelibrary.wiley.com/doi/pdf/10.1111/mmi.15064},
abstract = {Abstract Bacteria often grow into matrix-encased three-dimensional (3D) biofilm communities, which can be imaged at cellular resolution using confocal microscopy. From these 3D images, measurements of single-cell properties with high spatiotemporal resolution are required to investigate cellular heterogeneity and dynamical processes inside biofilms. However, the required measurements rely on the automated segmentation of bacterial cells in 3D images, which is a technical challenge. To improve the accuracy of single-cell segmentation in 3D biofilms, we first evaluated recent classical and deep learning segmentation algorithms. We then extended StarDist, a state-of-the-art deep learning algorithm, by optimizing the post-processing for bacteria, which resulted in the most accurate segmentation results for biofilms among all investigated algorithms. To generate the large 3D training dataset required for deep learning, we developed an iterative process of automated segmentation followed by semi-manual correction, resulting in >18,000 annotated Vibrio cholerae cells in 3D images. We demonstrate that this large training dataset and the neural network with optimized post-processing yield accurate segmentation results for biofilms of different species and on biofilm images from different microscopes. Finally, we used the accurate single-cell segmentation results to track cell lineages in biofilms and to perform spatiotemporal measurements of single-cell growth rates during biofilm development.}
}
```

## Credits

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

[paper]: https://doi.org/10.1111/mmi.15064
[StarDist OPP]: https://github.com/gatoniel/merge-stardist-masks
[tutorial]: https://merge-stardist-masks.readthedocs.io/en/latest/napari-plugin.html
[Zenodo repository]: https://doi.org/10.5281/zenodo.7704410

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

[file an issue]: https://github.com/gatoniel/napari-merge-stardist-masks/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
