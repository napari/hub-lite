
Napari plugin for ROP data copying and segmentation assistance.

Provides tools for:
- Copying scan data based on a study parquet file.
- Loading local scan data into Napari.
- Basic segmentation tools (add layer, brush size, paint/erase).
- ROI-based Otsu thresholding.
- Full-view edge detection labeling.

## Installation

For development, install in editable mode:

```bash
cd Mani_Tools_plugins/mKw-RopCop
pip install -e .
```

Or install using the provided script:

```bash
python Mani_Tools_plugins/mKw-RopCop/install_dev.py
```

## Usage

Launch Napari. The "mKw RopCop" widget should appear in the Plugins menu.

Alternatively, launch with the helper script:

```bash
python Mani_Tools_plugins/mKw-RopCop/launch_ropcop.py
