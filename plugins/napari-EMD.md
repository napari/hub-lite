
[![License BSD-3](https://img.shields.io/pypi/l/napari-EMD.svg?color=green)](https://github.com/NickiShaw/napari-EMD/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-EMD.svg?color=green)](https://pypi.org/project/napari-EMD)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-EMD.svg?color=green)](https://python.org)
[![tests](https://github.com/NickiShaw/napari-EMD/workflows/tests/badge.svg)](https://github.com/NickiShaw/napari-EMD/actions)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-EMD)](https://napari-hub.org/plugins/napari-EMD)

A simple plugin to view .emd files in napari (i.e. Velox files). Allows users to track metadata as it changes over the course of a video/stack, developed for analysis of in-situ microscopy data, where users may be changing magnification, focus, etc. during aquisition.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-EMD` via [pip]:

    `pip install napari-EMD`

You can install napari and access the plugin through the GUI. [Reccomended install command for napari](https://napari.org/stable/tutorials/fundamentals/installation.html):

    `python -m pip install "napari[all]"`

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-EMD" is free and open source software

## Issues and Requests

> **Warning: The metadata viewer does not work in the current [Napari bundle](https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-a-bundled-app) version (August 2023). Use the [python package version](https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-python-package-recommended) of Napari for this feature.**

If you encounter any problems or would like any functionality added, please [file an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) along with a detailed description.

Current maintainer(s): [Nicki Shaw](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)

## Preview

Images A and B show different frames in the same image stack, the metadata plugin on the right shows the changing focus value.
![NapariEMD screenshots](Images/napariEMD_screenshots.jpg)

## To Do

- Attatch last-opened information, so the widget does not reset when frames are changed and open toggle options are open remain.
- Add a search bar for navigating metadata.
- Output metadata as file option.
- Add note to change order of open files to replacee active metadata view.
- Make Singleframe note update automatically on change of file order.

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
