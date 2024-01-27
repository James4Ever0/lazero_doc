# computer gets stuck.
import subprocess
import sys
# from sub2 import timeout
x = "timeout 0.001 yes"
# what the fuck?
p = subprocess.Popen
p = p(x+"\n", shell=True, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE, stdin=subprocess.PIPE)
g = None
try:
    # g = p.communicate(input=b'\n\n\n', timeout=1)
    g= p.communicate(input=b'\n\n\n')
except:
    print("error")
print(sys.getsizeof(g[0]), type(g))
# this is not right?
# but nothing here?
# heck man, this gets stuck in no time.
# it is stuck.
# great.
# many difference here? I mean windows and more?
# SIGKILL, SIGTERM????
# I want to send those shits.
