
[![MIT License](https://img.shields.io/github/license/Biomedical-Imaging-Group/napari-psfgenerator)](https://github.com/Biomedical-Imaging-Group/napari-psfgenerator/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-psfgenerator.svg?color=green)](https://pypi.org/project/napari-psfgenerator)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-psfgenerator.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-psfgenerator)](https://napari-hub.org/plugins/napari-psfgenerator)

## PSF Generator Napari Plugin

The **PSF Generator Napari Plugin** provides an intuitive, interactive platform for simulating **Point Spread Functions (PSFs)** directly within the Napari ecosystem. Built on **PyTorch**, this plugin supports both **CPU and GPU-accelerated** computations, ensuring fast and efficient simulations for fundamental and advanced optical modeling.

### Key Features:

- **Flexible Propagation Models:** Scalar and vectorial propagators in Cartesian and spherical coordinates.
- **Customizable Parameters:** Configure **physical** (e.g., numerical aperture, wavelength), **numerical** (e.g., pixel size, Z-stacks), and **optical settings** (e.g., Gibson-Lanni corrections, Zernike aberrations).
- **Real-Time Visualization:** Seamless integration with Napari for immediate visual feedback.
- **Versatile API:** Access propagators programmatically for custom workflows.
- **Image Export:** Save computed PSFs in **TIFF format**.

This plugin is a powerful tool for researchers in **optics, computational microscopy, and imaging science**, bridging user-friendly interactivity with the computational capabilities of our Python library.

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

Set up a Python virtual environment and install napari following this [guide].

You can install `napari-psfgenerator` via [pip]:

    pip install napari-psfgenerator

To install latest development version :

    pip install git+https://github.com/Biomedical-Imaging-Group/napari-psfgenerator.git


Now you can try the plugin out! Open napari, click on the menu "Plugins" and select "Propagators (PSF Generator)".


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-psfgenerator" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template
[guide]: https://napari.org/dev/tutorials/fundamentals/installation.html
[file an issue]: https://github.com/VStergiop/napari-psfgenerator/issues
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[psf_generator library]: https://github.com/Biomedical-Imaging-Group/psf_generator
[plugin]: https://github.com/Biomedical-Imaging-Group/napari-psfgenerator
