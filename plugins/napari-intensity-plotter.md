
[![License BSD-3](https://img.shields.io/pypi/l/napari-intensity-plotter.svg?color=green)](https://github.com/Tbrn1103/napari-intensity-plotter/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-intensity-plotter.svg?color=green)](https://pypi.org/project/napari-intensity-plotter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-intensity-plotter.svg?color=green)](https://python.org)
[![tests](https://github.com/Tbrn1103/napari-intensity-plotter/workflows/tests/badge.svg)](https://github.com/Tbrn1103/napari-intensity-plotter/actions)
[![codecov](https://codecov.io/gh/Tbrn1103/napari-intensity-plotter/branch/main/graph/badge.svg)](https://codecov.io/gh/Tbrn1103/napari-intensity-plotter)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-intensity-plotter)](https://napari-hub.org/plugins/napari-intensity-plotter)

# napari-intensity-plotter

**napari-intensity-plotter** is a plugin for **[napari](https://napari.org)** that provides tools to measure and plot intensity profiles in 2D time-series images.

![Intensity Plot Widget](images/intensity_plot_widget_example.png)

*Screenshot: Intensity profile of a region of interest in a 2D time-series image.*

## Features

- **Intensity Plot Widget**: Allows you to select a region of interest in a 2D time-series image and plot the intensity profile over time.
- **Intensity Plot Control Widget**: Lets you fine-tune plot parameters and save the results as CSV or PNG files.

## Installation

You can install `napari-intensity-plotter` via pip:

```bash
pip install napari-intensity-plotter
```

Alternatively, you can install it directly from the napari plugin interface.

### Usage

1. **Load a 2D Time-Series Image**  
   Load a 2D time-series image (e.g., fluorescence microscopy data) in napari.

2. **Activate the Widgets**  
   Open the `Intensity Plot Widget` and `Intensity Plot Control Widget` from the `Plugins` menu in napari.

3. **Intensity Plot Widget**  
   - Move your mouse over the image, or click on a specific location to plot the intensity profile of the selected region across slices (e.g., time).
   - The region of interest (ROI) size can be adjusted using the square size setting in the control widget.

4. **Intensity Plot Control Widget**  
   - Configure the square size for the ROI (ensures that the region size remains odd).
   - Set the directory to save plots and intensity data.
   - Save the intensity profile as a `.csv` or `.png` file by clicking the corresponding buttons or using keyboard shortcuts (`Ctrl+S`).

5. **Additional Controls**  
   - Hide all layers using the `Hide All Layers` button or `Ctrl+D`.
   - Use the rectangle to visualize the selected ROI.

### Example Workflow

**Step 1**: Load a 2D time-series image (e.g., `tif` or `nd2`) into napari. Ensure the layer is visible.

**Step 2**: Open the `Intensity Plot Widget` to visualize intensity changes over time or slices for a specific ROI.

**Step 3**: Use the `Intensity Plot Control Widget` to:
- Adjust the square size for the ROI.
- Specify a directory to save intensity data.
- Enable saving in CSV or PNG formats.
  
**Step 4**: Save the plotted intensity data by clicking `Save to CSV/PNG` or pressing `Ctrl+S`.

**Step 5**: Hide all layers if necessary using `Hide All Layers` or `Ctrl+D`.

## Contributing

Contributions are welcome! If you encounter issues or have ideas for new features, please submit them via the [GitHub Issues](https://github.com/Tbrn1103/napari-intensity-plotter/issues).

## Acknowledgements

This plugin was developed using the **napari plugin cookiecutter template**, which greatly streamlined the creation of this tool. See the [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin) for more details.

Special thanks to the napari community for their continuous support and resources.

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.
