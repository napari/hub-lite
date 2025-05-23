
[![License BSD-3](https://img.shields.io/pypi/l/napari-pixel-correction.svg?color=green)](https://github.com/hereariim/napari-pixel-correction/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-pixel-correction.svg?color=green)](https://pypi.org/project/napari-pixel-correction)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-pixel-correction.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/napari-pixel-correction/workflows/tests/badge.svg)](https://github.com/hereariim/napari-pixel-correction/actions)
[![codecov](https://codecov.io/gh/hereariim/napari-pixel-correction/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/napari-pixel-correction)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-pixel-correction)](https://napari-hub.org/plugins/napari-pixel-correction)

Plugin to correct manually pixel wrongly predicted on image by annotation

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

This plugin allows you to manually correct the images of the apple tree flowers by annotation. Below, a piece of an image shows the predicted pixels (in brown). A pixel in brown is assigned to the flower class. We can see that the brown colour does not necessarily cover a flower in this image.

![Capture d’écran 2022-09-21 152404](https://user-images.githubusercontent.com/93375163/191530483-5ce230af-e34c-4fd5-ab91-1d611fd774d1.png)

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-pixel-correction` via [pip]:

    pip install napari-pixel-correction



To install latest development version :

    pip install git+https://github.com/hereariim/napari-pixel-correction.git

## How does it work

First, you need a compressed file (in .zip format) were you have all your images. For a compressed file named as `input.zip`, the compressed file should be built like :

```
.
└── input.zip
    └── repository
        ├── image
        │   ├── im_1.JPG
        │   ├── im_2.JPG  
        │   ├── im_3.JPG
        │   ...
        │   └── im_n.JPG
        │
        └── mask
            ├── im_1_mask.JPG
            ├── im_2_mask.JPG
            ├── im_3_mask.JPG
            ...
            └── im_n_mask.JPG
```
In repository, each image folder should have two elements : image in RGB and the segmented mask in binary image (where no-flower class is 0 and flower class is 255)

![napari-tutorial_simple](https://user-images.githubusercontent.com/93375163/191527225-47ba8667-e3bd-467b-b5f3-f8f7d97617a5.gif)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-pixel-correction" is free and open source software

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

[file an issue]: https://github.com/hereariim/napari-pixel-correction/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
