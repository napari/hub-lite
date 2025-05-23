
[![PyPI](https://img.shields.io/pypi/v/napari-ctc-io.svg?color=green)](https://pypi.org/project/napari-ctc-io)
[![tests](https://github.com/bentaculum/napari-ctc-io/workflows/tests/badge.svg)](https://github.com/bentaculum/napari-ctc-io/actions)
[![codecov](https://codecov.io/gh/bentaculum/napari-ctc-io/branch/main/graph/badge.svg)](https://codecov.io/gh/bentaculum/napari-ctc-io)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-ctc-io)](https://napari-hub.org/plugins/napari-ctc-io)

- Drag and drop annotations/results in the [Cell Tracking Challenge (CTC) format](https://celltrackingchallenge.net) into napari.

  Works for `TRA`, `RES`, etc. folders, which contain a time sequence of segmentations in `tiff` format, and a corresponding tracklet file `*.txt`.
- Write tracked cells (`labels` layer & corresponding `tracks` layer) to CTC format (see usage below).


https://github.com/bentaculum/napari-ctc-io/assets/8866751/197c9ea2-4115-4829-851a-4b77eb843bf2


## Installation

You can install `napari-ctc-io` via [pip]:

    pip install napari-ctc-io



To install latest development version :


    pip install git+https://github.com/bentaculum/napari-ctc-io.git

## Usage of writer in widget

```python
def _save(self, event=None):
    pm = npe2.PluginManager.instance()

    outdir = "TRA"
    writer_contrib = pm.get_writer(
        outdir,
        ["labels", "tracks"],
        "napari-ctc-io",
    )[0]

    save_layers(
        path=outdir,
        layers=[
            self._viewer.layers["masks_tracked"],
            self._viewer.layers["tracks"],
        ],
        plugin="napari-ctc-io",
        _writer=writer_contrib,
    )
```


## Contributing

Contributions are very welcome. Tests can be run with [tox].

## License

Distributed under the terms of the [BSD-3] license,
`napari-ctc-io` is free and open source software.

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

[file an issue]: https://github.com/bentaculum/napari-ctc-io/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
