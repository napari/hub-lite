
[![codecov](https://codecov.io/gh/midi-app-controller/midi-app-controller/graph/badge.svg?token=YALMD0PQ80)](https://codecov.io/gh/midi-app-controller/midi-app-controller)
[![Documentation Status](https://readthedocs.org/projects/midi-app-controller/badge/?version=latest)](https://midi-app-controller.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/midi-app-controller.svg)](https://badge.fury.io/py/midi-app-controller)

midi-app-controller is an app, that allows user to control all applications using 'pyapp-kit/app-model' with a USB MIDI controller.

## Documentation

Documentation at https://midi-app-controller.readthedocs.io/en/latest/.

## Usage (napari)

MIDI App Controller is a package designed to integrate MIDI controllers with Python Qt apps using app-model. As of now, it is used most commonly with [napari](https://napari.org), a viewer for multi-dimensional images. We will show how to use MIDI App Controller with napari but getting started with other applications should look very similar.

### Installation

To install MIDI App Controller in your environment (where Python and napari are already installed), use this command:

```
pip install midi-app-controller
```

napari will automatically detect the package and install the plugin next time it starts.

To install the newest development version, clone the GitHub repo and [install it as a local package](#installing).

### Setup

Launch the plugin from the _Plugins_ menu.

![](docs/img/plugins-menu.png)

A panel will open to the side.

![](docs/img/midi-status.png)

#### Controller

If your MIDI controller is supported out of the box, you can simply select the appropriate model. If not, you will need to tell MIDI App Controller how to interact with this model of controller by creating a [controller schema](controllers.md).

Once you have selected the controller schema, you can select binds schema.

#### MIDI ports

If they haven't been selected automatically, select MIDI input and output ports that correspond to your physical controller.

### Start handling

After a controller and bindings are selected, you can click "Start handling". This will start a thread that listens to all input from the controller and invokes appropriate commands. You can close the panel with the settings, the thread will work in the background until you click "Stop handling".

### Edit binds

Click "Edit binds" to open dialog where you can configure bindings by choosing which physical buttons and knobs on your controller correspond to which commands in the application. Think of it like configuring keyboard shortcuts.

![](docs/img/edit-binds.png)

All configurations are simple YAML files which you can copy, share, or edit manually. You can click "Reveal in explorer" to see the exact location of the currently chosen config file. You shouldn't edit built-in presets stored in the package directory; when you edit a built-in preset in the graphical user interface, a copy will automatically be created.

After you save changes, if you have already started handling, you need to click "Restart handling" to start a new server with the changes applied.

## Usage without GUI

The library can be also controlled using the singleton of [`StateManager`](api_reference.md) class:
```python
from midi_app_controller.state.state_manager import get_state_manager

state = get_state_manager()
# Now the library can be controlled using `state`.
```

## Development

### Installing
```sh
python3 -m pip install -e .
```

### Testing
```sh
python3 -m pip install -e .[testing]
python3 -m pytest --cov .
```

### Testing docs
```sh
mkdocs serve -a localhost:8080
```

### Using pre-commit
```sh
python3 -m pip install -e .[dev]
pre-commit install
```
