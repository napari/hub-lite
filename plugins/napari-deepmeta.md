
[![License MIT](https://img.shields.io/pypi/l/napari-deepmeta.svg?color=green)](https://github.com/EdgarLefevre/napari-deepmeta/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-deepmeta.svg?color=green)](https://pypi.org/project/napari-deepmeta)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-deepmeta.svg?color=green)](https://python.org)
[![tests](https://github.com/EdgarLefevre/napari-deepmeta/workflows/tests/badge.svg)](https://github.com/EdgarLefevre/napari-deepmeta/actions)
[![codecov](https://codecov.io/gh/EdgarLefevre/napari-deepmeta/branch/main/graph/badge.svg)](https://codecov.io/gh/EdgarLefevre/napari-deepmeta)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-deepmeta)](https://napari-hub.org/plugins/napari-deepmeta)

Mice lungs and metastases segmentation tool.
This tool is a demo tool for DeepMeta network.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `napari-deepmeta` via [pip]:

    pip install napari-deepmeta



To install latest development version :

    pip install git+https://github.com/EdgarLefevre/napari-deepmeta.git


## Usage

This plugin is designed to process your mouse MRI images with our dataset. It comes with a demo, including one of our
test images.

By opening the deepmeta demo plugin, you will see an interface with one unique button, by clicking on it, it will load an image,
run prediction and then draw the masks contours on each slice.

If you open the deepmeta plugin, you will see an interface with one button and 3 checkboxes.
By checking the checkboxes, you add steps to the pipeline (enhance contrast, do postprocessing, segment metastases).
Once everything is setup, just click on the button and wait (the waiting time depends on your computer performance.)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-deepmeta" is free and open source software

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

[file an issue]: https://github.com/EdgarLefevre/napari-deepmeta/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
