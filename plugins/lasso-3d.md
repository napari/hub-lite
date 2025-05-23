
[![License BSD-3](https://img.shields.io/pypi/l/lasso-3d.svg?color=green)](https://github.com/LorenzLamm/lasso-3d/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/lasso-3d.svg?color=green)](https://pypi.org/project/lasso-3d)
[![Python Version](https://img.shields.io/pypi/pyversions/lasso-3d.svg?color=green)](https://python.org)
[![tests](https://github.com/LorenzLamm/lasso-3d/workflows/tests/badge.svg)](https://github.com/LorenzLamm/lasso-3d/actions)
[![codecov](https://codecov.io/gh/LorenzLamm/lasso-3d/branch/main/graph/badge.svg)](https://codecov.io/gh/LorenzLamm/lasso-3d)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/lasso-3d)](https://napari-hub.org/plugins/lasso-3d)

3D lasso tool to select large 3D areas

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.


## Lasso tool

This repository allows to draw 3D lassos, generate masks from these, and then mask out the image.
For instructions on how to use the plugin, please refer to the [Usage instructions](./docs/Usage.md).

<div style="text-align: center;">
<img src="https://github.com/user-attachments/assets/88851e09-6f10-4219-9b45-6f608c3e10b6" alt="lasso_gif" width="75%" />
</div>

How it works: A polygon is drawn and a mask is generated via:
### Mask via rotation
Steps:
1. Rotate and project polygon to 2D and create a pixel mask
2. Create a 3D mask by stacking the pixel mask along z
3. Rotate 3D mask s.t. it is aligned with the original polygon

This performed more efficiently than the other methods:

### Mask via projection
Steps:
1. Project all points onto the hyperplane defined by the polygon
2. Rotate all points and the polygon s.t. they are in a horizontal plane and remove z component
3. Create a binary pixel mask of the polygon
4. Check which point projections are within the polygon mask
5. reshape mask to original tomogram size

### Mask via mesh voxelization
Steps:
1. Move polygon along its normal in both directions until end of tomogram shape --> front & back polygons
2. Define a surface by combining front & back polygons into a triangular mesh
3. Voxelize the surface, giving the outline of the cone
4. Fill holes to receive a filled cone

### Mask via attaching slices
Steps:
1. Rotate and project polygon to 2D and generate a pixel mask (2D)
2. Get indices of pixel mask and rotate them back to 3D space
3. Do that for many pixel mask, varying the z-component --> will be moved into tomogram along the polygon normal
4. Binary closing to get rid of holes from integer conversion

## Installation

pip install .
<!-- You can install `lasso-3d` via [pip]:

    pip install lasso-3d



To install latest development version :

    pip install git+https://github.com/LorenzLamm/lasso-3d.git -->


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"lasso-3d" is free and open source software

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

[file an issue]: https://github.com/LorenzLamm/lasso-3d/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
