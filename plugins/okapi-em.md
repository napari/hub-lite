
https://github.com/rosalindfranklininstitute/okapi-em

<!--
[![License](https://img.shields.io/pypi/l/okapi-em.svg?color=green)](https://github.com/rosalindfranklininstitute/okapi-em/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/okapi-em.svg?color=green)](https://pypi.org/project/okapi-em)
[![Python Version](https://img.shields.io/pypi/pyversions/okapi-em.svg?color=green)](https://python.org)
[![tests](https://github.com/perdigao1/okapi-em/workflows/tests/badge.svg)](https://github.com/rosalindfranklininstitute/okapi-em/actions)
[![codecov](https://codecov.io/gh/perdigao1/okapi-em/branch/main/graph/badge.svg)](https://codecov.io/gh/rosalindfranklininstitute/okapi-em)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/okapi-em)](https://napari-hub.org/plugins/okapi-em)
-->

A napari plugin for processing serial-FIB-SEM data.

Powered by [chafer] and [quoll].


A full description of this software is presented in biorXiv preprint paper:

https://doi.org/10.1101/2022.12.15.520541

This [napari] plugin contains the following tools:

- slice alignment using constrained SIFT
- two charge artifact suppression filters
    - directional fourier bandapass filter
    - line-by-line filter function optimiser and subtraction (requires charge artifact labels) - uses [chafer]
- fourier ring correlation (FRC) resolution estimation - uses [quoll]

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

You can install `okapi-em` via [pip]:

`>pip install okapi-em`

or using napari's plugin installation engine `Plugins->Install/Uninstall Plugins...` and filter for **Okapi-EM**.

For installing in development mode , clone this package then navigate to the cloned `okapi-em` folder and run:

`>pip install -e .`

Okapi-EM is a napari plugin. Launching napari is therefore required.

`>napari`

and then navigate `Menu->Plugins->Okapi-EM`

Note that to launch napari in older versions of python (<=3.7) you will need to use the command:

`>python -m napari`

## Computing requirements
Okapi-EM does not require powerful computers to run. None of the tools use GPU accelaration.

The minimum recommended RAM depends on the size of the data being used in napari. For a full image stack of 1Gb, it is recommended that user ensure that 3Gb of RAM is available or can be used. Modern OS's can extend physical RAM using `swap` memory (Linux) or cache (in Windows and also known as virtual memory), but processing can be significantly slower.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [Apache Software License 2.0] license,
"okapi-em" is free and open source software

## Citing

Please cite usage using the following reference.

Perdigão, L. M. A. et al. Okapi-EM – a napari plugin for processing and analysing cryogenic serial FIB/SEM images. 2022.12.15.520541 Preprint at https://doi.org/10.1101/2022.12.15.520541 (2022).


## Issues

There is currently a known issue with napari running in Linux machines, that it does not find the OpenGL driver correctly.
This will hopefully be resolved in the near future. If you bump into this issue we recommend trying to downgrade the python version. This is not an Okapi-EM problem.

If you encounter any problems, please file an issue along with a detailed description.

[quoll]: https://github.com/rosalindfranklininstitute/quoll
[chafer]: https://github.com/rosalindfranklininstitute/chafer
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


[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
