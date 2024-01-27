from __future__ import unicode_literals
from winpty import PTY
# this module is exclusive for windows. to port to linux there should be extra steps.
# i mean, android.
# hey! do not run this shit outside of sandbox, unless you want to get me killed.
import threading
# import wmi
import os
import pyte
import tornado.ioloop
import tornado.web
import requests
import base64
maxbark = 1
maxbark_granual = 5
maxterm = 3
maxterm_granual = 5
bark = 0
term = 0
# give the maxbark.
# interruption isn't working.
# import signal
# shall consider ddos prevension?
# import sys
# WMI = wmi.WMI()
port=8788
def kill(pid):
    # do it elsewhere.
    # global WMI
    os.system("taskkill /F /PID {}".format(pid))
    # better execute it in pypy or else.
    # this is shit. check source code from reactos.
    # or better not to use it. since it requires dll loading?
    # for x in WMI.Win32_Process():
    #     if x.processid == pid:
    #         print("killing process",pid)
    #         x.Terminate()
    # print("killing done")
    # too long.
# def signal_handler(signal, frame):
#     print('You pressed Ctrl+C!')
#     # sys.exit(0)
#     exit(0)
# signal.signal(signal.SIGINT, signal_handler)
display = ""
lag = 0.05
executable = u'C:\windows\system32\cmd.exe'
cols, rows = 80, 25
import time
watch_rate = 0.5
screen = pyte.Screen(cols,rows)
stream = pyte.ByteStream(screen)
process = PTY(cols, rows)
process.spawn(executable)
def read_to_term():
    global display, stream, screen
    # read a global list?
    # you can start another server. not quite like terminal. like execution shell.
    noerr=True
    while noerr:
        try:
            reading=process.read(blocking=True)
    # will raise error if not good.
            stream.feed(reading)
            display = "\n".join(screen.display)
        except:
            noerr = False
            break
t0=threading.Thread(target=read_to_term,args=())
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
def termdog():
    global term, maxterm_granual
    while True:
        term = 0
        time.sleep(maxterm_granual)
tx=threading.Thread(target=termdog,args=())
tx.setDaemon(True)
tx.start()
def watchdog():
    global process, watch_rate, port, bark, maxbark
    alive=True
    while alive:
        alive = process.isalive()
        time.sleep(watch_rate)
    # print("bark")
    bark+=1
    if bark >= maxbark:
        # print("max bark exceed.",bark)
        pass
    else:
        requests.get("http://localhost:{}/restart".format(port),stream=False,verify=False,timeout=1)
    # if not, call the handler. use requests.
t1=threading.Thread(target=watchdog,args=())
t1.setDaemon(True)
t1.start()

class RHandler(tornado.web.RequestHandler):
    def get(self):
        global process, screen, stream, t0, t1, executable, display, term, maxterm
        # print(type(process))
        # print(dir(process))
        term += 1
        if term >= maxterm:
            self.write("exceeding max termination quota!\n")
        else:
            kill(process.pid)
            # print("process pid",process.pid)
            # print("killing process")
            # os.kill(process.pid,signal.SIGKILL)
            # process.close()
            for x in [process, screen, stream, t0, t1]:
                # print("deleting")
                del x
            display = ""
            screen = pyte.Screen(cols,rows)
            stream = pyte.ByteStream(screen)
            process = PTY(cols, rows)
            process.spawn(executable)
            t0=threading.Thread(target=read_to_term,args=())
            t0.setDaemon(True)
            t0.start()
            t1=threading.Thread(target=watchdog,args=())
            t1.setDaemon(True)
            t1.start()
            self.write("terminal restart!\n")
class IHandler(tornado.web.RequestHandler):
    def get(self):
        global display, process, lag
        # print("type request received.")
        argument = self.get_argument("type",None)
        argumentx = self.get_argument("b64type",None)
        # that is for argument!
        autoreturn = self.get_argument("autoreturn",None) == "true"
        # print("actual argument",[argument],type(argument))
        # string.
        if argument is not None:
            # unicode.
            # may encounter error.
            if autoreturn:
                process.write(u'{}\r\n'.format(argument))
            else:
                process.write(u'{}'.format(argument))
            time.sleep(lag)
            self.write(display)
        elif argumentx is not None:
            # check if correctly formed.
            try:
                arx = base64.b64decode(argumentx)
                # the result is not right.
                # cannot decode here.
                if autoreturn:
                    process.write(arx+b'\r\n',raw=True)
                else:
                    process.write(arx,raw=True)
                    # this is not unicode string.
                time.sleep(lag)
                self.write(display)
            except:
                self.write("incorrect format")
                # pass
                # D:\Programs\Python\Python36\lib\site-packages\winpty\winpty_wrapper.py
        else:
            self.write("empty input")
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
