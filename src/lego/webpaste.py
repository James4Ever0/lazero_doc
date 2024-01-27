import tornado.ioloop
import tornado.web
import uuid
import subprocess
from parse import *
# get a random port somewhere.
#import sys
# cannot find these processes on the OS!
#import threading
#import time
# password is a must here. not kidding.
# called the connection to a process.
# that thing is calling the dynamic shell processor.
#def terminate():
#    time.sleep(0.1)
#    exit()
# just find the right shit.
blob = None
uuid_s = str(uuid.uuid4())
# might have collision.
# we need some predefined things.
class Hello(tornado.web.RequestHandler):
    def get(self):
        global uuid_s
        self.write("hello from server! UUID:{}\n".format(uuid_s))

class Refresh_UUID(tornado.web.RequestHandler):
    # maybe you can consider multiple pasteboard instance on the same server.
    def get(self):
        global uuid_s
        uuid_s = str(uuid.uuid4())
        self.write("UUID refreshed! UUID:{}\n".format(uuid_s))

class Terminate(tornado.web.RequestHandler):
    def get(self):
        global uuid_s
        self.write("terminating webserver. UUID:{}\n".format(uuid_s))
#        print(dir(self))
        self.finish()
        exit()
#        terminate()
        # anyway. just do this.
#        threading.Thread(target=terminate).start()
        # it is not the main thread.

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if blob is None:
            self.write("no data here.\n")
        elif type(blob) == bytes:
            self.write(blob)
        else:
            self.write("internal data error.\n")
    def post(self):
        # you can post things here. relay to 8888.
        sp = self.request.body
        blob = sp
        self.write("message received.\n")
        # do you want to clear the data?
        # pass a function to the place?
        # whatever the link is.
    def make_app():
        return tornado.web.Application([(r"/terminate",Terminate),(r"/uuid",Hello),(r"/refresh_uuid",Refresh_UUID),(r".+",MainHandler),])
if __name__ == "__main__":
    f0 = subprocess.Popen(["python3","ports_chooser.py"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    fa,fb = f0.communicate()
    fa = parse("port {}",fa.decode())
    if fa is not None:
        fa = [x for x in fa]
        if len(fa)==1:
            fa = fa[0]
            try:
                fa = int(fa)
#    print(fa) # great. no shit.
#    print(fa,fb)

                app = MainHandler.make_app()
                app.listen(fa)
    # need the arg.
    # so you are gonna check all ports one by one.
    # of course you can use all ports.
    # check avaliable ports? using utility?
                tornado.ioloop.IOLoop.current().start()
    # we must terminate the thing somehow.
                exit()
            except:
                pass
    # sys.exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?
