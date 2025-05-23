
[![License BSD-3](https://img.shields.io/pypi/l/napari-blossom.svg?color=green)](https://github.com/hereariim/napari-blossom/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-blossom.svg?color=green)](https://pypi.org/project/napari-blossom)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-blossom.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/napari-blossom/workflows/tests/badge.svg)](https://github.com/hereariim/napari-blossom/actions)
[![codecov](https://codecov.io/gh/hereariim/napari-blossom/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/napari-blossom)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-blossom)](https://napari-hub.org/plugins/napari-blossom)

Segmentation of blossom apple tree images

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

This plugin was written by Herearii Metuarea, student intern at LARIS (French laboratory located in Angers, France) in Imhorphen, french scientific team lead by David Rousseau (Full professor). This plugin was designed as part of the european project INVITE.

<img width="86" alt="Logo-IRHS-h_2022_png_large" src="https://github.com/hereariim/napari-blossom/assets/93375163/750bbd60-ef3e-4148-9cbd-8a32e11252a4"> ![Logo-INRAE](https://github.com/hereariim/napari-blossom/assets/93375163/d7cc95a1-f09c-4430-8ac8-8962c1046767) ![logo2](https://github.com/hereariim/napari-blossom/assets/93375163/3b41c838-acc8-49a3-81f8-46d1305f43d3) ![logolaris1](https://github.com/hereariim/napari-blossom/assets/93375163/bf92a903-5810-4c43-aa28-573f96f64ff9) ![logo1](https://github.com/hereariim/napari-blossom/assets/93375163/f9361560-dd4f-49f4-955d-ffe41b5c014d)

## Installation

You can install `napari-blossom` via [pip]:

    pip install napari-blossom

To install latest development version :

    pip install git+https://github.com/hereariim/napari-blossom.git

## How does it works

This module offers a plugin that allows you to segment the images of the apple tree flowers. As input, you can enter a **single image** with the image selection widget. Once the image is entered in the napari window, you can segment the apple blossoms with the image segmentation widget by running the run button. The segmented image will appear in the napari window.

![Capture d'écran 2024-04-24 120758](https://github.com/hereariim/napari-blossom/assets/93375163/4f0c6ac7-b3a8-4849-9c5c-0ff5f35c8362)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-blossom" is free and open source software

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

[file an issue]: https://github.com/hereariim/napari-blossom/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
