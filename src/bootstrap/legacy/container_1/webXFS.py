from twisted.internet import protocol, reactor
import time
# import sys
# import multiprocessing
import threading
# password is a must here. not kidding.

class MyPP(protocol.ProcessProtocol):
    def connectionMade(self):
        reactor.callLater(1.0, self.foo)

    def foo(self):
        self.transport.write('\033[B'.encode())

    def write(self, a):
        self.transport.write(a)

    def processExited(self, reason):
        print("processExited, status %s" % (reason.value.exitCode,))

    def outReceived(self, data):
        print(data)

    def errReceived(self, data):
        print("errReceived!", data)

if __name__ == "__main__":
    # multiprocessing.freeze_support()
    # while mainthread is alive... -> do the thing.
    pp = MyPP()
    # command = ['screen', '-x']
#    command = ['bash']
    command=['sudo','./dockerXFS.sh']
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
    ik = 5
    pp.write(b"parrot\n")
    time.sleep(1)
    # not working here.
    while ik > 0:
        pp.write(b"ls\n")
        print("[HELLO WORLD]")
        time.sleep(1)
        ik-=1
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
