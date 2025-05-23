
[![License BSD-3](https://img.shields.io/pypi/l/tootapari.svg?color=green)](https://github.com/kephale/tootapari/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/tootapari.svg?color=green)](https://pypi.org/project/tootapari)
[![Python Version](https://img.shields.io/pypi/pyversions/tootapari.svg?color=green)](https://python.org)
[![tests](https://github.com/kephale/tootapari/workflows/tests/badge.svg)](https://github.com/kephale/tootapari/actions)
[![codecov](https://codecov.io/gh/kephale/tootapari/branch/main/graph/badge.svg)](https://codecov.io/gh/kephale/tootapari)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/tootapari)](https://napari-hub.org/plugins/tootapari)

A plugin to send Mastodon toots from napari

----------------------------------

## Installation

You can install `tootapari` via [pip]:

    pip install tootapari



To install latest development version :

    pip install git+https://github.com/kephale/tootapari.git


## Setup

1. Setup your `.env` file in your XDG config directory. On MacOS this is `/Users/<username>/Library/Application\ Support/tootapari/`

It should include:

```
MASTODON_INSTANCE_URL="https://mastodon.social"
MASTODON_ACCESS_TOKEN="<your access token>"
```

2. You can generate your access token by following these instructions: https://learn.adafruit.com/intro-to-mastodon-api-circuitpython/generate-your-mastodon-token

TODO: someone should port these instructions to this readme.

3. Start tooting!

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"tootapari" is free and open source software

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

[file an issue]: https://github.com/kephale/tootapari/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
