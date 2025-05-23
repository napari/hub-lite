
[![License MIT](https://img.shields.io/pypi/l/Large-Image-Viewer.svg?color=green)](https://github.com/WyssCenter/Large-Image-Viewer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/Large-Image-Viewer.svg?color=green)](https://pypi.org/project/Large-Image-Viewer)
[![Python Version](https://img.shields.io/pypi/pyversions/Large-Image-Viewer.svg?color=green)](https://python.org)
[![tests](https://github.com/WyssCenter/Large-Image-Viewer/workflows/tests/badge.svg)](https://github.com/WyssCenter/Large-Image-Viewer/actions)
[![codecov](https://codecov.io/gh/WyssCenter/Large-Image-Viewer/branch/main/graph/badge.svg)](https://codecov.io/gh/WyssCenter/Large-Image-Viewer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/Large-Image-Viewer)](https://napari-hub.org/plugins/Large-Image-Viewer)

A simple plugin to view large images

----------------------------------

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `Large-Image-Viewer` via [pip]:

    pip install Large-Image-Viewer



To install latest development version :

    pip install git+https://github.com/WyssCenter/Large-Image-Viewer.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"Large-Image-Viewer" is free and open source software

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

[file an issue]: https://github.com/WyssCenter/Large-Image-Viewer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/




# Napari Large Image Viewer Plugin

The Napari Large Image Viewer Plugin is a powerful extension for the [napari](https://napari.org/) image visualization software. This plugin is designed to enable the visualization of large TIFF | TIF  files directly from disk, without the need to load the entire image into RAM. This is particularly useful when working with large datasets that exceed the available memory of your system.


## Features

- **Efficient Large Image Visualization**: The plugin allows you to open and visualize large files that are too big to fit into memory. It utilizes efficient memory-mapping techniques to display image data without fully loading it into RAM.

- **Interactive Exploration**: With the Napari Large Image Viewer Plugin, you can interactively explore large datasets using familiar zooming, panning, and slicing actions.

- **Quick Installation**: Installing the plugin is simple and straightforward, and it seamlessly integrates with the napari environment.

- **User-Friendly Interface**: The plugin provides an intuitive user interface that integrates seamlessly into the napari interface, making it easy to use for both beginners and experienced users.

## Installation

1. **Prerequisites**: Make sure you have [napari](https://napari.org/) installed on your system. If not, you can install it using:

   ```bash
   pip install napari
   ```

2. **Install the Plugin**: You can install the plugin directly from GitHub using pip:

   ```bash
   pip install git+https://github.com/WyssCenter/Large-Image-Viewer.git
   ```

3. **Launch napari**: Launch napari from your terminal:

   ```bash
   napari
   ```

4. **Activate the Plugin**: Once napari is launched, go to the `Plugins` menu and select `Large Image Viewer` to activate the plugin.

5. **Open Large TIFF | TIF  File**: With the plugin activated, you can now open a large file by dragging and dropping it to the napari viewer.

## Usage

1. Open a Large TIFF | TIF  File: Follow the installation instructions above to open a large TIFF | TIF  file using the plugin.

2. Explore the Image: Once the image is loaded, you can use the mouse to zoom in/out, pan, and interactively explore the data. You can also adjust the colormap, contrast, and other visualization settings from the napari interface.

3. Slicing and Navigation: Use the slicing and navigation tools in napari to navigate through different sections of the large file.

4. Save Visualizations: You can save snapshots or screenshots of the current visualization using the napari interface.

## Contributions

Contributions to the Napari Large Image Viewer Plugin are welcome! If you encounter issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/WyssCenter/Large-Image-Viewer.git).

## License

This plugin is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or questions, you can reach out to the author at nima.mojtahedi@wysscenter.ch
