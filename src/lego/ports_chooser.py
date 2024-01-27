UNIX_LIKE=True
# turn this off to get touch under 8000. if root. just saying.
import os
os.system("./check_ports.sh")
a = open("ports.log").read().split()
#print(a)
# this is the real network. the FS network. the RAM network. the turing machine.
a = [int(x) for x in a]
import random
f=None
# can we use port 0?
if UNIX_LIKE:
    f = [x for x in range(8000,65536)]
else:
    f = [x for x in range(1,65536)]
f = list(filter(lambda x: x not in a,f))
if len(f)==0:
    print("no port avaliable.")
else:
    r = random.choice(f)
    print("port", r)
    # zero is restricted. don't know why.
    # could use unix socket actually. but again, not CS.
