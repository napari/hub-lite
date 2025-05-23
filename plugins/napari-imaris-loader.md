

# Description

This plugin enables viewing of Bitplane Imaris files, including very large datasets.  The GIFs below demonstrate rendering of a ~2TB IMS file containing a 2 color whole mouse brain.  The plugin has been tested on datasets as large as 20TB.

**NOTE: For this plugin to work "File/Preferences/Experimental/Render Images Asynchronously" must be selected.**

### Open IMS file:

![Open IMS file GIF](https://i.imgur.com/ByHb0wI.gif "Open IMS file")



### Render in 3D:

A plugin is provided to dynamically reload the data after selecting the lowest resolution level to be included in the viewer.  Since napari only renders the lowest resolution, the user can use this plugin to control the quality of 3D rendering.  See features and limitations for tips on suggested usage.

![3D Rendering and Quality Adjustment GIF](https://i.imgur.com/MZNlWtM.gif "3D Rendering and Quality Adjustment")

### Features

* Multiscale Rendering
  * Image pyramids which are present in the native IMS format are automatically added to napari during file loading.
* Chunks are implemented by dask and matched to the chunk sizes stored in each dataset.  (Napari appears to only ask for 2D chunks - unclear how helpful this feature is currently)
* Successfully handles multi-terabyte multi-timepoint multi-channel datasets.
* Tested with all sample files provided by Bitplane.
* Higher 3D rendering quality is enabled by a widget that reloads data after specifying the lowest resolution level (higher number = lower resolution) to be included in the multiscale series.

### Known Issues / limitations

* Currently, this is **only an image loader**, and there are no features for loading or viewing objects
* Napari sometimes throws errors indicating that it expected a 3D or 5D array but receives the other.
  * This sometimes *but relatively rarely* causes napari to crash
  * Would like to enable Asynchronous Tiling of Images, but this results in more instability and causes crashes.


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-imaris-loader` via [pip]:

    pip install napari-imaris-loader

## Change Log:

##### <u>v0.1.2:</u>

**Fixed:** Issue where .ims files containing a single color 2D image would not open.

**Fixed:** Issue where using the widget to change resolutions while in 3D rendering would cause a crash.  Now the viewer is automatically forced into 2D rendering mode when the widget is used.

**Dependency change:** The loader is now dependent in a separate package for loading IMS files.  https://pypi.org/project/imaris-ims-file-reader/

**v0.1.3:**

Documentation

**v0.1.4:**

Add napari to install requirements for plugin compatibility

**v0.1.5:**

Changes to napari:

- now requires napari[all] upon install.
- requires >=v0.1.5 of imaris-ims-file-reader

**v0.1.6:**

- Fix issue #7 where contrastLimits possibly unbound in reader

**v0.1.7:**

- For squeeze_output=False when opening .ims file for Napari compatibility

**v0.1.8:**

- Add automatic determination of contrast_limits
- Fix bug in squeeze_output

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-imaris-loader" is free and open source software

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

[file an issue]: https://github.com/AlanMWatson/napari-imaris-loader/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


