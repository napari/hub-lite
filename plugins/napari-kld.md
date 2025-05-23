
[![License](https://img.shields.io/pypi/l/napari-kld.svg?color=green)](https://github.com/qiqi-lu/napari-kld/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-kld.svg?color=green)](https://pypi.org/project/napari-kld)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-kld.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-kld)](https://napari-hub.org/plugins/napari-kld)

`napari-kld` is a `napari` plugin that implements kernel learning deconvolution algrotihm.

## **Kernel Learning Deconvolution (KLD)**

KLD is a rapid deconvolution algorithm for fluorescence microscopic image, which learns the forward and backward kernels in Richardson-Lucy Deconvolution (RLD) from paired low-resolution (LR) and high-resolution (HR) images.

It only requires **one sample** to training the model, and **two iterations** to achieve a superior deconvolution performance compared to RLD and its variants using unmatched backward projection.

**This [napari] plugin was generated with [copier] using the [napari-plugin-template].*

## **Installation**

You must install `napari` firstly and then install `napari-kld`.

### **Install `napari`**

You can download the `napari` bundled app for a simple installation via https://napari.org/stable/tutorials/fundamentals/quick_start.html#installation.

Or, you can install `napari` with Python using pip:

```
conda create -y -n napari-env -c conda-forge python=3.10
conda activate napari-env
python -m pip install 'napari[all]'
```

Refer to https://napari.org/stable/tutorials/fundamentals/quick_start.html#installation.

### **Install `napari-kld`**

You can install `napari-kld` plugin with `napari`:

`Plugins` > `Install/Uninstall Plugins…` > [search napari-kld] > `install`.


Or you can install `napari-kld` via [pip]:

    pip install napari-kld

## **Instruction**
This plugin includes two part:

- `RL Deconvolution` : Conventional RLD algorithm using different type of backward kernels (including matched backward kernel [`Traditional`] and unmatched backward kernels [`Guassian`, `Butterworth`, `Wiener-Butterworth (WB)`]). The forward kernel, i.e., point spread function (PSF), is required.

- `KL Deconvolution` : KLD using learned forward/backward kernels.

**You can download the `"test"` folder  at https://github.com/qiqi-lu/kernel-learning-deconvolution for testing, which save some 2D/3D images used for training and testing.**

## **RL Deconvolution**

The conventional RLD using different type of backward kernels.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `RL Deconvolution`

2. Load input low-resolution (LR) image: `File` > `Open File(s)` > `[choose the image to be deconvolved]` > `[the image will appear in the layer list of napari]`, such as the simulated image `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train/raw/0.tif"`.

3. Choose the name of loaded image in `Input RAW data`, such as `"0"`.

4. Press `Choose` to choose a `PSF` correspongding to the loaded image, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train/psf.tif"`.

5. Choose the type of backward kernel in `Method` combo box:

    - `Traditional` : the backward kernel is just the flip of forward kernel (i.e., PSF).
    - `Guassian` : Guassian-shaped backward kernel, thw FWHM of which is same as the forward kernel.
    - `Butterworth` : Butterworth-shaped backward kernel, which is constructed using Butterworth filter.
    - `WB` : WB-shaped backward kernel, which is constructed by combining Wiener and Butterworth filter.

6. Set the number of RL iterations `Iterations` and parameters of backward kernel*.

7. Press `run` button to do deconvolution.

8. Wait the `progress bar` to reach 100%.

9. The output deconved image will appear in the layer list named as `{name of input image}_deconv_{Method}_iter_{Iterations}`, such as `"0_deconv_traditional_iter_30"`.

**The adjustment of parameters of backward kernels should refer to the paper : Guo, M. et al. Rapid image deconvolution and multiview fusion for optical microscopy. Nat Biotechnol 38, 1337–1346 (2020).*

## **KL Deconvolution**

### **Training data preparation**

The data used for training must be prepared in a folder consisting of:

- A folder named `"gt"` (optional) , such as `"test/data/real/2D/train/gt"`, which saves all the GT images (only support .tif file).
- A folder named `"raw"`, such as `"test/data/real/2D/train/raw"`, which saves all the LR images (only support .tif file). The file names must be the same as those in `"gt"` folder.
- A file named `"train.txt"`, such as `"test/data/real/2D/train/train.txt"`, which saves the name of each image in `"gt"/"raw"` filder in each line.

### **When yuo have paired LR image and HR image**

When we have paired LR image and HR image, we can treat LR image as **raw input** and HR image as **ground truth** (GT). We can first learn the forward kernel and then learn the backward kernel in a **supervised strategy**.

#### **Training of Forward Projection**

Train the forward projection to learn forward kernel.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Training` tab.

3. Choose `Data Directory`, such as `"test/data/real/2D/train"`. Then the dimention of training data will show in the `Dimension` box.

4. Choose `Output Directory`, such as `"test/data/real/2D"`.

5. `PSF Directory` is not required as the PSF is unknown.

6. If the raw input and GT image have different intensity, please check the `Preprocess` check box, which will rescale the input and GT images to have the same intensity. Here, do not check.

7. In the `Forward Projection` box, set the parameters of training:
    - `Epoch` : number of epochs of training.
    - `Batch Size` : batch size of training data used during training.
    - `Kernel Size (z, xy)` : the size of forward kernel to learned.
    - `Optimizer` : the optimization algorithm. Default: Adam.
    - `Learning Rate` : learning rate of training.
    - `Decay Step` ： the decay step of learning rate. Note: `0` for no decay.
    - `Decay Rate` : the decay rate of learning rate.

8. Press `run` button. You can press the `stop` button to end the training.

9. Wait the `progress bar` to reach 100% and training finished.

After the training of forward projection, the results will be save in the `/checkpoints` folder in `Output Directory`, the model was named as `forward_bs_{batch size}_lr_{learning rate}_ks_{kernel size (z)}_{kernel size (xy)}`, such as `"test/data/real/2D/checkpoints/forward_bs_1_lr_0.001_ks_1_31"`, which consists of:
- a `log` folder saved the `Tensorboard` log, which can be opened with `Tensorboard`.
- many model checkpoints, named as `epoch_{epoch}.pt`.
- a `parameters.json` file saving the parameters used to training the model.

#### **Training of Backward Projection**

After training of forward projeciton, we can freeze the forward projeciton and then train the backward projeciton.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Training` tab.

3. Choose `Data Directory`, such as `"test/data/2D/real/train"`. Then the dimention of training data will show in the `Dimension` box.

4. Choose `Output Directory`, such as `"test/data/2D/real"`.

5. `PSF Directory` is no required as the PSF is unknown.

6. If the raw input and GT image have different intensity, please check the `Preprocess` check box, which will rescale the input and GT images to have the same intensity. Here, do not check.

7. In the `Backward Projeciton` box, set parameters for the trianing of backward projeciton.

    - `Training strategy` : `supervised` training or `self-supervised` training. Here, set as `supervised`, as we have the GT images. When choosing the `self-supervised` mode, a PSF is required.
    - `Iterations (RL)` : The number of iterations of RL iterative procedure. Default: 2.
    - `Epoch` : The number fo epochs used to traing the model.
    - `Batch Size` : The batch size used to training the model.
    - `Kernel Size (z, xy)`: The size of backward kernel, `x` and `y` have the same size.
    - `FP directory` : the directory of the pre-trained forward projeciton model, such as `"test/data/real/2D/checkpoints/forward_bs_1_lr_0.001_ks_1_31/epoch_500_final.pt"` (commonly the model labeled with `"_final"` is used).
    - `Optimizer` : Optimization algorithm. Default: Adam.
    - `Learning Rate` : The learning rate used to trianing the model.
    - `Decay Step` : the decay step of learning rate.
    - `Decay Rate` : the decay rate of learning rate.

8. Press `run` button. You can press the `stop` button to end the training.

9. Wait the `progress bar` to reach 100% and then the training finishes.

When the training finishes, the results will be save in the `/checkpoints` folder in `Output Directory`, the model was named as `backward_bs_{batch size}_lr_{learning rate}_iter_{num of RL iterations}_ks_{kernel size (z)}_{kernel size (xy)}`, such as `"test/data/real/2D/checkpoints/backward_bs_1_lr_1e-05_iter_2_ks_1_31"`, which consists of:

- a `log` folder saved the `Tensorboard` log, which can be opened with `Tensorboard`.
- many model checkpoints, named as `epoch_{epoch}.pt`.
- a `parameters.json` file saving the parameters used to training the model.

Now we get the learned forward projection and backward projection.

Next, we can use them to do `Prediction`.

### **When you only have a PSF**

When you only have a PSF to do deconvolution, you can train the model using simulated data following the below steps:

1. Generate simulaiton data.
2. Train the model under supervised mode.
3. Apply the trained model on real data.

#### **Simulation data generation**

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Simulation` tab.

3. Choose the `Output Directory` of the generated simulation data, such as `"test\data\simulation"`.

4. Choose the `PSF Directory` (only support 2D/3D PSF file save as .tif, axes = (y, x) or (z, y, x)), such as `"test\data\simulation\psf.tif"`.

5. Adjust the parameters as needed.
    - `Image Shape` : the shape of simulated image, when `z=1`, 2D image will be generated.
    - `PSF Crop` : when the input PSF is too large, you can crop the PSF to acuqire a smaller PSF. All the PSF will be converted to have an odd shape and normalized.
    - `Num of Simulations` : number of generated images.
    - `Gaussian (std)` : the standard deviation (std) of Gaussian noise added in the generated LR images. The mean of Gaussian noise = 0. Default: 0 (i.e., without gaussian noise).
    - `Poisson` : whether to add Poisson noise, if `True`, make the `Enable` checked.
    - `Ratio` : a ratio factor multiplied on GT image to control the level of Poisson noise, thus the simulated raw input LR image RAW can be expressed as:

    $$ RAW = Possion((GT \cdot Ratio)\times PSF) + Gaussian $$

    - `Scale Factor` : downsampling scale factor. Default: 1.

6. Press `run` button.

7. Wait the `progress bar` to reach 100%.

The generated simulation data will be save in `Output directory`, named as `"data_{shape_z}_{shape_y}_{shape_x}_gauss_{std of Gaussian noise}_poiss_{whether to add Poisson noise}_ratio_{Ratio}"`, such as: `"test\data\simulation\data_128_128_128_gauss_0.0_poiss_0_ratio_1.0\train"`

- `"data\train\gt"` saves the GT images which consist of structures with various shapes*.
- `"data\train\raw"` saves the RAW images with blur and noise.
- `"data\train\parameters.json"` is a dictionary of parameters used to generate the simulation data.
- `"data\train\psf.tif"` is the PSF used in the simulation data generation (as the original PSF may be cropped).
- `"data\train\train.txt` save all the image used to train the model.

After you generate simulation data, you can use them to train the model.

**the code was refered to the paper: Li, Y. et al. Incorporating the image formation process into deep learning improves network performance. Nat Methods 19, 1427–1437 (2022).*

*You may need to adjust the noise level in the image accordding to the real acuqired data.*

#### **Training with known PSF and simulated data**

The simulated data should be those generated using the known PSF.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Training` tab.

3. Choose `Data Directory`, such as `test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train"`, which saves the data used to train the model in should include:
    - A `gt` folder saves the GT images
    - A `raw` folder save the raw input LR images with the same file name as GT images
    - A `train.txt` file saves all the file names used to train the model (does not need to list all the files in `gt`/`raw` folder but at least one).

4. Choose a `Output Directory` to save the model checkpoints, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0"`.

5. Choose `PSF Directory` of the PSF corresponding to the data, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train/psf.tif"`. Then the `Forward Projection` group box will be invisible as we do not need to learn the forward kernel when we know the PSF. Just use the PSF as the forward kernel.

6. If the raw input and GT image have different intensity, please check the `Preprocess` check box, which will rescale the input and GT images to have the same intensity. Here, do not check.

7. Then set parameters to learn the backward kernel.

    - `Training Strategy` : `supervised` training or `self-supervised` training. Here, set as `supervised`, as we have the GT images.
    - `Iterations (RL)` : the number of iterations of RL iteration procedure. Default: 2.
    - `Epoch` : the number fo epochs used to traing the model.
    - `Batch Size` : the batch size used to training the model.
    - `Kernel Size (z, xy)`: the size of backward kernel, `x` and `y` directions have the same size.
    - `FP Directory` : the directory of the forward projeciton model. Here, it is disabled as the PSF is known.
    - `Optimizer` : Optimization algorithm. Default: Adam.
    - `Learning Rate` : the learning rate used to trianing the model.
    - `Decay Step` : the decay step of learning rate.
    - `Decay Rate` : the decay rate of learning rate.

8. Press `run` button. You can press the `stop` button to end the training.

9. Wait the `progress bar` to reach 100% and the training finishes.

When the training finishes, a checkpoints folder will be created in `Output Directory` such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/checkpoints"`.

The models is save in `/checkpoints` folder, which is named as `"backward_bs_{batch size}_lr_{learning rate}_iter_{num of RL iterations}_ks_{kernel size (z)}_{kernel size (xy)}"`, such as `"/checkpoints/backward_bs_1_lr_1e-06_iter_2_ks_1_31"`, consists of:

- A `log` folder saved the `Tensorboard` log, which can be open with `Tensorboard`.
- Many model checkpoints, named as `epoch_{epoch}.pt`.
- A `parameters.json` file saving the parameters used to training the model.

### **When you only have LR image and corresponding PSF**
When we only have LR image and its PSF, we can traing the backward projection through supervised training using simulation data as introduced above. The plugin also provide an alternative self-supervised training stratergy to learn the backward kernel.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Training` tab.

3. Choose `Data Directory`, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train"`.

4. choose `Output Directory`, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0"`.

5. Choose `PSF Directory`, such as `"test/data/simulation/data_128_128_128_gauss_0.0_poiss_0_ratio_1.0/train/psf.tif"` then the `Forward Projection` box will be invisiable.

6. As there is no GT image, preprocessing is not needed. Do not check `Preprocess` check box.

7. In the `Backward Projeciton` box, set parameters for the trianing of backward projeciton.

    - `Training strategy` : `supervised` training or `self-supervised` training. Set as `self-supervised`, as we do not have the GT images.
    - `Iterations (RL)` : the number of iterations of RL iteration procedure. Default: 2.
    - `Epoch` : the number fo epochs used to traing the model.
    - `Batch Size` : the batch size used to training the model.
    - `Kernel Size (z, xy)`: the size of backward kernel, `x` and `y` directions have the same size.
    - `FP Directory` : the directory of the forward projeciton model. Here, it is disabled as the PSF is known.
    - `Optimizer` : Optimization algorithm. Default: Adam.
    - `Learning Rate` : the learning rate used to trianing the model.
    - `Decay Step` : the decay step of learning rate.
    - `Decay Rate` : the decay rate of learning rate.

8. Press `run` button. You can press the `stop` button to end the training.

9. Wait the `progress bar` to reach 100% and training finishes.

When the training finishes, the results will be save in the `/checkpoints` folder in `Output Directory`, the model was named as `backward_bs_{batch size}_lr_{learning rate}_iter_{num of RL iterations}_ks_{kernel size (z)}_{kernel size (xy)}_ss`, such as `"/checkpoints/backward_bs_1_lr_1e-05_iter_2_ks_31_31_ss"`, which consists of:

- a `log` folder saved the `Tensorboard` log, which can be opened with `Tensorboard`.
- many model checkpoints, named as `epoch_{epoch}.pt`.
- a `parameters.json` file saving the parameters used to training the model.

*The performance of self-supervised learning may be inferior to supervised learning according to our experiments.*

### **Prediction**
Use the learned forward/backward kernel to do deconvolution.

1. Open `napari` and load `napari-kld` plugin: `Plugins` > `Kernel Learning Deconvolution` > `KL Deconvolution`

2. Choose `Prediction` tab.

3. Load raw input low-resolution image through `napari`: `File` > `Open File(s)` > `[choose the image to be deconvolved]` > `[the image will appear in the layer list of napari]`, such as `"test/data/real/2D/test/raw/2.tif"`.

4. Choose the loaded image in `Input RAW data` box, e.g., `2`.

5. If the PSF is known, choose the `PSF directory`.

6. If the PSF is unknown, choose the `Forward Projection` directory, such as `"test/data/real/2D/checkpoints/forward_bs_1_lr_0.001_ks_1_31/epoch_500_final.pt"` (commonly the model labeled with `"_final"` is used). If both the directories of PSF and Forward Projeciton is choosen, KLD will directly use the PSF selected.

7. Choose the `Backward Projeciton` directory, such as `"test/data/real/2D/checkpoints/backward_bs_1_lr_1e-05_iter_2_ks_1_31/epoch_1000_final.pt"`  (commonly the model labeled with `"_final"` is used).

8. Set the number of RL iterations at `Iterations (RL)`. Default: 2.

9. Press run to do deconvolution.

10. Wait the progress bar to reach 100%.

The deconvolved image will be directly shown in the `layer list` of `napari`, named as `"{input data name}_deconvo_iter_{number of RL iterations}"`, e.g., `"16_deconv_iter_2"`. You can save it as needed.

### **Others**
The `log` tab print the message during running.
Press `clean` button will clean all the text in the `log` box.

### **Notice**

- *Currently, the plugin is runned on CPU. We have tried to run the training on GPU, but the training time did not decrease (maybe it is because the FFT-based covnlution was not optimized on GPU). We are trying to make improvements.*

- *The training time may be very long if we set the kernel size or the number of epoches too large, especially for 3D images. Besides, it also depends on the  computation capability of your device.*

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

MIT LICENSE

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
