import sys
import os
import threading
import subprocess
import uuid
import time
import traceback
import base64
from select import select
# shall use uuid as a separator. in case of confusion?
# shall we?
WATCH_DOG=5
MIN_INTERVAL=0.1
uid = str(uuid.uuid4()).encode()
arx = sys.argv
#print(arx)
arx = arx[1:]
sys.stdout.buffer.write(b"UUID"+uid+b"\n")
sys.stdout.buffer.flush()
# if the thing is going on right.
# we should accept stdin.
if len(arx) == 0:
    sys.stdout.buffer.write(b"ERROR_NOARGS"+uid+b"\n")
    sys.stdout.buffer.flush()
    exit(1)
else:
    sys.stdout.buffer.write(b"BEGIN_EXEC"+uid+b"\n")
    sys.stdout.buffer.flush()
# use the protocol?
#os.system()
def wr_out(x):
    return b"STDOUT"+uid+base64.encodebytes(x)
def wr_err(x):
    return b"STDERR"+uid+base64.encodebytes(x)
def rout(p,z):
    readable = {
        p.stdout.fileno(): sys.stdout.buffer, # log separately
        p.stderr.fileno(): sys.stdout.buffer,
    }
    rm = 2
    translator = {p.stdout.fileno():wr_out,p.stderr.fileno():wr_err}
    while rm > 0:
        for fd in select(readable, [], [])[0]:
            data = os.read(fd, 1024) # read available
            if not data: # EOF
                # del what?
                rm -= 1
                #del readable[fd]
            else: 
                readable[fd].write(translator[fd](data))
                readable[fd].flush()
    z[0]=True
    # ended.
def dog(z):
    time.sleep(WATCH_DOG)
    z[0]=True
NORMAL=0
try:
    ended = [False]
    pipe = subprocess.Popen(["stdbuf","-oL","-e0"]+arx,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# normally we keep this error.
    t_out = threading.Thread(target=rout,args=(pipe,ended))
    t_err = threading.Thread(target=dog,args=(ended,))
    t_out.setDaemon(True)
    t_err.setDaemon(True)
    t_out.start()
    t_err.start()
    while True:
        time.sleep(MIN_INTERVAL)
        if ended[0]:
# well, you can send the signal.
            sys.stdout.buffer.write(b"PROGRAM_EXIT"+uid+b"\n")
            sys.stdout.buffer.flush()
            break
except:
    NORMAL=1
    fmt = traceback.format_exc()
    sys.stdout.buffer.write(b"INTERNAL_ERROR"+uid+base64.encodebytes(fmt.encode()))
    sys.stdout.buffer.flush()
#    exit(1)
# well, if the problem is only about stdout or flushing, that's fine.
exit(NORMAL)
# so what is the main thread anyway.
# just a watch dog?
    # but this time we've had an agreement, right?
    # you shall do some remote handler now. dispatch the agent on such a port.
