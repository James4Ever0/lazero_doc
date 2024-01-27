# import asyncio
import threading
# import time
# import termios
# import fcntl
# import tempfile
import time
import subprocess
def run(cmd):
    # await asyncio.sleep(1)
    # stdin=tempfile.TemporaryFile("w+b")
    proc = subprocess.Popen(
        cmd,stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    # proc.stdin.write(b"junk\n")
    def readline(a,b):
        while True:
            buff=a.readline()
            print(b+buff)
    threading.Thread(target=readline,args=(proc.stdout,b"stdout: ")).start()
    threading.Thread(target=readline,args=(proc.stderr,b"stderr: ")).start()
    # start another shit.
    # read what?
    # when it is dead, it goes crazy. so share the namespace please?
    ik=5
    # how to pretend to be a terminal?
    x=["links","elinks","vim","ps","sed"]
    while ik>0:
        proc.stdin.write(x[ik-1].encode()+b"\n")
        proc.stdin.flush()
        ik-=1
        time.sleep(1)
    # ik=5
    # while ik>0:
    #     proc.stdin.write(b"this is junk.\n")
    #     proc.stdin.flush()
    #     ik-=1
    #     time.sleep(1)
    proc.kill()
    print("_EOL_")
    # or multiprocessing works the same?
    # stdout, stderr = await proc.communicate()
    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')

run('bash')
print("AHEAD OF TIME")