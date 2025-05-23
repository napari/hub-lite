
[![License](https://img.shields.io/pypi/l/napari-pystackreg.svg?color=green)](https://github.com/glichtner/napari-pystackreg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-pystackreg.svg?color=green)](https://pypi.org/project/napari-pystackreg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-pystackreg.svg?color=green)](https://python.org)
[![tests](https://github.com/glichtner/napari-pystackreg/workflows/tests/badge.svg)](https://github.com/glichtner/napari-pystackreg/actions)
[![codecov](https://codecov.io/gh/glichtner/napari-pystackreg/branch/main/graph/badge.svg)](https://codecov.io/gh/glichtner/napari-pystackreg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-pystackreg)](https://napari-hub.org/plugins/napari-pystackreg)

Robust image registration for napari.

## Summary
napari-pystackreg offers the image registration capabilities of the python package
[pystackreg](https://github.com/glichtner/pystackreg) for napari.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/napari-pystackreg.gif)

## Description

pyStackReg is used to align (register) one or more images to a common reference image, as is required usually in
time-resolved fluorescence or wide-field microscopy.
It is directly ported from the source code of the ImageJ plugin ``TurboReg`` and provides additionally the
functionality of the ImageJ plugin ``StackReg``, both of which were written by Philippe Thevenaz/EPFL
(available at http://bigwww.epfl.ch/thevenaz/turboreg/).

pyStackReg provides the following five types of distortion:

- Translation
- Rigid body (translation + rotation)
- Scaled rotation (translation + rotation + scaling)
- Affine (translation + rotation + scaling + shearing)
- Bilinear (non-linear transformation; does not preserve straight lines)

pyStackReg supports the full functionality of StackReg plus some additional options, e.g., using different reference
images and having access to the actual transformation matrices (please see the examples below). Note that pyStackReg
uses the high quality (i.e. high accuracy) mode of TurboReg that uses cubic spline interpolation for transformation.

Please note: The bilinear transformation cannot be propagated, as a combination of bilinear transformations does not
generally result in a bilinear transformation. Therefore, stack registration/transform functions won't work with
bilinear transformation when using "previous" image as reference image. You can either use another reference (
"first" or "mean" for first or mean image, respectively), or try to register/transform each image of the stack
separately to its respective previous image (and use the already transformed previous image as reference for the
next image).

## Installation

You can install ``napari-pystackreg`` via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/):

    pip install napari-pystackreg

You can also install ``napari-pystackreg`` via [conda](https://docs.conda.io/en/latest/):

    conda install -c conda-forge napari-pystackreg

Or install it via napari's plugin installer.

    Plugins > Install/Uninstall Plugins... > Filter for "napari-pystackreg" > Install

To install latest development version:

    pip install git+https://github.com/glichtner/napari-pystackreg.git

## Usage


### Open Plugin User Interface

Start up napari, e.g. from the command line:

    napari

Then, load an image stack (e.g. via ``File > Open Image...``) that you want to register. You can also use the example
stack provided by the pluging (``File > Open Sample > napari-pystackreg: PC12 moving example``).
Then, select the ``napari-pystackreg`` plugin from the ``Plugins > napari-pystackreg: pystackreg`` menu.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-initial.png)

### User Interface Options
A variety of options are available to control the registration process:

* `Image Stack`: The image layer that should be registered/transformed.
* `Transformation`: The type of transformation that should be applied.
  - `Translation`: translation
  - `Rigid body`: translation + rotation
  - `Scaled rotation`: translation + rotation + scaling
  - `Affine`: translation + rotation + scaling + shearing
  - `Bilinear`: non-linear transformation; does not preserve straight lines
* `Reference frame:` The reference image for registration.
  - `Previous frame`: Aligns each frame (image) to its previous frame in the stack
  - `Mean (all frames)`: Aligns each frame (image) to the average of all images in the stack
  - `Mean (first n frames)`: Aligns each frame (image) to the mean of the first n frames in the stack. n is a tuneable parameter.
* `Moving-average stack before register`: Apply a moving average to the stack before registration. This can be useful to
  reduce noise in the stack (if the signal-to-noise ratio is very low). The moving average is applied to the stack only
  for determining the transformation matrices, but not for the actual transforming of the stack.
* `Transformation matrix file`: Transformation matrices can be saved to or loaded from a file for permanent storage.

### Reference frame
The reference frame is the frame to which the other frames are aligned. The default option is to use the
`Previous frame`, which will register each frame to its respective previous frame in the stack. Alternatively, the
reference frame can be set to the mean of all frames in the stack (`Mean (all frames)`) or the mean of the first n
frames in the stack (`Mean (first n frames)`). The latter option can be useful if the first frames in the stack are more
stable than the later frames (e.g. if the first frames are taken before the sample is moved). When selecting the
`Mean (first n frames)` option, the number of frames to use for the mean can be set via the spinbox below the option.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-reference-mean-n.png)

### Moving average before registration
To increase registration performance with low signal-to-noise ratio stacks, a moving average can be applied to the
stack before registration. The moving average is applied to the stack only for determining the
transformation matrices, but not for the actual transforming of the stack. That means that the transformed stack will
still contain the original frames (however registered), but not the averaged frames.

When selecting the `Moving-average stack before register` option, the number of frames to use for the moving average can
be set via the spinbox below the option.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-moving-average.png)

### Transformation matrix file
The transformation matrices can be saved to or loaded from a file for permanent storage. This can be useful if you want
to apply the same transformation to another stack (e.g. a different channel of the same sample). The transformation
matrices are saved as a numpy array in a binary file (``.npy``). The file can be loaded via the `Load` button and saved
via the `Save` button.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-register-tmat.png)

### Register/Transform
To perform the actual registration and transformation steps, click the `Register` and `Transform` buttons, respectively.

The `Register` button will register the stack to the reference by determining the appropriate transformation matrices,
without actually transforming the stack. The transformation matrices can be saved to a file via the `Save` button in the
`Transformation matrix file` section.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-registered.png)

The `Transform` button (1) will transform the stack to the reference by applying the transformation matrices that are
currently loaded to the stack selected in `Image Stack`. For the button to become active, either the transformation
matrices have to be loaded from a file via the `Load` button in the `Transformation matrix file` section, or the
`Register` button has to be clicked first to determine the transformation matrices.

The `Transform` button will also add a new image layer to the napari viewer (2) with the transformed stack. The name of the
new layer will be the name of the original stack with the prefix `Registered`.

![](https://github.com/glichtner/napari-pystackreg/raw/main/docs/ui-transformed.png)

Finally, the `Register & Transform` button will perform both the registration and transformation steps in one go.

----------------------------------

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [Apache Software License 2.0] license,
"napari-pystackreg" is free and open source software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## Acknowledgments

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

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

[file an issue]: https://github.com/glichtner/napari-pystackreg/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
