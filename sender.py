MYPORT = 8000

import sys
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

count = 200
while 1:
    data = "photo-{0}".format(count)
    count = count + 1
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)
    message = raw_input("enter to continue")
    if str(message) == 'q':
        sys.exit()
    print "woo"
