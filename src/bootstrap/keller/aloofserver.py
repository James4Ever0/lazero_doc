import zmq
import random
import sys
import time

port = "5757"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.7:%s" % port)
while True:
#        socket.send_string("Server message to client3")
# what the fuck is this?
    msg = (socket.recv_string()+"\r\n").encode()
    print(msg)
    # will it stuck?
    # print(type(msg),msg)
        # this is fuck.
#        time.sleep(1)
# we'll receive it.
