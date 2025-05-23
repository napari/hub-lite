
[![License MIT](https://img.shields.io/pypi/l/napari-listener.svg?color=green)](https://github.com/aganders3/napari-listener/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-listener.svg?color=green)](https://pypi.org/project/napari-listener)
[![tests](https://github.com/aganders3/napari-listener/workflows/tests/badge.svg)](https://github.com/aganders3/napari-listener/actions)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-listener)](https://napari-hub.org/plugins/napari-listener)

Opens a socket to listen for commands to control napari from other processes.
This can be useful for controlling napari programmatically from other
applications, or for improving general OS integration (e.g. opening data from a
file or UrL in a running instance of napari).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s
[cookiecutter-napari-plugin] template.

## Installation

You can install `napari-listener` via [pip]:

    pip install napari-listener

## Usage

Once installed, `napari-listener` can be started from the `napari > Plugins >
Start Listening` menu. You will see a new docked widget that displays the
address and port for the listener.

The listener is a TCP server that expects app-model command IDs. It will
execute any valid app-model command, but `napari-listener` registers its own
additional commands for demonstration purposes in
https://github.com/aganders3/napari-listener/blob/main/src/napari_listener/_actions.py.

You can test `napari-listener` using a TCP client such as
[netcat](https://linux.die.net/man/1/nc) or
[curl](https://curl.se/docs/manpage.html) to send an app-model command (and
optional args). For example:

```shell
% nc 127.0.0.1 40256 <<< "napari:open-file /path/to/local/file"
```

<img src="https://raw.githubusercontent.com/aganders3/napari-listener/main/napari-listener-demo.gif" alt="quick demo of napari-listener">

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-listener" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed
description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
