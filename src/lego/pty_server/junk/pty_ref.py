from __future__ import unicode_literals

import threading
import pyte
import tornado.ioloop
import tornado.web
import requests
import sys
import errno
import pty
import base64
import os
import time
import subprocess
import traceback
import copy
from select import select


# still lacking basic control. not using pseudo terminal.
LF_CRLF=b"\n"
cols, rows = 80, 25
global_env = copy.deepcopy(os.environ)
global_env["COLUMNS"] = str(cols)
global_env["LINES"] = str(rows)

ended = [False]
maxbark = 1
maxbark_granual = 5
maxterm = 3
maxterm_granual = 5
bark = 0
term = 0
port=8688
def kill(pipe,masters):
    global ended
    try:
        for fd in masters:
            os.close(fd) # no input
        pipe.stdin.close()
        pipe.terminate()
        pipe.kill()
    except:
        print("_____process kill error_____")
        traceback.print_exc()
    finally:
        ended[0]=True
# use os.close.
# cannot close pty. thus keep using the shit.
# but we might need to regroup the whole thing somehow. shall we?
# shall we delete the pty and move on?
# dude, reconstruct the thing.

display = ""
# this means not a single return is initiated.
lag = 0.05
executable = 'bash'

# we should not call the wait function.
# we can log data into vterminal.
#watch_rate = 0.5
screen = pyte.Screen(cols,rows)
stream = pyte.ByteStream(screen)
masters, slaves = zip(pty.openpty(), pty.openpty())
process = subprocess.Popen([executable],env = global_env ,stdout=slaves[0],stderr=slaves[1],stdin=subprocess.PIPE)
# it is not running well.
def read_to_term(masters,slaves,z):
    global display, stream, screen
    for fd in slaves:
        os.close(fd) # no input
    readable = {
        masters[0]: stream, # log separately
        masters[1]: stream
    }
# does that mean anything?
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
#                    print(type(data),dir(data),"datatype")
                    # no data?
                    print("channel",fd)
                    readable[fd].feed(data)
                    display = "\n".join(screen.display)
#    print("process is dead.")
    z[0]=True

t0=threading.Thread(target=read_to_term,args=(masters,slaves,ended))
t0.setDaemon(True)
t0.start()

def barkdog():
    global bark, maxbark_granual
    while True:
        bark = 0
        time.sleep(maxbark_granual)
tb=threading.Thread(target=barkdog,args=())
tb.setDaemon(True)
tb.start()
# specify the env.
def termdog():
    global term, maxterm_granual
    while True:
        term = 0
        time.sleep(maxterm_granual)
tx=threading.Thread(target=termdog,args=())
tx.setDaemon(True)
tx.start()
def watchdog():
    global process, port, bark, maxbark, watch_rate
    #notdead = True
    #while notdead:
    #    pl = process.poll()
    #    print("poll result",pl)
    #    time.sleep(watch_rate)
    process.wait()
    # print("bark")
    bark+=1
    if bark > maxbark:
        # print("max bark exceed.",bark)
        pass
    else:
        requests.get("http://localhost:{}/restart".format(port),stream=False,verify=False,timeout=1)
    # if not, call the handler. use requests.
t1=threading.Thread(target=watchdog,args=())
t1.setDaemon(True)
t1.start()
# what the heck?
# you can set max execution time here. but is it necessary?
class RHandler(tornado.web.RequestHandler):
    def get(self):
        global process, screen, stream, t0, t1, executable, display, term, maxterm, masters, slaves, global_env 
        # print(type(process))
        # print(dir(process))
        term += 1
        if term > maxterm:
            self.write("exceeding max termination quota!\n")
        else:
            kill(process,masters)
            # what if it does not exist?
            # print("process pid",process.pid)
            # print("killing process")
            # os.kill(process.pid,signal.SIGKILL)
            # process.close()
            for x in [process, screen, stream, t0, t1, masters, slaves]:
                # print("deleting")
                del x
            ended[0]=False
            display = "default_refreshed"
            screen = pyte.Screen(cols,rows)
            stream = pyte.ByteStream(screen)
            masters, slaves = zip(pty.openpty(), pty.openpty())
            process = subprocess.Popen([executable],env = global_env ,stdout=slaves[0],stderr=slaves[1],stdin=subprocess.PIPE)
            t0=threading.Thread(target=read_to_term,args=(masters,slaves,ended))
            t0.setDaemon(True)
            t0.start()
            t1=threading.Thread(target=watchdog,args=())
            t1.setDaemon(True)
            t1.start()
# what if it changes the terminal columns? i do not care. just show me.
            self.write("terminal restart!\n")
class IHandler(tornado.web.RequestHandler):
    def get(self):
        global display, process, lag, ended
        # print("type request received.")
        argument = self.get_argument("type",None)
        argumentx = self.get_argument("b64type",None)
        # that is for argument!
        autoreturn = self.get_argument("autoreturn",None) == "true"
        # print("actual argument",[argument],type(argument))
        # string.
# unless it is writable.
        if ended[0]:
            self.write("process is ended.\n")
        elif process.stdin.closed:
            self.write("stdin is closed.\n")
        elif not process.stdin.writable():
            self.write("stdin is not writable.\n")
        elif argument is not None:
            # unicode.
            # may encounter error.
            if autoreturn:
# shall we dispatch it to a thread? therefore we do not need to wait.
                process.stdin.write(argument.encode("utf8")+LF_CRLF)
                process.stdin.flush()
            else:
                process.stdin.write(argument.encode("utf8"))
                process.stdin.flush()
            time.sleep(lag)
# may you adjust this.
            self.write(display)
        elif argumentx is not None:
            # check if correctly formed.
            try:
                arx = base64.b64decode(argumentx)
                # the result is not right.
                # cannot decode here.
                if autoreturn:
                    process.stdin.write(arx+LF_CRLF)
                    process.stdin.flush()
                else:
                    process.stdin.write(arx)
                    process.stdin.flush()
                    # this is not unicode string.
                time.sleep(lag)
                self.write(display)
            except:
                self.write("incorrect format\n")
        else:
            self.write("empty input\n")
            # pass
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global display
        self.write(display)
    def make_app():
        return tornado.web.Application([(r"/display",MainHandler),(r"/restart",RHandler),(r"/input",IHandler)])

app = MainHandler.make_app()
app.listen(port)
# here's the shit.
tornado.ioloop.IOLoop.current().start()
# register handler.
exit()
