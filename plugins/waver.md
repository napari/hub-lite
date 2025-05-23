
[![License](https://img.shields.io/pypi/l/waver.svg?color=green)](https://github.com/sofroniewn/waver/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/waver.svg?color=green)](https://pypi.org/project/waver)
[![Python Version](https://img.shields.io/pypi/pyversions/waver.svg?color=green)](https://python.org)
[![tests](https://github.com/sofroniewn/waver/workflows/tests/badge.svg)](https://github.com/sofroniewn/waver/actions)
[![codecov](https://codecov.io/gh/sofroniewn/waver/branch/main/graph/badge.svg?token=QBP7K6YUT7)](https://codecov.io/gh/sofroniewn/waver)

Run simulations of the [wave equation](https://en.wikipedia.org/wiki/Wave_equation) in nD on grids of variable speed in Python. This library owes a lot of its design and approach to the [fdtd](https://github.com/flaport/fdtd) library, a Python 3D electromagnetic FDTD simulator.

This package allows for a fair amount of customization over your wave simulation. You can
 - specify the size and spacing of the grid
 - specify the time step for the simulation, which will be checked to ensure stability of the simulation
 - specify the duration of the simulation
 - setting a variable speed array (one value per grid point) to allow for "objects" in your environment
 - set the source of the wave, which can be a point, line, or any (n-1)D subarray
 - record the wave with a detector, which can be the full grid, the full boundary, or a particular boundary
 - use convenience methods to run many simulations with different sources on the same grid and detector combination

You can use [napari](https://napari.org/), a multi-dimensional image viewer for Python, to allow for easy visualization of the detected wave. Some functionality is also available as a napari plugin to allow for running simulations from a graphical user interface.

Results can look like

https://user-images.githubusercontent.com/6531703/128283012-a784ec06-4df9-4ddf-bf4f-e21b927fe4a3.mov

----------------------------------

## Installation

You can install `waver` via [pip]:

    pip install waver

## Usage

### Convenience Methods

The most convenient way to use waver is to use one of two convenience methods that will create and run a simulation
for you and return the results.

The first method `run_single_source` allows you to run a single simulation with a single source on one grid and 
record the results using a detector. For example

```python
from waver.simulation import run_single_source

single_sim_params = {
    'size': (12.8e-3, 12.8e-3),
    'spacing': 100e-6,
    'duration': 80e-6,
    'min_speed': 343,
    'max_speed': 686,
    'speed': 686,
    'time_step': 50e-9,
    'temporal_downsample': 2,
    'location': (6.4e-3, 6.4e-3),
    'period': 5e-6,
    'ncycles':1,
}

detected_wave, speed_grid = run_single_source(**single_sim_params)
```

The second method `run_multiple_sources` allows you to run multiple simulations with multiple sources on the same
grid and with the same detector and return the results. For example

```python
from waver.simulation import run_multiple_sources

multi_sim_params = {
    'size': (12.8e-3, 12.8e-3),
    'spacing': 100e-6,
    'duration': 80e-6,
    'min_speed': 343,
    'max_speed': 686,
    'speed': 686,
    'time_step': 50e-9,
    'temporal_downsample': 2,
    'sources': [{
        'location': (6.4e-3, 6.4e-3),
        'period': 5e-6,
        'ncycles':1,
    }]
}

detected_wave, speed_grid = run_multiple_sources(**multi_sim_params)
```

The main difference between these two methods is that `run_multiple_sources` takes a `sources` parameter which takes a list 
of dictionaries with keys corresponding to source related keyword arguments found in `run_single_source`.

### Visualization

If you want to quickly visualize the results of `run_multiple_sources`, you can use the `run_and_visualize` command which will 
run the simulation and then launch napari with the results, as seen in [examples/2D/point_source.py](./examples/2D/point_source.py)

```python
from waver.datasets import run_and_visualize

run_and_visualize(**multi_sim_params)
```

### Datasets

If you want to run simulations with on many different speed grids you can use the `generate_simulation_dataset` method as a convenience. The results will be saved to a [zarr](https://zarr.readthedocs.io/en/stable/) file of your chosing. You can then use the `load_simulation_dataset` to load the dataset.

```python
from waver.datasets import generate_simulation_dataset

# Define root path for simulation
path = './simulation_dataset.zarr'
runs = 5

# Define a simulation, 12.8mm, 100um spacing
dataset_sim_params = {
    'size': (12.8e-3, 12.8e-3),
    'spacing': 100e-6,
    'duration': 80e-6,
    'min_speed': 343,
    'max_speed': 686,
    'speed': 'mixed_random_ifft',
    'time_step': 50e-9,
    'sources': [{
        'location': (None, 0),
        'period': 5e-6,
        'ncycles':1,
    }],
    'temporal_downsample': 2,
    'boundary': 1,
    'edge': 1,
}

# Run and save simulation
generate_simulation_dataset(path, runs, **dataset_sim_params)
```

The `generate_simulation_dataset` allows the `speed` to be a string that will specify a particular method of randomly generating speed values for the simulation grid.

### The Simulation Object

If you'd like to understand in a little bit more detail how a simulation is defined then you might want to use the unerlying simulation object `Simulation` and manually set key objects like the `Source` and `Detector`. A full example of this is as follows

```python
# Create a simulation
sim = Simulation(size=size, spacing=spacing, max_speed=max_speed, time_step=time_step)

# Set speed array
sim.set_speed(speed=speed, min_speed=min_speed, max_speed=max_speed)

# Add source
sim.add_source(location=location, period=period, ncycles=ncycles, phase=phase)

# Add detector grid
sim.add_detector(spatial_downsample=spatial_downsample,
                    boundary=boundary, edge=edge)

# Run simulation
sim.run(duration=duration, temporal_downsample=temporal_downsample, progress=progress, leave=leave)

# Print simulation wave and speed data
print('wave: ', sim.detected_wave)
print('speed: ', sim.grid_speed)
```

Note these steps are done inside the `run_single_source` method for you as a convenience.

## Known Limitations

A [perfectly matched layer](https://en.wikipedia.org/wiki/Perfectly_matched_layer) boundary has recently been added, but might not perform well under all conditions. Additional contributions would be welcome here.

Right now the simulations are quite slow. I'd like to add a [JAX](https://github.com/google/jax) backend, but 
havn't done so yet. Contributions would be welcome.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"waver" is free and open source software

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
[file an issue]: https://github.com/sofroniewn/waver/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


