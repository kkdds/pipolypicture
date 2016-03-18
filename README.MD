# PiPollyPicture

PiPollyPicture is a way of coordinating multiple RaspberryPi on the same network.

# Requirements

* Python
* a local network
* Pi Camera Module
* A minimum of two pis

## How does it work

This Repo contains two python scripts, `sender.py` and `listen.py`. It uses UDP broadcast sockets to make node discovery simple

## Usage:

On all the client nodes, ssh in an run `python listener.py`

on the trigger machine run `python sender.py`

Every time you hit enter, you'll send out a broadcast packet that will trigger each listener to take a photo. The First photo will be taken at roughly the same time. Whilst the photo is saving you are dependent on SD card speed. 


