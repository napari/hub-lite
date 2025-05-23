
![](https://raw.githubusercontent.com/hnguyentt/mousechd-napari/master/assets/demo.gif)

*Tool for heart segmentation and congenital heart defect detection in mice.*

## Installation

There are several ways to run the plugin: (1) from bundle, (2) Containers (Docker or Apptainer), (3) from code

### From Bundle

(1) Install Napari by following this instruction https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-a-bundled-app

(2) Install `mousechd-napari` plugin:
    * Run Napari
    * `Plugins` --> `Install/Uninstall Plugins ...` --> Search for `mousechd-napari` --> Click on `install`.

(3) Restart Napari to run the plugin


### Containers
#### Docker
##### Pull docker
```
sudo docker pull hoanguyen93/mousechd-napari
```

##### Run MouseCHD Plugin
* Run plugin with local resources:

    ```
    sudo docker run --gpus all -v <path/to/home/on/host>:<path/to/home/on/host> -it --rm -p 9876:9876 -p 6006:6006 hoanguyen93/mousechd-napari
    ```

    <details>
    <summary>Example:</summary>

    ```
    sudo docker run --gpus all -v /home/hnguyent:/home/hnguyent -it --rm -p 9876:9876 -p 6006:6006 hoanguyen93/mousechd-napari
    ```

    </details>

    Open this link on your browser: [http://localhost:9876/](http://localhost:9876/)

* Run plugin with server resources:

    * Follow [this instruction](./docs/server_setup.md) to setup running on server.
    * Copy ~/.ssh folder to a temporary location, for example in ~/Downloads: `cp -r ~/.ssh ~/Downloads/`
    * Change ownership for temporary ~/Downloads/.ssh folder: `chown -R root:root ~/Downloads/.ssh`
    * Run docker: `udo docker run --gpus all -v <path/to/home/on/host>:<path/to/home/on/host> -v /home/hnguyent/Downloads/.ssh:/root/.ssh:ro -it --rm -p 9876:9876 -p 6006:6006 hoanguyen93/mousechd-napari`
    * Open this link on your browser: [http://localhost:9876/](http://localhost:9876/)

##### Known issues
* The plugin in docker container can't display 3D view, please choose 2D view to display the sample and images.

#### Apptainer (Singularity)
If you want to run with server resource, follow [this instruction](./docs/server_setup.md) to setup running on server.

* Download Apptainer image `mousechd-napari.sif` from (Zenodo)[https://zenodo.org/records/14652180] or simply: `wget https://zenodo.org/records/14652180/files/mousechd-napari.sif`
* Run the plugin: 
```
apptainer exec \
    --nv \
    --bind /tmp/.X11-unix:/tmp/.X11-unix \
    --env DISPLAY=$DISPLAY \
    <path/to/mousechd-napari.sif> napari
```

### From code

```bash
conda create -n mousechd_napari python=3.9
conda activate mousechd_napari
pip install "napari[all]"
pip install mousechd-napari
napari
```

## How to use
Please find details instruction in folder [docs](https://github.com/hnguyentt/mousechd-napari/tree/master/docs)
