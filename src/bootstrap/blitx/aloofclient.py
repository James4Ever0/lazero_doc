import zmq
import random
import sys
import time
# from sub2 import timeout

port = "5757"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.setsockopt(zmq.LINGER, 0)
# this works. not blocking.
socket.connect("tcp://127.0.0.7:%s" % port)
#while True:
#        msg = socket.recv()
#        print msg
# performing one-shot.
#        socket.send("client message to server1")
# fuck.
# for the latter.
send_string = socket.send_string
# send_string = timeout(1)(socket.send_string)
# send_string(input("Enter the command:\r\n"))
def sender(a):
    send_string(a)
# cannot send shit.
# will stuck if no receive. switch to non-block mode here?
#        time.sleep(1)
# asshole.
# WTF?
# just to send one single string.

