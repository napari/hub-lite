Microscope control plugin for Napari via Python Microscope.

Current development stage is whatever comes before alpha and "proof of
concept".

To test
-------

I haven't had access to real hardware yet, so this has all been
developed with simulated devices.

1. Start the device server with simulated devices.

    a. Create a device server configuration file like so::

        import microscope
        from microscope.device_server import device
        from microscope.simulators import (
            SimulatedCamera,
            SimulatedFilterWheel,
            SimulatedLightSource,
            SimulatedStage,
        )

        DEVICES = [
            device(SimulatedCamera, "localhost", 8000,),
            device(SimulatedLightSource, "localhost", 8001),
            device(SimulatedFilterWheel, "localhost", 8002,
                   {"positions": 6}),
            device(SimulatedStage, "localhost", 8003,
                   {"limits": {"X": microscope.AxisLimits(0, 25000),
                               "Y": microscope.AxisLimits(0, 12000)}}),
        ]

    b. Start the device server (ensure port 8000-8003 are unused)::

        $ device-server path-to-microscope-config.py

2. Start napari

3. Plugins > Add Dock Widget > microscope: MicroscopeWidget

4. Connect to the camera:

    a. On the new widget, click on the "Add device" button.

    b. Enter the camera URI `PYRO:SimulatedCamera@localhost:8000`

5. Tick the `Enabled` box to enable the camera and then press the
"Snap" button.

6. A random values image will appear displayed on the napari viewer.
Keep pressing the "Snap" button to get new images.  The top left
corner of the image is the simulated image number.

7. Connect to the other simulated devices.  Their URIs are:

    a. PYRO:SimulatedLightSource@localhost:8001
    b. PYRO:SimulatedFilterWheel@localhost:8002
    c. PYRO:SimulatedStage@localhost:8003

8. Changing the other simulated devices, doesn't really do much (but
does change state of the devices, as can be seen in the logs)


Test with stage aware camera
----------------------------

This is pretty much the same as before but one can use a large RGB
TIFF (histology samples are perfect) to simulate a camera that returns
subsections of the image file based on the simulated stage position.

For quick example, try::

    wget https://zenodo.org/record/1445489/files/B0002.tif

And use the following device server configuration file::

    from microscope.device_server import device
    from microscope.simulators.stage_aware_camera import simulated_setup_from_image

    DEVICES = [
        device(simulated_setup_from_image, "localhost", 8000,
               conf={"filepath": "B0002.tif"}),
    ]

The URI for the devices will be::

    PYRO:camera@localhost:8000
    PYRO:filterwheel@localhost:8000
    PYRO:stage@localhost:8000

Changing the filterwheel changes which channel from the image is
returned.  Changing the stage coordinates changes the image that is
returned (but beware of the corners, pixels outside the image size are
not handled yet and will give an error).
