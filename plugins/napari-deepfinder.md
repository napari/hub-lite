
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/napari-deepfinder.svg?color=green)](https://github.com/deep-finder/napari-deepfinder/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-deepfinder.svg?color=green)](https://pypi.org/project/napari-deepfinder)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-deepfinder.svg?color=green)](https://python.org)
[![tests](https://github.com/deep-finder/napari-deepfinder/workflows/tests/badge.svg)](https://github.com/deep-finder/napari-deepfinder/actions)
[![codecov](https://codecov.io/gh/deep-finder/napari-deepfinder/branch/main/graph/badge.svg)](https://codecov.io/gh/deep-finder/napari-deepfinder)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-deepfinder)](https://napari-hub.org/plugins/napari-deepfinder)

A napari plugin for the DeepFinder library which includes display, annotation, target generation, segmentation and clustering functionalities.
An orthoslice view has been added for an easier visualisation and annotation process.

**The documentation for users is available [here](https://deep-finder.github.io/napari-deepfinder/).**

> [!WARNING]
>
> An upstream bug in `napari` versions **≥ 0.5.0** causes the menu bar to break when closing the *Orthoslice view*.
> 
> See this issue for more details: https://github.com/napari/napari/issues/7588.
> 
> As a temporary workaround, you can use [napari v0.4.19](https://github.com/napari/napari/releases/tag/v0.4.19), which is not affected by this bug.


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `napari-deepfinder` via [pip]:

    pip install napari-deepfinder



To install latest development version :

    pip install git+https://github.com/deep-finder/napari-deepfinder.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-deepfinder" is free and open source software

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

[file an issue]: https://github.com/deep-finder/napari-deepfinder/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
