
[![License](https://img.shields.io/pypi/l/napari-timeseries-opener-plugin.svg?color=green)](https://github.com/gatoniel/napari-timeseries-opener-plugin/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-timeseries-opener-plugin.svg?color=green)](https://pypi.org/project/napari-timeseries-opener-plugin)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-timeseries-opener-plugin.svg?color=green)](https://python.org)
[![tests](https://github.com/gatoniel/napari-timeseries-opener-plugin/workflows/tests/badge.svg)](https://github.com/gatoniel/napari-timeseries-opener-plugin/actions)
[![codecov](https://codecov.io/gh/gatoniel/napari-timeseries-opener-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/gatoniel/napari-timeseries-opener-plugin)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-timeseries-opener-plugin)](https://napari-hub.org/plugins/napari-timeseries-opener-plugin)

Simple plugin that opens separate .tif files as a 3-dimensional layer.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Run

In powershell run when you do not have sufficient GPU support in your environment
```
$env:CUDA_VISIBLE_DEVICES=-1; napari
```

## Installation

You can install `napari-timeseries-opener-plugin` via [pip]:

    pip install napari-timeseries-opener-plugin



To install latest development version :

    pip install git+https://github.com/gatoniel/napari-timeseries-opener-plugin.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-timeseries-opener-plugin" is free and open source software

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

[file an issue]: https://github.com/gatoniel/napari-timeseries-opener-plugin/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
