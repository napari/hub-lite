
[![License BSD-3](https://img.shields.io/pypi/l/napari-boardgame-maker.svg?color=green)](https://github.com/jo-mueller/napari-boardgame-maker/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-boardgame-maker.svg?color=green)](https://pypi.org/project/napari-boardgame-maker)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-boardgame-maker.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-boardgame-maker/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-boardgame-maker/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-boardgame-maker/branch/main/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-boardgame-maker)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-boardgame-maker)](https://napari-hub.org/plugins/napari-boardgame-maker)

This plugin turns 2D grayscale images into 3D-printable landscape tiles for a certain all-time tabletop boardgame which revolves around building settlements, obtaining ressources expanding and collecting more points than your opponents.

In short, images (for instance, [digital elevation models](https://en.wikipedia.org/wiki/Digital_elevation_model)) can be turned into surfaces like this:

| Image | Created tile|
| --- | --- |
| <img src="https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/sample.png"> | <img src="https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/sample_as_tile.png"> |

## Data

In principle, all 2D grayscale image data can be used to create a tile. However, using digital elevation models is particularly cool. Such data is publicly available at [OpenTopography.org](https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.2). Acknowledgement:

```text
 NASA JPL. NASADEM Merged DEM Global 1 arc second V001. 2020, distributed by NASA EOSDIS Land Processes DAAC, https://doi.org/10.5067/MEaSUREs/NASADEM/NASADEM_HGT.001.
```
## Usage

To use the boardgame tile maker, open it from the plugins menu (`Plugins > napari-boardgame-maker: Boardgame Tile Maker`) or from the tools menu (`Tools > Boardgame tile maker (npbgm)`). There are a few steps and parameters to set before the tile can be created.

[](https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/GUI_screenshot.jpg)

Clicking on `Make hexagon` and `Make number field` will create a hexagonal shape in the viewer (which will be the outline of the tile) and a circular field (which can later be used to put some markers, figures, chips, etc. On the center of the board).

![](https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/sample_with_shapes.png)

The next step is to set the parameters for the tile. The following parameters can be set:

### Radii and sizes

The following sketch shows the different radii and sizes that can be set:

![](https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/stride_and_town.png)

- `hexagon radius`: The radius of the hexagon (in pixels). Upon export, this will be rescaled to a desired physical size in mm.
- `number field radius`: The radius of the number field (in pixels). Can also be set in mm units. The pixels are changed accordingly if the size of the whole hexagon is changed.
- `stride`: The region next to the edge of the tile that should remain flat.
- `town radius`: A circular region around the edges of the hexagonal tiles that should remain flat.

### Topography

The following parameters can be set to create the topography of the tile:

![](https://github.com/jo-mueller/napari-boardgame-maker/raw/main/docs/imgs/slope_and_heights.png)

- `slope`: Adds a smooth transition of a given width between the edge of the cropped topography and the level of the base platte. Setting this to zero will result in a sharp edge.
- `z-multiplier`: The height of the topography is multiplied by this factor. This can be used to scale the topography to the desired height.
- `Plate thickness`: The thickness of the base plate (in mm).

### Export

- CLicking on `produce tile` will run the workflow to create the tile
- Clicking `Export` will open a dialog to save the tile as an `.stl` file. *Note*: The tile will be exported in the size of the hexagon radius. If the hexagon radius is set to 100 mm, the tile will be exported as a 100 mm hexagon.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-boardgame-maker` via [pip]:

    pip install napari-boardgame-maker


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-boardgame-maker" is free and open source software

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
