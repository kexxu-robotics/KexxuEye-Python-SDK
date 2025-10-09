![Tests](https://github.com/kexxu-robotics/KexxuEye-Python-SDK/actions/workflows/ci.yml/badge.svg)
[![Coverage](https://codecov.io/gh/kexxu-robotics/KexxuEye-Python-SDK/branch/main/graph/badge.svg)](https://codecov.io/gh/kexxu-robotics/KexxuEye-Python-SDK)


KexxuEye Python SDK
===

To be used with the Kexxu eye tracking glasses available on [kexxu.com](https://kexxu.com).

Install with (python>=3.7):

```
pip install git+https://github.com/kexxu-robotics/KexxuEye-Python-SDK.git
```

![Kexxu Eye Tracking Glasses](images/eyetracker.webp)

### Documentation at:

[kexxu-robotics.github.io/KexxuEye-Python-SDK/](https://kexxu-robotics.github.io/KexxuEye-Python-SDK/)


## The basics of connecting to the Eye Tracker

The Kexxu eye tracker has a device id, like:

```
openeye-v4-abcd1234
```

It can be found on a local network with its hostname built op from its device id, like:

```
openeye-v4-abcd1234.local
```

Real time eye tracking data is available over MQTT.

The list of recordings and the files of the recordings of the device are available on http.



# This SDK is still work in progress, check the progress here


### File format

- [x] Convert from OpenEye Datafile to x,y pixel locations in video

- [ ] Convert pixel locations back into OpenEye Datafile

- [ ] Read specific event types in the Datafile

- [ ] Add specific event types in the Datafile

### Connectivity

- [ ] Try to find device by DeviceID

- [ ] Get current wifi network

- [ ] Scan for device on all ip addresses

- [ ] Send event to device


### Actions

- [ ] Start preview

- [ ] Stop preview

- [ ] Start recording

- [ ] Stop recording


### Calibration

- [ ] Get conf

- [ ] Get eye location

- [ ] Move tracking window

- [ ] Move tracking cross offset


### Recordings

- [ ] List recordings

- [ ] Show disk space

- [ ] Delete recording



### WIFI

- [ ] scanned networks

- [ ] saved networks

- [ ] add network

- [ ] remove network


