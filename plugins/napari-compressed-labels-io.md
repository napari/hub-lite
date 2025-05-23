
[![License](https://img.shields.io/pypi/l/napari-compressed-labels-io.svg?color=green)](https://github.com/DragaDoncila/napari-compressed-labels-io/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-compressed-labels-io.svg?color=green)](https://pypi.org/project/napari-compressed-labels-io)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-compressed-labels-io.svg?color=green)](https://python.org)
[![tests](https://github.com/DragaDoncila/napari-compressed-labels-io/workflows/tests/badge.svg)](https://github.com/DragaDoncila/napari-compressed-labels-io/actions)
[![codecov](https://codecov.io/gh/DragaDoncila/napari-compressed-labels-io/branch/master/graph/badge.svg)](https://codecov.io/gh/DragaDoncila/napari-compressed-labels-io)


## Description

This napari plugin provides readers and writers for labels and their corresponding image layers into zarr format for compression and portability. Each reader/writer pair supports a round trip of saving and loading image and labels layers.

## Writers
Two writers are provided by this plugin, each with its own reader.

### `labels_to_zarr`
This writer is an alternative to napari's default label writer and will write an entire labels layer, regardless of its dimensions, into a single zarr file. This writer provides the best compression option and its associated reader `get_zarr_labels` will read the layer back into napari.

This writer will be called when the user tries to save a selected labels layer into a path ending with .zarr

### `label_image_pairs_to_zarr`
This writer will save 3-dimensional labels and image layers from the viewer into individual zarrs for portability and convenience. For example, given one labels and one image layer of the shape (10, 200, 200) saved to my_stacks.zarr, 10 subdirectories will be created, each with two zarrs inside of shape (200, 200) corresponding to the labels and image layer.

This writer allows users to load stacks of associated images, label them, and then quickly save these stacks out into individual slices for easy loading, viewing and interaction. Its associated reader supports the loading into napari of the whole stack, all layers at one slice of the stack, and an individual layer of a given slice of the stack.

The writer currently supports only 3D layers, with the exception of RGB images of the form (z, y, x, 3), which are also supported.


## Readers

Two readers are provided by this plugin for loading the formats saved by each writer. These are detailed below.

### `get_zarr_labels`

This reader will open any zarr file with a .zarray at the top level in `path` as a labels layer. This is to be used in conjunction with `labels_to_zarr`.


### `get_label_image_stack`

This reader will open any zarr containing a `.zmeta` file as layers into napari. Depending on what is being opened, the reader will either load a full stack of labels and images, one slice of a stack of images and labels or an individual layer within a slice. This is to be used in conjunction with `label_image_pairs_to_zarr`.

## .zmeta

This metadata file contains information about the layer types in the stack and in each individual slice, as well as the number of image/label slices. This allows the reader plugin to load the correct layer types with appropriate names both at a stack level and at the individual slice level.

### An example .zmeta specification

```json
{
    "meta": {
        "stack": 7                               # number of slices in the entire stack (1 for an individual slice, 0 for a layer within a slice)
    },
    "data": {
        "image" : [                              # all image layers must be listed here
            {
                "name": "leaves_example_data",
                "shape": [790, 790, 3],
                "dtype": "uint8",
                "rgb": true                      # where rgb is false the image will be loaded as greyscale (colormap support has not yet been implemented)
            }
        ],
        "labels" : [
            {
                "name": "oak",
                "shape": [790, 790],
                "dtype": "int64"
            },
            {
                "name": "bg",
                "shape": [790, 790],
                "dtype": "int64"
            }
        ]
    }
}

```


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-compressed-labels-io` via [pip]:

    pip install napari-compressed-labels-io

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-compressed-labels-io" is free and open source software

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
[file an issue]: https://github.com/DragaDoncila/napari-compressed-labels-io/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


