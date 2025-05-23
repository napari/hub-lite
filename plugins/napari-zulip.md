
[![License BSD-3](https://img.shields.io/pypi/l/napari-zulip.svg?color=green)](https://github.com/kephale/napari-zulip/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-zulip.svg?color=green)](https://pypi.org/project/napari-zulip)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-zulip.svg?color=green)](https://python.org)
[![tests](https://github.com/kephale/napari-zulip/workflows/tests/badge.svg)](https://github.com/kephale/napari-zulip/actions)
[![codecov](https://codecov.io/gh/kephale/napari-zulip/branch/main/graph/badge.svg)](https://codecov.io/gh/kephale/napari-zulip)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-zulip)](https://napari-hub.org/plugins/napari-zulip)

A simple plugin for interacting with Zulip from napari.

![An example screenshot of napari-zulip in action. It shows the plugin napari-boids and a filtered noise image, as well as a docked version of the napari-zulip plugin](./resources/demo_screenshot.png)  

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-zulip` via [pip]:

    pip install napari-zulip



To install latest development version :

    pip install git+https://github.com/kephale/napari-zulip.git

### Setting it up

The plugin is going to look for a file in `<home directory>/.zulip.d/napari.zulipchat.com.zuliprc`.

**If you want to use this on a different zulip then adjust the `napari.zulipchat.com` to whatever the correct domain should be.**

#### How to generate a `.zuliprc` file

In the Zulip app:
- Select `Menu`
- Select `Personal settings`
- Select `Account & privacy`
- Click on `Show/change your API key`
- Enter your password
- Click `Download .zuliprc` 
- Save the file as `<home directory>/.zulip.d/napari.zulipchat.com.zuliprc` (or change the domain name if using a different Zulip server)

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-zulip" is free and open source software

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

[file an issue]: https://github.com/kephale/napari-zulip/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
