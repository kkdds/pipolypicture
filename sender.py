#!/usr/bin/env python
'''
This sends out a broadcast packet with the word "photo" and
an incrementing number
'''
import sys
import time
import socket

MYPORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Change this number to stop accidentally writing 
# previous images
count = 200
while 1:
    data = "photo-{0}".format(count)
    count = count + 1
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)
    message = raw_input("enter to take picture, q to quit:")
    if str(message) == 'q':
        sys.exit()
    print "woo"
