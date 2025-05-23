The napari plugin for UniSPAC [A Unified Segmentation framework for Proofreading and Annotation in Connectomics]. UniSPAC provides interactive 3D neuron segmentation. Neuron segmentation, proofreading and tracking can be done with just mouse clicks, which is much more efficient than existing tools.

## Requirements

A system with enough GPU memory and pytorch installed. The size of the GPU memory is related to the size of the vEM image that can be processed. For  `test_roi1_sub_z0-100.tiff` with a shape of 800x800x100, the recommended minimum GPU memory is 12GB.

## Installation

Step 1: install napari via pip:

```
pip install -U 'napari[all]'
```

Step 2: install `napari-UniSPAC`

```
git clone https://github.com/ddd9898/napari-UniSPAC.git
cd napari-UniSPAC
pip install -e .
```

Step 3: run napari:

```
napari
```

You can familiarise yourself with how UniSPAC's napari plugin operates by labeling  `test_roi1_sub_z0-100.tiff`, which is an example of Drosophila vEM images.
