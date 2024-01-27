f=None
import sys
sys.path.append("../")
from cruncher import multibw as blackwhite

with open("locate.log","rb") as fs:
    f=fs.read()
    #x="".join([chr(o) for o in range(500)]).encode()
    f=blackwhite(f,b"\n",8,False)
    #f=f.split("\n")
    # bytes are strange.
"""
import random
def choice(s):
    rng=random.SystemRandom()
    return rng.choice(s)
print(choice(f))"""
from storeADill import storeXList
storeXList(f,"within")
# store in a db as a service. get count and acquire one.
