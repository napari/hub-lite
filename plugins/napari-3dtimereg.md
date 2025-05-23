
[![License BSD-3](https://img.shields.io/pypi/l/napari-3dtimereg.svg?color=green)](https://gitlab.pasteur.fr/gletort/napari-3dtimereg/-/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-3dtimereg.svg?color=green)](https://pypi.org/project/napari-3dtimereg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-3dtimereg.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-3dtimereg)](https://napari-hub.org/plugins/napari-3dtimereg)

Temporal registration of 2D/3D movies on one channel based on [itk-elastix](https://pypi.org/project/itk-elastix/), and transpose alignement to the other channels.

Adaptated from [multireg](https://gitlab.pasteur.fr/gletort/multireg) for temporal movies.
For a tutorial on using `elastix` for registration, see [this tutorial](https://m-albert.github.io/elastix_tutorial/intro.html).


----------------------------------
## Installation

* You can install the plugin directly in `Napari` by going to `Plugins>Install/Uninstall plugins` and search for `napari-3dtimereg`

* Or you can install `napari-3dtimereg` via [pip]:

    pip install napari-3dtimereg


## Usage

You can launch `3dtimereg` in napari by going to `Plugins>Do 3D movie registration (napari-3dtimereg)`.

### Choose movie and reference chanel

First, choose select the movie that you want to register. The plugin will create a folder `aligned` in the folder of your selected movie where the results will be saved.

Choose the color chanel on which to calculate the registration (`reference chanel`). Color chanels are numbered from 0 to nchanels, and you can see their respective number in the layer list on the left panel of Napari. Click on `Update` when the correct chanel is selected to go to the registration calculation step.

### Calculate temporal alignement

The registration is calculated iteratively from one frame to another. Thus the first frame is not moved and all the other frames are aligned to it.
You can tune several parameters in this plugin:

![parameters screenshot](./imgs/parameters.png "Registration parameters")

The other parameters are parameters to use [itk-elastix](https://elastix.lumc.nl/) to calculate the registration.
* `show log`: to see the log of Elastix calculation
* `do rigid`: performs a rigid (affine) transformation step, that allowed to correct for translations/rotations.
* `do bspline`: performs a b-spline based transformation step, that allowed for local deformations in the image.
* `show advanced parameters`: to control the parameters used in the rigid and/or bspline transformations. These parameters control the size of the local registrations calculated, the resolutions at which the transformations are calculated, and can thus greatly impact the results.
* `final order`: is the final order of the B-Splines used for the registration. 
* `resolution`: is the number of consecutives resolutions at which the registration will be made. First the registration is made at the lowest level of resolution, correcting global deformations/motions, then at each step, the registration is done on higher resolution, allowing to correct for more local deformations.
* `final spacing`: is the physical spacing of the smallest resolution.
* `iterations`: are the maximum number of iterations allowed to minimize the distance between the two images for each resolution and type of registration.

If both rigid and bspline transformations, the program first applies the rigid transformation to allow for a global registration of the images. Then it will performs the second step of b-spline transformation that can includes local deformations.

For each frame, after calculating the registration on the reference chanel, the plugin will apply the calculated transformation to all the other color chanels of the initial movie. All results are saved as separated images in the `aligned` folder during the computation.

### Create the final aligned movie

When all frames have been processed, each color chanel and each frame have been saved in the `aligned` folder as separated images. This is usefull to calculate the registration on large movies without having to keep all the intermediates and calculated images in memory. You can directly use these separated images, or reconstruct a single composite movie of the result.

If you click on `Concatenate aligned images` on the plugin interface, the plugin will create a single composite movie from the aligned images, save it and delete the separated images in the `aligned` folder. 

## License

Distributed under the terms of the [BSD-3] license, "napari-3dtimereg" is free and open source software


[napari]: https://github.com/napari/napari
[@napari]: https://github.com/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
