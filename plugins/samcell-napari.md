
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/samcell-napari)](https://pypi.org/project/samcell-napari/)

A napari plugin for cell segmentation using the Segment Anything Model (SAM) foundation model.

![SAMCell Segmentation Example](https://github.com/saahilsanganeriya/samcell-napari/raw/main/docs/images/samcell-napari.jpg)

## Description

SAMCell-napari provides an intuitive interface for segmenting cells in microscopy images using deep learning. It leverages the power of the Segment Anything Model (SAM) adapted specifically for biological cell segmentation, providing accurate results with minimal tuning.

### Key Features:
- Simple, user-friendly interface within napari
- Compatible with SAMCell models in multiple formats (`.pt`, `.bin`, `.safetensors`)
- Support for both SAM-ViT-Base and SAM-ViT-Large model architectures
- Adjustable segmentation parameters for fine-tuning
- Real-time visualization of results
- Distance map visualization for analyzing cell proximity
- Full integration with napari's layer system
- Enhanced sliding window algorithm with advanced blending for seamless segmentation of large images

### What's New in v1.0.0:
- Support for multiple model file formats (`.pt`, `.bin`, `.safetensors`)
- Improved sliding window algorithm with smooth blending between crops
- Better handling of small images and edge cases
- Enhanced error recovery and logging
- Multiple threshold testing capability
- Optimized default thresholds for better segmentation results
- Support for both SAM-ViT-Base and SAM-ViT-Large model variants

## Installation

You can install `samcell-napari` via [pip]:

```bash
pip install samcell-napari
```

To install latest development version:

```bash
pip install git+https://github.com/saahilsanganeriya/samcell-napari.git
```

## Usage

1. Start napari
   ```bash
   napari
   ```

2. Load your image in napari

3. Open the SAMCell plugin:
   ```
   Plugins > samcell-napari > SAMCell Segmentation
   ```

4. Provide the path to your SAMCell model file (supports `.pt`, `.bin`, or `.safetensors` formats)
   - You can download pre-trained models from the [official SAMCell release page](https://github.com/saahilsanganeriya/SAMCell/releases/tag/v1)

5. Adjust parameters if needed:
   - Cell peak threshold: Higher values detect fewer cells (default: 0.47)
   - Cell fill threshold: Lower values create larger cells (default: 0.09)
   - Crop size: Size of image crops for processing (default: 256)

6. Click "Run Segmentation"

7. View the segmentation results in napari as a Labels layer

## Requirements

- Python 3.8 or higher
- napari 0.4.14 or higher
- PyTorch 1.9 or higher
- transformers 4.20.0 or higher
- CUDA-capable GPU recommended for faster processing

## Model Compatibility

The plugin is compatible with SAMCell model files in multiple formats:
- PyTorch model files (`.pt`)
- Binary model files (`.bin`) - including the standard `pytorch_model.bin`
- SafeTensors files (`.safetensors`) - a safer alternative to PyTorch's pickle-based format

The plugin supports models based on:
- SAM-ViT-Base architecture - Primary model type
- SAM-ViT-Large architecture - Fallback if a model doesn't load with base architecture

Pre-trained models can be downloaded from the [official SAMCell release page](https://github.com/saahilsanganeriya/SAMCell/releases/tag/v1).

Recommended models include:
- SAMCell1.0-Cellpose-cyto: Trained on the Cellpose cytoplasm dataset
- SAMCell1.0-livecell: Trained on the LiveCELL dataset

These models are part of the release assets for the paper "SAMCell: Generalized Label-Free Biological Cell Segmentation with Segment Anything".

## How It Works

SAMCell operates using an enhanced sliding window approach to process large images:

1. The image is divided into overlapping crops with intelligent handling of image boundaries
2. Each crop is processed through a SAM-based model
3. A distance map is created, representing cell centers and boundaries
4. The crops are stitched back together with smooth blending for seamless transitions
5. The distance map is processed to extract individual cell masks using watershed segmentation
6. Results are displayed in napari as labels

## Technical Details

### Model Type Detection

The plugin intelligently determines the appropriate SAM model architecture:
1. First tries to load the model with SAM-ViT-Base architecture
2. If that fails, automatically falls back to SAM-ViT-Large
3. This ensures maximum compatibility with various pre-trained models

### Sliding Window Algorithm

The plugin uses an advanced sliding window algorithm that:
- Handles images of any size, including those smaller than the crop size
- Creates appropriate overlaps between crops to ensure no cells are missed
- Uses a cosine-based blending mask to create smooth transitions between crops
- Fills any potential gaps using nearest neighbor interpolation

### Multiple Threshold Testing

For researchers who want to optimize segmentation parameters, the plugin includes a batch processing capability to test multiple threshold combinations at once (available via the API).

## Contributing

Contributions are very welcome! Please feel free to submit a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Citation

If you use this plugin in your research, please cite:

```
@article{samcell2023,
  title={SAMCell: Generalized Label-Free Biological Cell Segmentation with Segment Anything},
  author={...},
  journal={...},
  year={2023}
}
``` 
