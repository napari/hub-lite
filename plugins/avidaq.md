
[![PyPI](https://img.shields.io/pypi/v/avidaq.svg?color=green)](https://pypi.org/project/avidaq)
[![Python Version](https://img.shields.io/pypi/pyversions/avidaq.svg?color=green)](https://python.org)
[![tests](https://github.com/optimax/avidaq/workflows/tests/badge.svg)](https://github.com/optimax/avidaq/actions)
[![codecov](https://codecov.io/gh/optimax/avidaq/branch/main/graph/badge.svg)](https://codecov.io/gh/optimax/avidaq)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/avidaq)](https://napari-hub.org/plugins/avidaq)

controls for napari and micromanger

---

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

### Standard installation

You can install `avidaq` via [pip]:

```shell
pip install napari[all] avidaq
```

### Install from plugin menu

Alternatively you can install `avidaq` via the [napari] plugin menu:

## ![napari-add-plugin](napari-add-plugin.png)

## Running

First start micromanager.  Make sure the server port checkbox is activated.

Then to start napari with the avidaq plugin active run:
`napari -w avidaq`

![](screenshot.png)

## Updating presets

MDA presets are stored in a json file in the user's home directory.

```shell

`C:\\Users\YourName\.avidaq\mda_presets.json`
```

This file should exist after plugin installation with some defaults. You do not need to create the file yourself.

Add or modify the values and reload napari to see the changes.

All parameter entries are optional, if not provided the default value will be used.

The parameter names and their descriptions can be found [here] (https://github.com/micro-manager/pycro-manager/blob/main/pycromanager/acq_util.py#L102-L115)

The format is as follows:

```json
{
    "gui_display_name": {
        "parameter_name": value,
        "parameter_name": value,
        ...
    },
    "gui_display_name": {
        "parameter_name": value,
        "parameter_name": value,
        ...
    },
    ...
}
```

defaults:

```json
{
  "Basic": {
    "num_time_points": 5,
    "z_start": 0,
    "z_end": 6,
    "z_step": 0.4
  },
  "Simple": {
    "num_time_points": 2,
    "z_start": 0,
    "z_end": 2,
    "z_step": 0.1
  },
  "Detailed": {
    "num_time_points": 10,
    "z_start": 0,
    "z_end": 12,
    "z_step": 0.2
  }
}
```

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## Development

You should have python3.8 or higher installed.

1. clone this repo
2. create a virtual environment `python -m venv .venv && source .venv/bin/activate`
3. run `pip install -e '.[testing,build]'`
4. run `pre-commit install`

### To run unit tests

`pytest`

### typical workflow

1. edit code in `/src`
2. run napari -w avidaq
3. repeat

### Releasing to pypi


Project is automically built and deployed to pypi upon


---

[napari]: https://github.com/napari/napari
[cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[mit]: http://opensource.org/licenses/MIT
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache software license 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[mozilla public license 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[pypi]: https://pypi.org/
