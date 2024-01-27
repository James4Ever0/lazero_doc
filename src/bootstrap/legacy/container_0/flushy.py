import subprocess
# import tempfile
from subprocess import PIPE
import threading
import time

def runnable(console):
    # console.stdin.write(b"samejunkhere\n")
    # not running shit.
    while True:
        console.stdin.write(b"ls\n")
        console.stdin.flush()
        time.sleep(1)
        print("FROM STDIN.")
    # cannot write again.
# give up on this total utter crap.
def readable(console):
    # cannot read shit.
    # able to peek, but unable to read.
    while True:
        print(console.stdout.peek())
        print("_STDOUT_")
        time.sleep(1)
# stdout=tempfile.TemporaryFile("w+b")
# stderr=tempfile.TemporaryFile("w+b")
# so this is the hackish way to do the job.
console=subprocess.Popen(["bash"],stdin=PIPE,stderr=PIPE,stdout=PIPE)

# console.stdin.write(b"ls\n")
# console.stdin.flush()
thread = threading.Thread(target=runnable,args=(console,))
# console.wait()
thread.start()
thread0 = threading.Thread(target=readable,args=(console,))
# console.wait()
# does not share same shit?
thread0.start()
print("remainder")
# try java instead.
# # print(console.stdout.peek())
# # cannot even peek shit.
# print(console.stdout.peek())
# print("__________________SPLITER__________________")
# console.stdin.write(b"junkfilewhatever\n")
# console.stdin.flush()
# # cannot read lines.
# # cannot use other shits?
# # maybe EOF found.
# print(dir(console.stderr.raw))
# print(console.stderr.raw.readall())
# do it in another thread?
# you can try it.
# print(console.stderr.peek())
# # print(dir(console.stderr))
# console.stdout.seek(len(console.stdout.peek()))
# # here we go again.
# # can only peek once?
# # # cannot read shit.
# # console.stdout.read()
# # print("reach there")
# # console.stderr.read()
# # # cannot do again?
# print("reach here")
# console.stdin.write(b"echo hello world\n")
# console.stdin.flush()
# # console.wait()
# # print(console.stdout.peek())
# print(console.stdout.peek())
# console.stdin.write(b"junkfilewherever\n")
# console.stdin.flush()
# print(console.stderr.peek())