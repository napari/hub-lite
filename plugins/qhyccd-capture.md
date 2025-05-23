
## Project Introduction

`qhyccd-capture` is a basic operation library for handling QHYCCD series cameras. This library provides functionalities to interact with QHYCCD cameras, including camera connection, parameter setting, image capture, and display. This project is a [napari] plugin, aimed at simplifying the use of the camera through a graphical user interface.

## Features

- **Camera Connection**: Supports loading the corresponding QHYCCD dynamic link libraries on different operating systems (such as Windows, Linux, macOS) and initializing camera resources.
- **Parameter Setting**: Provides the functionality to set camera parameters, such as exposure time, gain, offset, USB bandwidth, etc.
- **Image Capture**: Supports single-frame mode exposure and retrieves image data.
- **Image Display**: Displays captured images through napari, supports distributed display, single display, and sequence display modes.
- **Histogram and White Balance**: Provides histogram equalization and white balance adjustment functions.
- **ROI (Region of Interest)**: Supports creating and applying ROIs to operate on specific areas.
- **Video Recording**: Supports video recording and saves in various video formats.
- **Temperature Control**: Supports temperature control and displays temperature.
- **CFW Control**: Supports CFW control and displays CFW status.
- **Star Point Resolution**: Supports star point resolution and displays the results.

![qhyccd-capture 插件界面显示](https://raw.githubusercontent.com/LiuQiang-AI/qhyccd-capture/main/src/qhyccd_capture/images/image.png)

## Installation
You can install via pip:

    pip install qhyccd-capture

To install the latest development version:

    pip install git+https://github.com/nightliar-L/qhyccd-capture.git

## Dependency Installation
#### Astrometry.net 
Currently, astrometry.net only supports the Ubuntu system.

    sudo apt-get install astrometry.net
    sudo apt-get install astrometry-data-tycho2
    sudo vim ~/.bashrc
    # Add the following content
    export PATH=$PATH:/usr/local/astrometry/bin

## Version Changes

- 2024-10-23 Version 0.0.1 Initial version
- 2024-10-24 Version 0.0.2 Fixed some issues introduced by the release
- 2024-10-24 Version 0.0.3 Optimized some functions and processing logic

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"qhyccd-capture" is free and open source software
