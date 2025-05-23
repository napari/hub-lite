
[![License](https://img.shields.io/pypi/l/napari-medical-image-formats.svg?color=green)](https://github.com/MBPhys/Partial-Aligner/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/Partial-Aligner.svg?color=green)](https://pypi.org/project/Partial-Aligner)
[![Python Version](https://img.shields.io/pypi/pyversions/Partial-Aligner.svg?color=green)](https://python.org)


A napari plugin to affine transform images and parts of images in 2D and 3D. It was developed in the context of brain slice registration and solves multiple, related problems when working with histology slices.

----------------------------------

## Installation

You can install `Partial-Aligner` via [pip]:

    pip install Partial-Aligner
    
To make full use of this plugin, please also install the sister plugins:

    pip install Label-Creator
    pip install Layer-Data-Replace
    pip install World2Data

## Usage

It is important to note that this plugin is part of a group of plugins ([Label-Creator](https://github.com/DKFZ-TMTRR/Label-Creator, "Creates Labels"), [Layer-Data-Replace](https://github.com/DKFZ-TMTRR/Layer-Data-Replace, "Replaces the data of a layer with other data"), [World2Data](https://github.com/DKFZ-TMTRR/World2Data, "Applies a transformation to an image")) which are intended to be used together. 

The principle workflow with this plugin is as follows:

1. Load an image of interest (ioi) using standard napari.
2. Find out meaningful transformation parameters for the ioi (or part of it) based on what you see in the viewer.
3. (optional) Save the affine transformation matrix (can later be applied to other modalities)
4. Apply the transformation to create a new, altered version of the ioi (use plugin [World2Data](https://github.com/DKFZ-TMTRR/World2Data, "Applies a transformation to an image"))

Decisions on the parameters (step 2) are made based on the problem at hand:

- Registration: You have a second (fixed) image and you want to align your ioi to that image? Transform your whole ioi! Just play with the transformation parameters until you are happy with the alignment of ioi and fixed image.

<p align="center">
    <img src="https://user-images.githubusercontent.com/36212786/149524198-9a25b6dc-4169-4546-85b3-7c2f57fccc97.png" width="50%" height="50%">  <br /> 
     <i>DAPI staining (red) before (left) and after (right) manual registration on an MRI image (green).</i> 
</p>

- Histology artifact repair: Parts of your histology slice are misplaced? Transform the misplaced parts! Label them and change the transformation parameters for the misplaced parts until you are happy with their alignment with the rest of the image.

<p align="center">
<img src="https://user-images.githubusercontent.com/36212786/149526385-09aeebe2-d03e-4dd4-a424-d0f3af207529.png" width="50%" height="50%">  <br /> 
     <i> Original slice with misplaced region (left), marked using the label function (middle) and after manual adjustment (right), where the misplaced region (green) was cut and newly positioned.</i> 
</p>

To make this plugin run reasonably fast, the affine transformations are not applied to the image data in real time. Instead, the internal napari viewing parameters are changed according to the transformation parameters. Therefore, to save transformed image data, the [World2Data](https://github.com/DKFZ-TMTRR/World2Data, "Applies a transformation to an image") plugin is used, which calculates and saves the resulting image based on the internal napari viewing parameters.


Here we showcase a resulting multimodal 3D alignment of a whole mouse brain. The modalities are CT, MRI, simulated radiation dose distributions, DAPI staining and DNA-damage repair foci, with a Nissl-staining mouse atlas as template.

https://user-images.githubusercontent.com/36212786/149530462-51a53631-bf74-459b-ab4e-572c52cf2692.mov







## Contributing

Contributions are very welcome. Tests can be run with [tox].

## License

Distributed under the terms of the [BSD-3] license,
"Partial-Aligner" is free and open source software.

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
[file an issue]: https://github.com/MBPhys/Partial-Aligner/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


