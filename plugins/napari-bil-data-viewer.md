<p href="https://www.brainimagelibrary.org/">
    <align="center" width="100%">
    <img width="100%" src="https://i.imgur.com/ljZKq8h.png">
</p>


# Description

View datasets archived at the **[Brain Image Library](https://www.brainimagelibrary.org/)**.

**NOTE: This plugin is under early development.  Currently, only a subset of single-channel, fMOST datasets which include projections are available to view.  An example can be found [here]( https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/).



![Plugin Demo GIF](https://imgur.com/gkDCsMd.gif "Plugin Demo GIF")



### Features

* Multiscale Rendering
  * In datasets that include multiple resolution representations of the data, each resolution can be combined to improve the speed of browsing and user experience.  An example of a dataset with multiple resolution projections can be found [here](https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/).
  * All datasets included in the current release of napari-bil-data-viewer use multi-resolution datasets.
* 3D rendering of whole datasets.  The lowest resolution is used for rendering.  Currently, this is a limitation imposed by napari.
* The plugin does NOT require a BIL account as datasets are already accessible via https.

### Known Issues / limitations
* Currently the only datasets that are available are those which have been manually selected by the developers.  If you would like a specific dataset to be included please consider adding the dataset(s) to the [dataset_info.py](https://github.com/brain-image-library/napari-bil-data-viewer/blob/main/napari_bil_data_viewer/dataset_info.py) file and submitting a pull request.
* To inquire about this plugin please contact Brain Image Library support:  bil-support@psc.edu
* The plugin is still under development.  We appreciate all [reports of issues / errors](https://github.com/brain-image-library/napari-bil-data-viewer/issues) which occur during use.


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

Option #1: Install plugin via the napari plugin menu

1. Menu: Plugins >> Install/Uninstall Plugins
2. Search: napari-bil-data-viewer
3. Select install

Option #2:  Install a fresh python virtual environment

```bash
# Example of venv creation using conda
conda create -y -n bil-viewer python=3.8
conda activate bil-viewer

# Install napari-bil-data-viewer
pip install napari-bil-data-viewer

# Run Napari
napari
```

## Contributing

Please consider contributing to this project!  Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-bil-data-viewer" is free and open source software

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

[file an issue]: https://github.com/brain-image-library/napari-bil-data-viewer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

## Change Log:

##### <u>v0.1.0:</u>

Initial release.

<u>**v0.1.1 & v0.1.2:**</u>

Changes to documentation

<u>**v0.1.3:**</u>

Added all available summary fMOST datasets

<u>**v0.2.0:**</u>

Added support for SWC neuron tracings

<u>**v0.3.0:**</u>

Added support for multiscale OME zarr data

<u>**v0.4.0:**</u>

Add scale controls for layers

<u>**v0.4.2:**</u>

Add URL input to visualize image stacks (tif, tiff, jp2)

<u>**v0.5.0:**</u>

Split the plugin into 5 widgets:<br/>
- Load Curated Datasets
- Load Image Stack From URL
- Load Multiscale Data From URL
- Load Neuron Morphology From URL
- Layer Scale Controls

<u>**v0.5.1:**</u>

Add metadata link to curated datasets

<u>**v0.6.0:**</u>

Add widget to visualize histology RGB tiffs
