
[![License BSD-3](https://img.shields.io/pypi/l/napari-cursor-tracker.svg?color=green)](https://github.com/faymanns/napari-cursor-tracker/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-cursor-tracker.svg?color=green)](https://pypi.org/project/napari-cursor-tracker)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-cursor-tracker.svg?color=green)](https://python.org)
[![tests](https://github.com/faymanns/napari-cursor-tracker/workflows/tests/badge.svg)](https://github.com/faymanns/napari-cursor-tracker/actions)
[![codecov](https://codecov.io/gh/faymanns/napari-cursor-tracker/branch/main/graph/badge.svg)](https://codecov.io/gh/faymanns/napari-cursor-tracker)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-cursor-tracker)](https://napari-hub.org/plugins/napari-cursor-tracker)

Plugin for easy manual annotation/tracking of 3D or 2D + t dataset by following the cursor.

----------------------------------

<!--
This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-cursor-tracker` via [pip]:

    pip install napari-cursor-tracker

## Getting Started with napari-cursor-tracker

Welcome to `napari-cursor-tracker`, a tool that simplifies the annotation of points in stacks of images by tracking your cursor's position. This documentation will guide you through the process of setting up and using this plugin effectively.

### Points Layer Setup

Before you can start tracking, you need to create a points layer, which will store the positions of your cursor for each image in the stack. Here's how to set it up:

1. **Choose a Reference Image:** Start by selecting a "Reference image" from your image stack. The number of frames or slices in the reference image determines how many points your new layer will have (one per frame/slice).

2. **Specify Point Name:** Assign a name to the tracked point. This name will also serve as the name for the new layer. This step is particularly useful when tracking multiple points.

3. **Create the Layer:** Click on "Add new layer" to create the points layer. Initially, all points will be located at the origin (0, 0, 0), but their positions will be updated as you start tracking.

### Tracking Your Cursor

Now that you have set up the points layer, you can start tracking your cursor's position. Follow these steps:

1. **Select the Active Layer:** Choose the points layer where you want to save the tracking results as the "Active layer."

2. **Initiate Tracking:** Begin tracking your cursor's position by pressing the 't' key on your keyboard. To stop tracking, press 't' again. If the "Auto play when tracking is started" option is enabled, playback will start automatically when you press 't'. Alternatively, you can manually scroll through the images, and your cursor's position will be saved whenever the slice/frame index changes.

3. **Customize Playback:** To facilitate or expedite tracking, you can adjust playback parameters as needed.

### Tracking Multiple Points

If you need to track multiple points of interest, you can follow these steps:

1. **Create Individual Layers:** Create a separate points layer for each point you want to track.

2. **Select Active Layer:** Use the "Active layer" dropdown menu to select the specific points layer you want to work with.

3. **Start Tracking:** Begin tracking the selected point following the previously mentioned tracking process.

### Saving Your Results

The results from your tracking sessions can be saved as CSV files. Any points that were not tracked will be marked at the origin point (0, 0, 0) in the saved file.

With these guidelines, you should be well-prepared to efficiently annotate points in your image stacks using `napari-cursor-tracker`. Happy tracking!


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-cursor-tracker" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
