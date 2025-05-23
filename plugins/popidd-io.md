
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/popidd-io.svg?color=green)](https://github.com/IntegratedPathologyUnit-ICR/popidd-io/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/popidd-io.svg?color=green)](https://pypi.org/project/popidd-io)
[![Python Version](https://img.shields.io/pypi/pyversions/popidd-io.svg?color=green)](https://python.org)
[![tests](https://github.com/IntegratedPathologyUnit-ICR/popidd-io/workflows/tests/badge.svg)](https://github.com/IntegratedPathologyUnit-ICR/popidd-io/actions)
[![codecov](https://codecov.io/gh/IntegratedPathologyUnit-ICR/popidd-io/branch/main/graph/badge.svg)](https://codecov.io/gh/IntegratedPathologyUnit-ICR/popidd-io)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/popidd-io)](https://napari-hub.org/plugins/popidd-io)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14185575.svg)](https://doi.org/10.5281/zenodo.14185575)



A simple plugin to read digital pathology images and annotations.
Made by Ferran Cardoso at the Integrated Pathology Unit (ICR/RMH).

This is still an experimental and in-development project,
so expect considerable additions and changes to existing methods.
Documentation and tests will be added in the coming weeks.

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation


Setup conda environment

    mamba create -n popidd_io python pip pyqt

Activate conda environment

    mamba activate popidd_io

### End users

You can install `popidd-io` via [pip]:

    pip install popidd-io

### Development

Install test version from project base directory

    pip install -e ".[testing]"

Run dev environment with

    python developing.py

Before contributing, please install and use pre-commit hooks:

    pip install pre-commit
    pre-commit install

## Description

This plugin brings support for brightfield and fluorescence images to Napari,
as well as adding support for polygonal annotations in geoJSON files saved by QuPath.

Brightfield images are loaded as a single layer, incorporating also resolution
information if found on the metadata.
Fluorescence images are separated into channels annotated using the information
present in the image metadata.
Support for this latter modality is still ongoing and will improve in the coming weeks.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Made by Ferran Cardoso Rodriguez with the help of colleagues at the Integrated Pathology Unit.

Distributed under the terms of the [GNU GPL v3.0] license,
"popidd-io" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
