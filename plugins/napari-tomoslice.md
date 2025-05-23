
[![License](https://img.shields.io/pypi/l/napari-tomoslice.svg?color=green)](https://github.com/alisterburt/napari-tomoslice/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tomoslice.svg?color=green)](https://pypi.org/project/napari-tomoslice)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tomoslice.svg?color=green)](https://python.org)
[![tests](https://github.com/alisterburt/napari-tomoslice/workflows/tests/badge.svg)](https://github.com/alisterburt/napari-tomoslice/actions)
[![codecov](https://codecov.io/gh/alisterburt/napari-tomoslice/branch/master/graph/badge.svg)](https://codecov.io/gh/alisterburt/napari-tomoslice)

A napari plugin for visualising and interacting with electron cryotomograms.


## Installation

You can install `napari-tomoslice` via [pip]:

    pip install napari-tomoslice

## Usage

This plugin provides a user interface for opening electron cryotomograms in 
napari as both volumes and slices through volumes.

![demo](https://user-images.githubusercontent.com/7307488/138575305-b05c4735-9c03-4629-bfb0-9612ea8f26fd.gif)

The plugin can be opened from the `plugins` menu in napari, or with 
`napari-tomoslice` at the command line.

![plugins-menu](https://user-images.githubusercontent.com/7307488/138575015-00ea78d9-02c1-44bc-9034-0c0a7fa8d973.png)

```yaml
Usage: napari-tomoslice [TOMOGRAM_FILE]

  An interactive tomogram slice viewer in napari.

  Controls: 
  x/y/z - align normal vector along x/y/z axis 
  click and drag - shift plane along its normal vector
  alt-click - add point on plane (if points layer is active)
  o - align plane normal to view direction
  [] - decrease/increase plane thickness

Arguments:
  [TOMOGRAM_FILE]

Options:
  --help                          Show this message and exit.

```

## Contributing

Contributions are very welcome. 

## License

Distributed under the terms of the [BSD-3] license,
"napari-tomoslice" is free and open source software

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

[file an issue]: https://github.com/alisterburt/napari-tomoslice/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


