#!/usr/bin/env python
'''
listens for a broadcast packet with the string "photo" in it.
then takes a picture, names it with the hostname and timestamp
'''
import time
import socket
import picamera


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udp.bind(('',8000))
print 'BEGIN!'
with picamera.PiCamera() as camera:
    camera.resolution = (2592,1944)
    time.sleep(1)
    while True:
        data, addr = udp.recvfrom(1024)
        print "Got me a packet"
        print data
        # This could be any word or string, allowing you to trigger
        # different things using the same system
        if "photo" in data:
            print "taking a photo"
            serial = data.split("-")
            serial = serial[1]
            camera.capture("{0}_{1}.jpg".format(socket.gethostname(),serial))

