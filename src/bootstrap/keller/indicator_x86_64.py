from aloofclient import sender
from cruncher import blackwhite
def returnAList(a):
    with open(a,"r") as f:
        s=f.read()
        s=blackwhite(s,"\r\n",False)
        return s

r = returnAList("COMSEED_x86_64")
# print()
import time
for x in r:
    sender(x)
    time.sleep(1)
        # print(d)
