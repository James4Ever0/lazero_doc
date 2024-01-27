# import os
# os.exec()
# import zmq
import time
# from sub2 import timeout
# import sys
import subprocess
# import commands
# import io
# from io import StringIO
from releas import ins

def think(a):
    return a.split()


# def findout(a):
#     return subprocess.call(("/usr/bin/which "+a).split(),timeout=1)
# construct possible commands. think it is valid.
# believe it or not, just use normal things.
o = ""
with open("commands.log", "r") as f:
    o = f.read()
# print(o)
o = think(o)
# print(o)
# all splitable things.
# while True:
#        msg = socket.recv()
#        print msg
# performing one-shot.
#        socket.send("client message to server1")
# socket.send_string("client message to server2")
#        time.sleep(1)
# asshole.

ok = [" ".join(["mutool", x]) for x in o]

# f=findout("mutool")
# print(f,"out")
# you just won't try?
# there's nothing deep. nothing arbitrary.
# all lies.
# remember, to focus.
xok=[]
for x in ok:
    with open("sample", "r") as f:
        # print(x)
        # sys.stdin=StringIO("hello\n")
        # there is nothing there?
        p = subprocess.Popen(x+"\n", shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE) # no timeout?
        g = p.communicate(input=b"\n\n\n")
        xok.append((time.time(),x,str(g)))
        # k.write("anything\n")
        # sys.stdin.read()
        # something?
        # p.stdin.read()
        # p=subprocess.Popen(x+"\n",shell=True,stderr=subprocess.PIPE,stdin=io.BytesIO(b"stream"))
        # g = p.communicate(input=b"\nnothing\n")
        # what the heck?
        # print(p.communicate())
        # it needs input. how to get it?
        # how to catch that stdin?
        # print(g, type(g))
        # print(g)
    # while True:
    #     out = p.stderr.read(1)
    #     if out == '' and p.poll() != None:
    #         break
    #     if out != '':
    #         sys.stdout.write(str(out))
    #         sys.stdout.flush()
    # y=subprocess.call(x,timeout=1)
    # print(y)
ins("projects",xok)
print("done")
# not working.
# port = "5599"
# context = zmq.Context()
# socket = context.socket(zmq.PAIR)
# socket.connect("tcp://127.0.0.17:%s" % port)
# while True:
#     try:
#         o = timeout(1)(socket.recv_string)()
#         assert o == "heartbeat"
#         for x in ok:
#             socket.send_pyobj(x)
#             time.sleep(0.2)
#     except:
#         print("not sent")
#     print(x) # execute and display?
#     # make sure it is not stuck.
