
[![License BSD-3](https://img.shields.io/pypi/l/biaplotter.svg?color=green)](https://github.com/BiAPoL/biaplotter/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/biaplotter.svg?color=green)](https://pypi.org/project/biaplotter)
[![Python Version](https://img.shields.io/pypi/pyversions/biaplotter.svg?color=green)](https://python.org)
[![tests](https://github.com/BiAPoL/biaplotter/workflows/tests/badge.svg)](https://github.com/BiAPoL/biaplotter/actions)
[![codecov](https://codecov.io/gh/BiAPoL/biaplotter/branch/main/graph/badge.svg)](https://codecov.io/gh/BiAPoL/biaplotter)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/biaplotter)](https://napari-hub.org/plugins/biaplotter)

A base napari plotter widget for interactive plotting

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Documentation

The full documentation with API and examples can be found [here](https://biapol.github.io/biaplotter/).

## Installation

* Make sure you have Python in your computer, e.g. download [miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#download).

* Create a new environment, for example, like this:

```
mamba create --name biaplotter-env python=3.9
```

If you never used mamba/conda environments before, take a look at [this blog post](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html).

* **Activate** the new environment with `mamba`:

```
mamba activate biaplotter-env
```

* Install [napari](https://napari.org/stable/), e.g. via `mamba`:

```
mamba install -c conda-forge napari pyqt
```

Afterwards, install `biaplotter` via `pip`:

```
pip install biaplotter
```

To install latest development version :

```
pip install git+https://github.com/BiAPoL/biaplotter.git
```


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"biaplotter" is free and open source software

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

[file an issue]: https://github.com/BiAPoL/biaplotter/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
