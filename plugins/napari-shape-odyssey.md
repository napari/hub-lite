
[![License BSD-3](https://img.shields.io/pypi/l/napari-shape-odyssey.svg?color=green)](https://github.com/jo-mueller/napari-shape-odyssey/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-shape-odyssey.svg?color=green)](https://pypi.org/project/napari-shape-odyssey)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-shape-odyssey.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-shape-odyssey/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-shape-odyssey/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-shape-odyssey/branch/main/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-shape-odyssey)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-shape-odyssey)](https://napari-hub.org/plugins/napari-shape-odyssey)

Analyze shapes of meshes: This plugin provides advanced measures of shape for meshes. It is based largely on the following libraries and tools:

* [PyFM](https:/github.com/robinmagnet/pyfm)
* [boundary-first-flattening](https://github.com/GeometryCollective/boundary-first-flattening)

## Shape analysis

This plugin provides Laplace spectra ([Reuter, Wolter, Peinecke (2005)](https://dl.acm.org/doi/abs/10.1145/1060244.1060256)), heat kernel signatures ([Bronstein & Kokkinos (2010)](https://ieeexplore.ieee.org/abstract/document/5539838/)) & wave kernel signatures ([Audrey, Schlickewei, Cremers et al.](https://ieeexplore.ieee.org/abstract/document/6130444)).

**Laplace spectra** can be imagined to be the equivalent of resonance modes on the surface of a mesh. The resonance and the resonance modes can, for typical objects, look like this:

![](https://github.com/jo-mueller/napari-shape-odyssey/raw/main/docs/imgs/Eigenvalues.gif)

**Heat kernel signatures**: Heat dissipation on a mesh depends on local geometry. You can use the heat kernel signature to easily generate a large number of local features of shape

![](https://github.com/jo-mueller/napari-shape-odyssey/raw/main/docs/imgs/heat_kernel_signature.gif)

## Unwrapping

This plugin provides a number of methods to unwrap a mesh into basic shapes such as spheres or disks. The method relies on [boundary-first flattening](https://github.com/GeometryCollective/boundary-first-flattening) - currently it's only available on Windows.

![](https://github.com/jo-mueller/napari-shape-odyssey/raw/main/docs/imgs/unwrap_to_sphere.png)



----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-shape-odyssey` via [pip]:

´´´bash
    pip install napari-shape-odyssey
    napari-skimage-regionprops @ git+https://github.com/jo-mueller/napari-skimage-regionprops.git
    pyFM @ git+https://github.com/RobinMagnet/pyFM.git
´´´




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-shape-odyssey" is free and open source software

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
