
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/napari-live-flim.svg?color=green)](https://github.com/uw-loci/napari-live-flim/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-live-flim.svg?color=green)](https://pypi.org/project/napari-live-flim)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-live-flim.svg?color=green)](https://python.org)
[![tests](https://github.com/uw-loci/napari-live-flim/workflows/tests/badge.svg)](https://github.com/uw-loci/napari-live-flim/actions)
[![codecov](https://codecov.io/gh/uw-loci/napari-live-flim/branch/main/graph/badge.svg)](https://codecov.io/gh/uw-loci/napari-live-flim)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-live-flim)](https://napari-hub.org/plugins/napari-live-flim)

A plugin for real-time FLIM analysis

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Required dependencies

- [OpenScan] TCSPC module and all dependencies.
    - Verify FLIM electronics are compatible with OpenScan
- Python and the [napari] package and all dependencies

You can install `napari` via [pip]:

    pip install napari[all]

## Installation

You can install `napari-live-flim` via [pip]:

    pip install napari-live-flim

## Usage

1. In MicroManager, set a port number in the device property setting named `OpenScanFLIM-BH-TCSPC-SendFLIMHistogramsToUDPPort`
2. In Napari, select **Plugins > FLIM Viewer (napari-live-flim)** to run the plugin. Enter the same port number to connect to OpenScan.
3. Begin acquisition within MicroManager.
4. Interact with the FLIM data in real-time within napari.
    - Modify the FLIM Parameters and Display Filters settings as desired.
    - Add selections to the Lifetime Image or Phasor Plot by clicking the relevant New Selection buttons.
    - Manipulate the selections with the mouse cursor and modify the selection layer with the layer controls.
    - Click the Snapshot button during acquisition to take a snapshot.
    - Use the scroll bar under the Lifetime Image to recall a specific snapshot.
5. Stop scanning within MicroManager to end acquisition.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-live-flim" is free and open source software

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
[file an issue]: https://github.com/uw-loci/napari-live-flim/issues
[OpenScan]: https://github.com/openscan-lsm/OpenScan

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
