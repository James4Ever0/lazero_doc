from twisted.internet import protocol, reactor
import time
# import multiprocessing
import threading
from dbM import up, createMain
import re, os
from pairserver import onceMore
# password is a must here. not kidding.
if "Monitor.db" not in os.listdir("."):
    createMain()
pid=0
class MyPP(protocol.ProcessProtocol):
    global pid
    def connectionMade(self):
        reactor.callLater(1.0, self.foo)

    def foo(self):
        self.transport.write('\033[B'.encode())

    def write(self, a):
        self.transport.write(a)

    def processExited(self, reason):
        print("processExited, status %s" % (reason.value.exitCode,))

    def outReceived(self, data):
        global pid
        print(data)
        if pid==0:
            #print("received:",data[:4])
            if data[:4]==b"\x00\xd0\x9d\x09":
                pid=int(re.findall(r'[0-9]+',data[4:].decode())[0])
                #print("pid:",pid)
        # it is here.
        up(time.time(),pid,data,{"type":"output"})

    def errReceived(self, data):
        global pid
        print(data)
        up(time.time(),pid,data,{"type":"error"})

if __name__ == "__main__":
    # multiprocessing.freeze_support()
    # while mainthread is alive... -> do the thing.
    pp = MyPP()
    # command = ['screen', '-x']
#    command = ['bash']
    command=['./launcher_x86_64_linux.sh']
    # does this work in WINDOWS?
    def theFunc(a):
        a.run()
    reactor.spawnProcess(pp, command[0], command, {'TERM': 'xterm'}, usePTY=True)
    # print("{MIDDLE}")
    p =threading.Thread(target=theFunc,args=(reactor,))
    p.setDaemon(True) # the whole shit.
    # print("{AHEAD}")
    # start after the set.
    # somehow.
    # all dead here. not even better than JS.
    p.start() # not RUN!
    # what the heck?
    # with TIMESTAMP.
    # print("{OF}")
    ik = 10
    #pp.write(b"parrot\n")
    time.sleep(1)
    # not working here.
    while ik>0:
        inp=onceMore()
        print(inp)
        pp.write(inp)
        up(time.time(),pid,inp,{"type":"input"})
        time.sleep(.500)
        ik-=1
    pp.write(b"exit\n")
    time.sleep(1)
    # this will provide the debug info.
    pp.write(b"ls\n")
    time.sleep(1)
    # this will not work.
    # p.kill()
    # print(dir(p))
    # quit()
    print("__EOL__")
    # sys.exit()
    exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?
# do we need a separate process?
# this is running fine.
# but how to communicate?
# somehow worked.
