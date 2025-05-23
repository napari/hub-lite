
[![License](https://img.shields.io/pypi/l/napari-update-checker.svg?color=green)](https://github.com/napari/update-checker/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-update-checker.svg?color=green)](https://pypi.org/project/napari-update-checker)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-update-checker.svg?color=green)](https://python.org)
[![tests](https://github.com/napari/update-checker/actions/workflows/test_and_deploy.yml/badge.svg)](https://github.com/napari/update-checker/actions/workflows/test_and_deploy.yml)
[![codecov](https://codecov.io/gh/napari/update-checker/branch/main/graph/badge.svg)](https://codecov.io/gh/napari/update-checker)

[napari] update checker to query for new napari versions.

You can read the documentation at [napari.org/update-checker](https://napari.org/update-checker).

## Overview

The `napari-update-checker` is a plugin that checks for newer versions of napari available either on [conda-forge], or on [PyPI], by querying the repository release tags.

![Screenshot of the napari-update-checker interface, showcasing the plugin](https://raw.githubusercontent.com/napari/update-checker/refs/heads/main/images/description.png)

`napari-update-checker` knows how to detect if napari was installed using `conda` or `pip` or if it was installed using the application bundle to provide the correct documentation on how to update napari to the latest version.

## Widget

![Screenshot of the napari-update-checker widget](https://raw.githubusercontent.com/napari/update-checker/refs/heads/main/images/widget.png)

## License

Distributed under the terms of the [BSD-3] license, "napari-update-checker" is free and open source
software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[file an issue]: https://github.com/napari/update-checker/issues
[conda-forge]: https://anaconda.org/conda-forge/napari
[PyPI]: https://pypi.org/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[napari]: https://github.com/napari/napari
