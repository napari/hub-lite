
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI](https://img.shields.io/pypi/v/napari-quoll.svg?color=green)](https://pypi.org/project/napari-quoll)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-quoll.svg?color=green)](https://python.org)
[![tests](https://github.com/rosalindfranklininstitute/napari-quoll/workflows/tests/badge.svg)](https://github.com/rosalindfranklininstitute/napari-quoll/actions)
[![codecov](https://codecov.io/gh/rosalindfranklininstitute/napari-quoll/branch/main/graph/badge.svg)](https://codecov.io/gh/rosalindfranklininstitute/napari-quoll)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-quoll)](https://napari-hub.org/plugins/napari-quoll)

Resolution estimation for electron tomography

The Python package which does the resolution estimation is [Quoll](https://github.com/rosalindfranklininstitute/quoll). This repository, `napari-quoll` is just the Napari plugin.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-quoll` via [pip] into a <b>Python 3.7</b> environment, replacing <env_name> with an environment name of your choice:

    conda -n create <env_name> python=3.7
    conda activate <env_name>
    pip install napari-quoll



To install latest development version :

    pip install git+https://github.com/rosalindfranklininstitute/napari-quoll.git

<b>Note:</b> Due to [miplib]() dependencies, this plugin only works on Python 3.7 environments.


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [Apache Software License 2.0] license,
"napari-quoll" is free and open source software

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

[file an issue]: https://github.com/rosalindfranklininstitute/napari-quoll/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
