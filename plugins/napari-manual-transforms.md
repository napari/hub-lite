
[![License](https://img.shields.io/pypi/l/napari-manual-transforms.svg?color=green)](https://github.com/tlambert03/napari-manual-transforms/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-manual-transforms.svg?color=green)](https://pypi.org/project/napari-manual-transforms)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-manual-transforms.svg?color=green)](https://python.org)
[![tests](https://github.com/tlambert03/napari-manual-transforms/workflows/tests/badge.svg)](https://github.com/tlambert03/napari-manual-transforms/actions)
[![codecov](https://codecov.io/gh/tlambert03/napari-manual-transforms/branch/main/graph/badge.svg)](https://codecov.io/gh/tlambert03/napari-manual-transforms)

Interface to manually edit layer affine transforms.

- express rotations as quaternion, euler angle, or axis + angle.
- allows rotation around arbitrary origin
- currently, focusing on rigid rotations
- Alt-Drag to rotate a layer independently of the rest.
- image resampling (i.e. "apply" the transformation to create new dataset that can be saved)

![Plugin Preview](/preview.jpeg)

caveats:

- only works on 3D Image layers for now, open a feature request for other dims/layers.
- will likely result in "Non-orthogonal slicing is being requested" warnings in 2D view.

## Try it out

```python

import napari

v = napari.Viewer()
v.dims.ndisplay = 3
v.open_sample('napari', 'cells3d')
v.window.add_plugin_dock_widget('napari-manual-transforms')

napari.run()

```

----------------------------------

## Installation

You can install `napari-manual-transforms` via [pip]:

```sh
pip install napari-manual-transforms
```

To install latest development version :

```sh
pip install git+https://github.com/tlambert03/napari-manual-transforms.git
```

## License

Distributed under the terms of the [BSD-3] license,
"napari-manual-transforms" is free and open source software

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

[file an issue]: https://github.com/tlambert03/napari-manual-transforms/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


