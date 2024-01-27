import sys
import pty
import os
import threading
import subprocess
import uuid
import errno
import time
import traceback
from select import select
import base64
# shall use uuid as a separator. in case of confusion?
# shall we?
# check for terminal later.
WATCH_DOG=5
MIN_INTERVAL=0.1
# what is this then?
# we can solder it.
uid = str(uuid.uuid4()).encode()
arx = sys.argv
#print(arx)
arx = arx[1:]
sys.stdout.buffer.write(b"UUID"+uid+b"\n")
sys.stdout.buffer.flush()
# if the thing is going on right.
# we should accept stdin.
# does not grarantee these packages will contain the same amount of information.
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
def rout(masters,slaves,z):
    for fd in slaves:
        os.close(fd) # no input
# why the fuck it does not work?
    readable = {
        masters[0]: sys.stdout.buffer, # log separately
        masters[1]: sys.stderr.buffer,
    }
    translator = {masters[0]:wr_out,masters[1]:wr_err}
    rdb = 2
    while rdb>0:
        for fd in select(readable, [], [])[0]:
            try:
                data = os.read(fd, 1024) # read available
            except OSError as e:
                if e.errno != errno.EIO:
                    raise #XXX cleanup
                rdb-=1
                # so it is good.
                #del readable[fd] # EIO means EOF on some systems
            else:
                if not data: # EOF
                    rdb-=1
                    # it does not end properly.
#                    del readable[fd]
                else:
                    print("feeding back.",fd)
                    readable[fd].write(translator[fd](data))
                    readable[fd].flush()
    z[0]=True
    # ended.
def dog(z):
    time.sleep(WATCH_DOG)
    z[0]=True
def rin(pipe):
    t=5
    while t>0 and pipe.stdin.writable() and not pipe.stdin.closed:
        # check if writable.
        print("writable?",pipe.stdin.writable())
        print("closed?",pipe.stdin.closed)
        pipe.stdin.write(b"whoami\n")
        pipe.stdin.flush()
        time.sleep(1)
        t-=1
    # may not succeed.
    pipe.stdin.close()
    pipe.terminate()
    pipe.kill()
#    print(dir(pipe.stdin))
    # write and flush.
#    print(dir(pipe),type(pipe))
NORMAL=0
masters, slaves = zip(pty.openpty(), pty.openpty())
try:
    ended = [False]
    pipe = subprocess.Popen(arx,stdout=slaves[0],stderr=slaves[1],stdin=subprocess.PIPE)
# normally we keep this error.
    t_in = threading.Thread(target=rin,args=(pipe,))
    # it seems that stdout is not being read.
    t_out = threading.Thread(target=rout,args=(masters,slaves,ended))
    t_err = threading.Thread(target=dog,args=(ended,))
    t_in.setDaemon(True)
    t_out.setDaemon(True)
    t_err.setDaemon(True)
    t_in.start()
    t_out.start()
    t_err.start()
# not blocking, of course.
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
finally:
    for fd in masters:
        os.close(fd)
    for fd in slaves:
        try:
            os.close(fd)
        except:
            pass
#    exit(1)
exit(NORMAL)
# so what is the main thread anyway.
# just a watch dog?
    # but this time we've had an agreement, right?
    # you shall do some remote handler now. dispatch the agent on such a port.
