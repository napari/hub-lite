
[![License GNU GPL v3.0](https://img.shields.io/pypi/l/napari-tracing.svg?color=green)](https://github.com/mapmanager/napari-tracing/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tracing.svg?color=green)](https://pypi.org/project/napari-tracing)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tracing.svg?color=green)](https://python.org)
<!-- [![tests](https://github.com/mapmanager/napari-tracing/workflows/tests/badge.svg)](https://github.com/mapmanager/napari-tracing/actions) -->
<!-- [![codecov](https://codecov.io/gh/mapmanager/napari-tracing/branch/main/graph/badge.svg)](https://codecov.io/gh/mapmanager/napari-tracing) -->
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-tracing)](https://napari-hub.org/plugins/napari-tracing)

## Napari Tracer Plugin

The `Napari Tracer Plugin` provides an intuitive interface for users to load images, perform brightest path tracing, and visualize the results. This plugin, which is built on top of the Napari viewer, enables users to explore and annotate complex images, and take advantage of the viewer's built-in features such as zooming, panning, and adjusting contrast while viewing their tracings. The `Napari Tracer Plugin` uses the brightest path tracing algorithms from [brightest-path-lib](https://github.com/mapmanager/brightest-path-lib) to provide an interactive path building process for users to create traced segments in 2D and 3D images.

## Examples

<video loop muted autoplay controls >
  <source src="sample-2d-tracing.mp4" type="video/mp4">
</video>

You can download our [2D](data/sample-2d.tif) and [3D](sample-3d.tif) example tif files.

## Features

1. Load images and trace paths in 2D and 3D.
1. Offloads computations to a background thread to ensure a responsive user interface.
1. Two tracing modes: disjoint and continuous. Disjoint segments refer to paths that do not share any points, while continuous segments start from the endpoint of a previously traced path.
1. Verify traced segments and cancel tracing if necessary.
1. Save traced paths in SWC format commonly used in biology to represent neuronal morphology.
1. Load previously saved tracings in SWC format.

## Installation

You can install `napari-tracing` via pip:

    pip install napari-tracing

To install latest development version :

    pip install git+https://github.com/mapmanager/napari-tracing.git

## Usage

Once installed, the Napari Tracer Plugin can be accessed from the Napari menu under "Plugins" > "napari tracing: Tracer Widget". This will open the plugin interface, where you can load your image and start tracing.

## Tracing

1. To trace a path, select the "Trace" mode and the image layer that you want to trace from their respective dropdowns.
2. Once you select the image, a points layer called the terminal points layer will be created on the Napari viewer where you can add the start and end point.
3. Click the "Start Tracing" button to perform brightest path tracing between the points.
4. The traced path will appear in a new points layer called the tracing result result layer in the Napari viewer as a line overlay.
5. Each new traced segment is verified, so you can either accept the tracing or reject it. If you choose to reject the tracing, you can try again with a different set of points if necessary.
6. You can click on the "Cancel Tracing" button to cancel a tracing that is in progress.

## Saving and loading tracings

1. To save a tracing, click on the "Save Trace" button from the plugin menu. This will save the traced path in SWC format to a file of your choosing.
1. To load a previously saved tracing, click on the "Load Trace" button and choose the SWC file you want to load. The traced path will appear in the Napari viewer.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [GNU GPL v3.0] license,
"napari-tracing" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[file an issue]: https://github.com/mapmanager/napari-tracing/issues
