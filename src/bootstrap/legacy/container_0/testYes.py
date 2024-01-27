# import asyncio
import threading
# import multiprocessing
# import time
# import termios
# import fcntl
# import tempfile
# pretend to be a terminal.
# it can do some harm on you. consider a sandbox for everything.
# {SANDBOX}! -> deepfreeze.
import time
import subprocess
import os
# with threading.Lock():
# write some env to it. both os and popen.
# three fucking python.
# send it into a pseudo terminal like some kind of .js file.
os.environ['TERM'] = 'xterm'
env=os.environ.copy()
# heck!
def run(cmd):
    # await asyncio.sleep(1)
    globlock=True
    # just render it into something else.
    # stdin=tempfile.TemporaryFile("w+b")
    proc = subprocess.Popen(
        cmd,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,env=env)
    # proc.stdin.write(b"junk\n")
    def readline(a,b):
        while globlock:
            buff=a.readline()
            print(b+buff)
    # they seem to copy the same things several times?
    # only one fucking process when using threading.
    p=threading.Thread(target=readline,args=(proc.stdout,b"stdout: "))
    p0=threading.Thread(target=readline,args=(proc.stderr,b"stderr: "))
    # does not share information?
    p.start()
    p0.start()
    # start another shit.
    # read what?
    # when it is dead, it goes crazy. so share the namespace please?
    # not gonna start.
    # ik=5
    # x=["links","elinks","vim","ps","sed"]
    # while ik>0:
    proc.stdin.write(b"yes\n")
    proc.stdin.flush()
    #     ik-=1
    # yes it can be killed.
    # how to receive that signal? share the space please?
    # do it there.
    time.sleep(1)
    print("_____theStop_____")
    # not working for process.
    globlock=False # process have a different namespace though.
    # but working for threads.
    time.sleep(2)
    proc.kill()
    # print(dir(p))
    # p.kill()
    # p.terminate()
    # p0.kill()
    # p0.terminate()
    # p0.n()
    # this works.
    # not inserting shit. fuck me please?
    # does not affect?
    # how comes.
    # set the overall value into something else?
    print("_EOL_")
    # or multiprocessing works the same?
    # stdout, stderr = await proc.communicate()
    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')
# somewhat works.
# how to link to OBSstudio?
if __name__ == "__main__":
    # multiprocessing.freeze_support()
    run('bash')
    print("AHEAD OF TIME")
    # well, you can record things from daily typings.
    # it is all that one machine can receive. replay it if needed.