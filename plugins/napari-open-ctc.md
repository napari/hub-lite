
[![PyPI](https://img.shields.io/pypi/v/napari-open-ctc.svg?color=green)](https://pypi.org/project/napari-open-ctc)
[![tests](https://github.com/bentaculum/napari-open-ctc/workflows/tests/badge.svg)](https://github.com/bentaculum/napari-open-ctc/actions)
[![codecov](https://codecov.io/gh/bentaculum/napari-open-ctc/branch/main/graph/badge.svg)](https://codecov.io/gh/bentaculum/napari-open-ctc)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-open-ctc)](https://napari-hub.org/plugins/napari-open-ctc)

Drag and drop annotations/results in the [Cell Tracking Challenge (CTC) format](https://celltrackingchallenge.net) into napari.

Works for `TRA`, `RES`, etc. folders, which contain a time sequence of segmentations in `tiff` format, and a corresponding tracklet file `*.txt`.

https://github.com/bentaculum/napari-open-ctc/assets/8866751/197c9ea2-4115-4829-851a-4b77eb843bf2


## Installation

You can install `napari-open-ctc` via [pip]:

    pip install napari-open-ctc



To install latest development version :


    pip install git+https://github.com/bentaculum/napari-open-ctc.git


## Contributing

Contributions are very welcome. Tests can be run with [tox].

## License

Distributed under the terms of the [BSD-3] license,
`napari-open-ctc` is free and open source software.

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

[file an issue]: https://github.com/bentaculum/napari-open-ctc/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
