
[![License BSD-3](https://img.shields.io/pypi/l/multireg.svg?color=green)](https://gitlab.pasteur.fr/gletort/multireg/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/multireg.svg?color=green)](https://pypi.org/project/multireg)
[![Python Version](https://img.shields.io/pypi/pyversions/multireg.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/multireg)](https://napari-hub.org/plugins/multireg)

Registration of 3D multiplex images with one common chanel, based on itk-elastix.

Napari plugin to align 3D stacks that have one common field of view in one chanel used to calculate the alignement. The plugin will apply the registration to all other chanels and output one final stack with all the aligned chanels.

The stacks **must have one common chanel** (typically cell junctions and nuclei) that is used to calculate the registration transformation. It can be rotated, translated, deformed, and with a wider field of view. 
Then the calculated transformation is applied to all the other chanels for each stack.

The final result is **one multi-chanel 3D stack**, with the first chanel being an average (or not) of the common chanel and each other chanel the registered chanels from the multiple stacks. The common chanel can be averaged between the different chanels, which improves its quality.

The plugin save and load files to a folder named `aligned` and created in the same directory as the source images.

Example of usage of this module is in the case of imaging the same cells with washing out or moving the sample in between. The corresponding cells will not be at the same position in the new stacks, and can even be deformed by the procedure. This plugin realign the images based on one common chanel on which the transformation is calculated. 

----------------------------------
## Installation

* You can install the plugin directly in `Napari` by going to `Plugins>Install/Uninstall plugins` and search for `multireg`

* Or you can install `multireg` via [pip]:

    pip install multireg


## Usage

You can launch `multireg` in napari by going to `Plugins>multireg: do multiplex registration`.

### Fixed image
It will open a prompt to ask you to select the reference (fixed) image, compared to which all other images will be aligned.
Then you have to choose the `reference chanel` that will be used in all the stacks to calculate the alignement. So this chanel should be common to all stacks.

![](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/plugin_step0.png)

#### Reference points
The first part of the registration relies on reference points manually selected, because the common field of view can be quite far from each other in the acquisition. So first a affine registration is applied to bring close the region of interest between the two stacks to match. 
<br> *Note that if your stacks did not move a lot then you could calculate the transformation without using the reference points. There's an option in the alignement calculation panel for this.*

![](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/plugin_fixedpoints.png)

You have to manually placed a few reference points (4-5 should be enough). Try to spread them in the image (in x,y and z) on landmarks to recognize them in other images. 

To add a new reference point, click on the "plus" sign in the left panel. To select one, click on the arrow icon (or press 3), then on the point. You can move the point in x and y. To move it in z, press `u` for up and `d` for down. 

When all points are placed, save them. The **points have to be saved** to be correctly loaded by the alignement calculation step.
Then click on `Fixed points done` to continue to the next step.


### Moving images
Then you can choose one of the images you want to align with the reference image. Its chanel that is common to the fixed image should be the same chanel, selected in the first step (the `reference chanel`). Select the file of the moving image to align by clicking on `select file`. This will open the new image and go to the step of placing the moving points in this image.

When you will have process all the moving images, you can click on `All done` to finish the plugin by creating the [resulting stack](#create-resulting-image).

![moving image step](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/plugin_movingimg.png)

#### Moving points
You now have to locate where the region of interest (the fixed image) is in your new image and find the landmarks referenced in the fixed image are in this new image. This allows the plugin to put together the region of interest in the two images in a first step, before to fine-tune the registration.

For each point placed in the fixed image, place the corresponding point in the moving image. By default, the moving points are placed close to the fixed points. 
* Each point must have the same label (number) as its corresponding fixed points to associate them correctly. You can change a point label by selecting it and putting the new value in `param` and clicking on `update`.


* When a point is selected, you can drag it to its desired location. To move it in the Z direction, you can press `u` to move it to the next Z (up direction) and `d` (down) to the previous Z. The viewed slice will also move, following the point new position, when you do so.

* You can click on `side_by_side_view` to see the two images (fixed and moving) with their placed points at the same time.

* You can click on `two_windows_view` to see the fixed image and points in a separate Napari window. This allows to have visualize separatly the fixed and moving images and points, and thus to see different z-slices or zoom for each image. The new window will be closed automatically by the plugin if you unselect this option or when you click on `Moving done`.

![two window](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/twowin.png)

When all the moving points have been correctly placed, click on `Save points` to save this positions and let it be usable by the alignement step. The points **have to be saved** in the point file to be correctly loaded in the alignement step.

### Alignement calculation
This step is the core of the plugin. The transformation necessary to change the moving image to match with the fixed image on the `reference chanel` is calculated based on [itk-elastix](https://pypi.org/project/itk-elastix/) python module. It is decomposed in two steps. 

1. First a global **affine registration** is performed, based on the correspondance between the reference and moving points (`do rigid` option). This allows to locate the fixed image postion within the moving image and apply a first **shearing, scaling, rotation and translation** to super-impose the region of interest. 

2. The second step fine-tunes the registration. It doesn't use the reference points (except if rigid transformation was not selected) anymore but calculate the matching based on the images local intensities. **Non-rigid transformation** based on B-spline is performed at this step, thus allowing to compensate for **local deformations** in the moving image (`do bspline` option).

The option `use reference points` determines if the previously placed reference points should be used or if the registration is only based on intensities matching. It's possible to use only the intensities if the two images are not so far away from each other. The reference points will be used only in the first pass (either rigid or bspline) when both are selected. If only one is selected, the points will be used on the selected transformation.

The option `strong_weight_points` allows to give more importance to reference points than to intensities matching when calculating the registration. The weights will be 0.2 for the intensity metric and 0.8 for points metric. Note that if both rigid and bspline transformations are selected, the second transformation (bspline) do not use the points.

![apply alignement step](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/interm.png)


You can click on `show advanced parameters` to tune the parameters of the non rigid transformation. After calculating the registration, the plugin will add a new layer, which is the moving image after alignement, so you can check the sucess of the regristration. `show intermediate_layer` will also add the moving image aligned after the first step only (the points matching with affine registration).

![calculate alignement step](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/align.png)


### Apply alignement
Once the calculated registration is satisfying, you can apply it to all the chanels of your moving image, or only to a few. By default, all chanels are selected in the `Apply alignement` panel, but you can unselect the chanels that you don't want to align in the parameter `align chanels`. 
When you click on `Align images`, the plugin will apply the transformation on the selected chanels of the moving image and save each of them in the `aligned` folder as individual `.tif` files. 

![apply alignement step](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/goalign.png)

### Create resulting image
This step allows to save a single 3D multi-chanels stack with all the aligned chanels. 

The common chanel present in all the images can be averaged together after alignement to obtain a much less noisy image. By default, the aligned `reference chanel` of all the images are averaged together to create the final image first chanel. However, it is possible to unselect some images in the first panel (`average chanels` parameter) if you do not wish to use all the images or do an average.

![create result image](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/create.png)

Then each aligned chanel of all the images that were not the reference chanel are stacked together in the final resulting image. Here also, if you don't want to keep all the other chanels in the resulting image, you can unselect the one that you don't want stacked, in the `add_chanels` parameter. 
All the aligned chanels have been previously saved in the `aligned` folder. If `delete_files` is checked (default) all these interemediate files will be deleted and only the final resulting stack will be saved in that folder.

You will end-up with a final 3D multi-chanels stack, saved as a `.tif` file in the `aligned` folder, with the same name as your fixed image. It can have a lot of chanels if you stacked together multiple images.
In napari, you can separate the chanels by right clicking on the layer and select `Split stack`. 
In Fiji, you can make the stack as a composite to see the chanels with different colors.

![final image](https://gitlab.pasteur.fr/gletort/multireg/raw/main/imgs/reslayer.png)

## License
Distributed under the terms of the [BSD-3] license,
"multireg" is free and open source software

## Plugin initialization
This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.


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
