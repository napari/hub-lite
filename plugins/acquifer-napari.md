
The acquifer-napari plugin allows loading IM04 dataset directory, as multi-dimensional images in napari.  
Sliders for well, channel, time and Z are automatically rendered when there are more than 1 coordinates along the dimension.  
The plugin uses Dask-Image for efficient data-loading "on request" similar to the VirtualStack in ImageJ.  

## Installation
Via the napari plugin manager : acquifer-napari.
Or with pip : `pip install acquifer-napari`.

Use `pip install -e .` to install in developement mode, so any change in the source code is directly reflected.  
Use `npe2 list` to check that the plugin is correctly installed and visible by napari.  
For instance here, the package defines 1 command, which is a reader.  
One could have more commands, which would be implement other types.   
This should output something like following 
┌──────────────────────────────┬─────────┬──────┬───────────────────────────────────────────────────────────┐
│ Name                         │ Version │ Npe2 │ Contributions                                             │
├──────────────────────────────┼─────────┼──────┼───────────────────────────────────────────────────────────┤
│ acquifer-napari              │ 0.0.1   │ ✅   │ commands (1), readers (1)

The plugin should be installed in an environment with napari installed.  
Napari can be started with the `napari`command in a command prompt with a system wide python installation.  
Once installed, napari can be opened in a IPython interactive session with

```python
>> import napari
>> napari.Viewer()
```

## Configurations
The file `napari.yaml` in `acquifer_napari_plugin` defines what functions of the python package are visible to napari.  
The top level `name` field must be the same than the python package name defined in `setup.cfg`.
It first define a set of commands, which have a custom `id`, and a `python_name`, which is the actual location of the function in the python package (or module).  
Then the napari.yaml has optional subsections `readers`, `writers`, `widget`, to reference some of the commands previously defined, to notify napari that they implemente those standard functions.  
For instance I first define a command myReader pointing to myPackage.myReader, and I reference that command using the id it in the section readers  
See https://napari.org/stable/plugins/first_plugin.html#add-a-napari-yaml-manifest  


## Issues
If you encounter any problems, please [file an issue](https://github.com/Luxendo/acquifer-napari/issues) along with a detailed description.
