
[![License](https://img.shields.io/pypi/l/iacs_ipac_reader.svg?color=green)](https://github.com/zcqwh/iacs_ipac_reader/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/iacs_ipac_reader.svg?color=green)](https://pypi.org/project/iacs_ipac_reader)
[![Python Version](https://img.shields.io/pypi/pyversions/iacs_ipac_reader.svg?color=green)](https://python.org)
[![tests](https://github.com/zcqwh/iacs_ipac_reader/workflows/tests/badge.svg)](https://github.com/zcqwh/iacs_ipac_reader/actions)
[![codecov](https://codecov.io/gh/zcqwh/iacs_ipac_reader/branch/main/graph/badge.svg)](https://codecov.io/gh/zcqwh/iacs_ipac_reader)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/iacs_ipac_reader)](https://napari-hub.org/plugins/iacs_ipac_reader)

A plugin used a convolutional neural network (CNN) to distinguish single platelets, platelet clusters, and white blood cells and performed classical image analysis for each subpopulation individually. Based on the derived single-cell features for each population, a Random Forest (RF) model was trained and used to classify COVID-19 associated thrombosis and non-COVID-19 associated thrombosis.

More information about IACS/iPAC.  
__IACS__: DOI: [10.1016/j.cell.2018.08.028](https://www.sciencedirect.com/science/article/pii/S0092867418310444)   
__iPAC__: DOI: [10.7554/eLife.52938](https://elifesciences.org/articles/52938)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You can install `iacs_ipac_reader` via [pip]:

    pip install iacs_ipac_reader



To install latest development version :

    pip install git+https://github.com/zcqwh/iacs_ipac_reader.git


## Introduction

The iacs-ipac-reader plugin mainly include 3 functional tabs:

* iPAC
* IACS
* AID classif.



### iPAC image contour tracker
<center>Interface of iPAC contour tracker</center>    

![ipac.](https://github.com/zcqwh/iacs_ipac_reader/blob/main/Tutorial/pictures/ipac.png?raw=true "iPAC")

### IACS image contour tracker
<center>Interface of IACS contour tracker</center>    

![iacs.](https://github.com/zcqwh/iacs_ipac_reader/blob/main/Tutorial/pictures/iacs.png?raw=true "IACS")

### AID classif.
<center>Interface of AID classif.</center>     
 
![AID_classif.](https://github.com/zcqwh/iacs_ipac_reader/blob/main/Tutorial/pictures/classifier.jpg?raw=true "AID classif")



## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"iacs_ipac_reader" is free and open source software

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

[file an issue]: https://github.com/zcqwh/iacs_ipac_reader/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/



