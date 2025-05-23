
[![License BSD-3](https://img.shields.io/pypi/l/napari-simpleannotate.svg?color=green)](https://github.com/hiroalchem/napari-simpleannotate/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-simpleannotate.svg?color=green)](https://pypi.org/project/napari-simpleannotate)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-simpleannotate.svg?color=green)](https://python.org)
[![tests](https://github.com/hiroalchem/napari-simpleannotate/workflows/tests/badge.svg)](https://github.com/hiroalchem/napari-simpleannotate/actions)
[![codecov](https://codecov.io/gh/hiroalchem/napari-simpleannotate/branch/main/graph/badge.svg)](https://codecov.io/gh/hiroalchem/napari-simpleannotate)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-simpleannotate)](https://napari-hub.org/plugins/napari-simpleannotate)

A simple plugin to label image

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

![overview](https://github.com/hiroalchem/napari-simpleannotate/raw/main/images/dog_and_cat.jpg)


## Installation

You can install `napari-simpleannotate` via [pip]:

    pip install napari-simpleannotate



To install latest development version :

    pip install git+https://github.com/hiroalchem/napari-simpleannotate.git


## How to use

1. **Opening Files or Directories**:
   - Click the `Open File` button to open an image file.
   - Click the `Open Directory` button to open a directory containing images.
   - If there's a `class.yaml` in the directory of the selected file or within the selected directory, it will be automatically detected. A popup will appear, giving you the option to load it.

2. **Class Management**:
   - Enter the class name in the textbox and click the `Add class` button to add a class. When adding a class name, a number is automatically assigned to it. This number will be used when saving annotations.
   - Select a class from the class list and click the `Delete selected class` button to remove it.

3. **Annotating Images**:
   - Use napari's rectangle tool to annotate the images. If you have a class selected, the annotation will automatically be assigned to that class.
   - For existing rectangles, you can change their class by selecting the rectangle and then choosing a different class from the list.

4. **Saving Annotations**:
   - Click the `Save Annotations` button to save the annotations in YOLO format.
   - Along with saving the annotations, the `class.yaml` will also be saved. If a `class.yaml` already exists and its content is different from the current one, a popup will appear asking for confirmation to overwrite it.


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-simpleannotate" is free and open source software

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

[file an issue]: https://github.com/hiroalchem/napari-simpleannotate/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
