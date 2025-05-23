
[![License](https://img.shields.io/pypi/l/workshop-demo.svg?color=green)](https://github.com/DragaDoncila/workshop-demo/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/workshop-demo.svg?color=green)](https://pypi.org/project/workshop-demo)
[![Python Version](https://img.shields.io/pypi/pyversions/workshop-demo.svg?color=green)](https://python.org)
[![tests](https://github.com/DragaDoncila/workshop-demo/workflows/tests/badge.svg)](https://github.com/DragaDoncila/workshop-demo/actions)
[![codecov](https://codecov.io/gh/DragaDoncila/workshop-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/DragaDoncila/workshop-demo)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/workshop-demo)](https://napari-hub.org/plugins/workshop-demo)

A demo napari plugin incorporating reader, writer and dock widget contributions using the new npe2 plugin architecture.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `workshop-demo` via [pip]:

    pip install workshop-demo


To install latest development version :

    pip install git+https://github.com/DragaDoncila/workshop-demo.git

## What is this?

This plugin was created to serve as a semi-meaningful example of a plugin using
the new napari [npe2](https://pypi.org/project/npe2/) architecture.

It provides a reader, a writer and two dock widgets to support opening, processing
and writing out [cell tracking challenge](https://celltrackingchallenge.net/) data.

We've provided comments and example tests that can be used as a reference
when building your own plugin.

## Using this plugin

### Sample Data
You can download sample data for this plugin from the tracking challenge website. Any 2D+T
sequence should work, but this plugin has been tested only with the 
[Human hepatocarcinoma-derived cells expressing the fusion protein YFP-TIA-1](http://data.celltrackingchallenge.net/training-datasets/Fluo-C2DL-Huh7.zip) 
dataset.
### Reading Data
This plugin's reader is designed for tracking challenge segmentation gold standard ground truth
data conforming to the file format described in the [data specification](https://public.celltrackingchallenge.net/documents/Naming%20and%20file%20content%20conventions.pdf).

Ground truth data is only provided for a subset of the frames of the entire sequence. This
reader will attempt to find the number of frames of the associated sequence in a sister
directory of the ground truth data directory and open a labels layer with the same number
of frames, thus ensuring the labelled data is correctly overlaid onto the original sequence.



https://user-images.githubusercontent.com/17995243/146114062-36124c05-f44a-488e-8991-f39a702c917f.mov



### Segmenting Data
One of the dock widgets provided by this plugin is "Segment by Threshold". The widget
allows you to select a 2D+T image layer in the viewer (e.g. any of the sequences in the Human 
hepatocarcinoma dataset above) and segment it using a selection of scikit-image thresholding functions.

The segmentation is then returned as a `Labels` layer into the viewer.


https://user-images.githubusercontent.com/17995243/146114088-f6fb645e-8d78-4880-827b-2f0334dad859.mov



### Highlighting Segmentation Differences
The second dock widget provided by this plugin allows you to visually compare your segmentation
against the ground truth data by computing the difference between the two and adding this as a
layer in the napari viewer.

To use this widget, open it from the Plugins menu and select the two layers you wish to compare.



https://user-images.githubusercontent.com/17995243/146114112-c891723f-8640-4708-8014-c78731fb3396.mov



### Writing to Zip
Finally, you can save your segmentation to a zip file whose internal directory structure
will closely mimic that of the tracking challenge datasets, so that it may be opened 
again in the viewer.

To save your layer, choose File -> Save selected layer(s) with *one* labels layer selected,
then select label zipper from the dropdown choices.



https://user-images.githubusercontent.com/17995243/146114163-ee886990-979c-4756-97c5-aaf2c39dccde.mov



## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"workshop-demo" is free and open source software

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

[file an issue]: https://github.com/DragaDoncila/workshop-demo/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


