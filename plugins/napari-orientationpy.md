![EPFL Center for Imaging logo](https://imaging.epfl.ch/resources/logo-for-gitlab.svg)
# napari-orientationpy

Analyze orientations in 2D, 3D, and RGB images in Napari. This plugin is based on the [Orientationpy](https://gitlab.com/epfl-center-for-imaging/orientationpy/) project.

<p align="center">
    <img src="assets/ori_color-1.gif" height="400">
</p>

## Installation

You can install `napari-orientationpy` via [pip]:

    pip install napari-orientationpy

## Usage
To get started, open an image in the Napari viewer and start `napari-orientationpy` from the `Plugins` menu:

```
Plugins > Napari Orientationpy > Orientation measurement
```

1. **Select the structural scale parameter `sigma`**. This value control represents the scale at which the image gradients are computed. Try different values of `sigma` to understand what works best for your images. A reasonable guess would be the order in size, in pixels, of the structures that you are interested in. For example, if you are imaging fibers that appear to be about 4 pixels wide, try to set a value of *sigma=4*.

<p align="center">
    <img src="assets/sigmas.png" height="230">
</p>

2. **If you are analyzing a 3D image, select `fiber` or `membrane` mode**. In `fiber` mode, the orientation normals follow fibrous structures. In `membrane` mode, the orientations are normal to the surface of membranous structures.

3. **Decide which outputs you'd like to visualize.**
  - The `color-coded orientation` is a pixel-wise representation of 3D orientations as colors (similar colors = similar orientations).
  - The `orientation vectors` get rendered in a `Vectors` layer in Napari. They are sampled on a regular grid defined by the `Spacing (X)`, `Spacing (Y)` and `Spacing (Z)` values (for 2D images, the `Z` value is ignored). The length of the vectors can be rescaled based on the `energy` value of the orientation computation.
  - You can also output the local `orientation gradient` (misorientation).

4. **Compute orientation**. This button will trigger the orientation computation **only when necessary** (i.e. when the value of `sigma`, the `mode` or the `image` have changed). If you only adjust the `orientation vectors` parameters, clicking the compute button will update the results very fast.
5. **Save orientation (CSV)**. This will save the orientation measurements as a CSV table with columns `X`, `Y`, `Z`, `theta`, `phi`, `energy`, and `coherency` for all the pixels in the image. 

### Plotting the 3D orientation distribution

If you have computed **orientation vectors** for a 3D image, you can plot their spatial distribution as a `stereographic projection` along the `X`, `Y` or `Z` direction directly in Napari. Select the widget from:

```
Plugins > Napari Orientationpy > Orientation distribution (3D)
```
<p align="center">
    <img src="assets/fibers_dist.png" height="400">
</p>

## Sample images

We provide a few sample images to test our plugin. Open them from:

```
File > Open Sample > Napari Orientationpy
```

## Contributing

Contributions are very welcome. Please get in touch if you'd like to be involved in improving or extending the package.

## License

Distributed under the terms of the [BSD-3] license,
"napari-orientationpy" is free and open source software

## Issues

If you encounter any problems, please file an issue along with a detailed description.

----------------------------------

[napari]: https://github.com/napari/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[pip]: https://pypi.org/project/pip/
