
[![License BSD-3](https://img.shields.io/pypi/l/manini.svg?color=green)](https://github.com/hereariim/manini/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/manini.svg?color=green)](https://pypi.org/project/manini)
[![Python Version](https://img.shields.io/pypi/pyversions/manini.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/manini/workflows/tests/badge.svg)](https://github.com/hereariim/manini/actions)
[![codecov](https://codecov.io/gh/hereariim/manini/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/manini)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/manini)](https://napari-hub.org/plugins/manini)

Manini (**MA**chi**N**e **IN**ference  & Correct**I**on) is thought as a tool to boost the collaborative contribution of end-users to the assessment of deep learning model during their testing phase.
It is a user-Friendly plugin that enables to manually correct the result of an inference of deep learning model by an end-user. The plugin covers the following informational tasks: segmentation, classification and object detection.

## White paper

Herearii Metuarea, David Rousseau. [Toward more collaborative deep learning project management in plant phenotyping. ](https://essopenarchive.org/doi/full/10.22541/essoar.169876925.51005273/v1)

ESS Open Archive . October 31, 2023.
DOI: 10.22541/essoar.169876925.51005273/v1

----------------------------------

This plugin was written by Herearii Metuarea, PHENET engineer at LARIS (French laboratory located in Angers, France) in Imhorphen team (bioimaging research group lead) under the supervision by David Rousseau (Full professor). This plugin was designed in the context of the european project INVITE and PHENET.

![Screenshot from 2023-11-13 00-13-13](https://github.com/hereariim/manini/assets/93375163/c602e802-71b9-48ec-a9f2-cec3e4fa8220)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html!

-->

## Installation

You can install `manini` via [pip]:

    pip install manini

To install latest development version :

    pip install git+https://github.com/hereariim/manini.git


## Description

This plugin is a tool to perform image inference. The inference is open to the model for image segmentation (binary or multiclass), image classification and object detection. The dimension of image should be the same size with the input of model.
Currently compatible with tensorflow h5 models and torch torchscript models. In this format, the model file must contain all the elements of the model (architecture, weights, etc). Several ongoing developments, feel free to contact us if you have some request.

## Contact

Imhorphen team, bioimaging research group

42 rue George Morel, Angers, France

- Pr David Rousseau, david.rousseau@univ-angers.fr
- Herearii Metuarea, herearii.metuarea@univ-angers.fr 

### Scheme

![manini](https://github.com/hereariim/manini/assets/93375163/636a5e15-da0f-4387-8f37-b8ca89b4482b)

#### Input

The user must deposit two items (+1 optional item). 

- A compressed file (.zip) containing the images in RGB

```
.
└── input.zip
    ├── im_1.JPG
    ├── im_2.JPG 
    ├── im_3.JPG
    ...
    └── im_n.JPG
```

- A model file (.h5 , pt or torchscript) which is the segmentation model
- A text file (.txt) containing the names of the classes (optional)

The Ok button is used to validate the imported elements. The Run button is used to launch the segmentation.

#### Process

Correction is made by selecting some classes displayed in a widget :

- Paint panel for image segmentation

- Table for image classification

- Bounding box panel for object detection

#### Output

##### Segmentation + Detection

The plugin suggest 'Export' widget. When user select image and mask, the Save button allows you to obtain data in a compressed file. This file contains folders containing the images and their mask.

##### Classification

The Save button allows you to obtain a csv file. This file is the table on which the user had made his modifications.

#### Tutorial

Please, you can learn better if you watch a video tutorial below.

Presentation video of the context where the plugin was developped : [MANINI Napari Plugin Part 1](https://www.youtube.com/watch?v=ltbMIhApwRk)

Tutorial video to get started : [MANINI Napari Plugin Part 2](https://www.youtube.com/watch?v=HU21VQpvRAM)


## License

Distributed under the terms of the [BSD-3] license,
"manini" is free and open source software

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

[file an issue]: https://github.com/hereariim/manini/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

