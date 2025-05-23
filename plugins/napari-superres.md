
[![License BSD-3](https://img.shields.io/pypi/l/napari-superres.svg?color=green)](https://github.com/RoccoDAnt/napari-superres/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-superres.svg?color=green)](https://pypi.org/project/napari-superres)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-superres.svg?color=green)](https://python.org)
[![tests](https://github.com/RoccoDAnt/napari-superres/workflows/tests/badge.svg)](https://github.com/RoccoDAnt/napari-superres/actions)
[![codecov](https://codecov.io/gh/RoccoDAnt/napari-superres/branch/main/graph/badge.svg)](https://codecov.io/gh/RoccoDAnt/napari-superres)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/RoccoDAnt/napari-superres)](https://napari-hub.org/plugins/napari-superres)


A collection of super-resolution microscopy FF-SRM methods.

Open-source implementation of methods for Fluorescence Fluctuation based Super Resolution Microscopy (FF-SRM):

Review: [Alva et al., 2022. “Fluorescence Fluctuation-Based Super-Resolution Microscopy: Basic Concepts for an Easy Start.” Journal of Microscopy, August.](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13135)

MSSR article: [Torres-García, E., Pinto-Cámara, R., Linares, A. et al. Extending resolution within a single imaging frame. Nat Commun 13, 7452 (2022).](https://doi.org/10.1038/s41467-022-34693-9)

ESI article: [Idir Yahiatene, Simon Hennig, Marcel Müller, Thomas Huser (2015/2016). "Entropy-based Super-resolution Imaging (ESI): From Disorder to Fine Detail" ACS Photonics 8, 2 (2015)](https://doi.org/10.1021/acsphotonics.5b00307)

SOFI article: [T. Dertinger, R. Colyer, G. Iyer, and J. Enderlein. Fast, background-free, 3D super-resolution optical fluctuation imaging (SOFI). PNAS 52, 106 (2009) ](https://doi.org/10.1073/pnas.0907866106)

SRRF article: [Gustafsson, N., Culley, S., Ashdown, G., D. M. Owen, P. Matos Pereira, and R. Henriques. Fast live-cell conventional fluorophore nanoscopy with ImageJ through super-resolution radial fluctuations. Nat Commun 7, 12471 (2016)](https://www.nature.com/articles/ncomms12471)

MUSICAL article: [K. Agarwal and R. Machan, Multiple Signal Classification Algorithm for super-resolution fluorescence microscopy, Nature Communications, vol. 7, article id. 13752, (2016)](https://www.nature.com/articles/ncomms13752)



Methods implemented:
- MSSR
- ESI
- SOFI
- SRRF
- MUSICAL
- Split channels


| **Super Resolution Radial Fluctuations (SRRF)**  | **Mean-Shift Super Resolution (MSSR)** | **Entropy-based Super-resolution Imaging (ESI)** |
| --- | --- | --- |
| ![](https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/Fig_7_SRRF_Alva_2022.png) | ![](https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/Fig_2a_MSSR_Garcia_2021.png) | ![](https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/Fig_6_ESI_Alva_2022.png) |
from Fig. 7 of [Alva et al., 2022](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13135) | from Fig. 2 of [García et al., 2021](https://www.biorxiv.org/content/10.1101/2021.10.17.464398v2.full)|  from Fig. 6 of [Alva et al., 2022](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13135)|


Repositories available:
- [ESI](https://github.com/biophotonics-bielefeld/ESI) GitHub repository
- [PySOFI](https://github.com/xiyuyi-at-LLNL/pysofi) GitHub repository
- [MUSICAL](https://sites.google.com/site/uthkrishth/musical) Google site

----------------------------------


This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->


## Installation
First install napari viewer (if you haven't):

    conda create -y -n napari-env -c conda-forge python=3.9
    conda activate napari-env
    pip install "napari[all]"

For details check: https://napari.org/stable/




You can install the plugin [graphically](https://github.com/LIBREhub/napari-LatAm-Workshop-2023/blob/napari-superres/docs/day3/napari-superres/napari-superres_installation_guide.pdf).

or install latest development version :

    pip install git+https://github.com/RoccoDAnt/napari-superres.git

You might need to install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) first.

----------------------------------
Examples of use:

| **Original**  | **tMSSR** |
| --- | --- |
| <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/single-frame-good-exposure.png" width=100% height=100%> </p>| <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/tmssr-mean-mag2.png" width=48% height=48%> </p>|
| Parameters: | Amplification: 2, Order: 0, PSF FWHM: 6, <br> Interpolation: Bicubic, Statistical integration: CV*sigma |

| **Original**  | **ESI** |
| --- | --- |
| <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/synt.png" width=40% height=40%> </p> | <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/ESI.png" width=50% height=50%> </p> |
| Parameters: | image in output: 2, bins: 2, Order: 2 |

| **Original**  | **SOFI** |
| --- | --- |
|<p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/noSOFI.png" width=100% height=100%> </p> | <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/SOFI.png" width=100% height=100%> </p> |
| Parameters: | Amplification factor: 2, Moment Order: 4, lambda parameter: 1.5, No. Iterations: 20, Window size: 100|

| **Original**  | **SRRF** |
| --- | --- |
|<p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/synt.png" width=50% height=50%> </p> | <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/SRRF.png" width=50% height=50%> </p>|
| Parameters: | Amplification: 2, Spatial radius: 5, Symmetry Axis: 6, Start frame: 0, End frame: 48|

| **Original**  | **MUSICAL** |
| --- | --- |
| <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/musical_mean.png" width=70% height=100%> </p> | <p align="center"> <img src="https://raw.githubusercontent.com/RoccoDAnt/napari-superres/main/docs/MUSICAL-CardioMyoblast_Mitochondria.png" width=70% height=100%> </p>|
| Parameters: | Emission [nm]: 510 NA: 1.4, Mag: 100, Pizel size: 8000, Threshold: -0.5, Alpha: 4, Subpixels per pixel: 20|
----------------------------------



## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-superres" is free and open source software

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

[file an issue]: https://github.com/RoccoDAnt/napari-superres/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
