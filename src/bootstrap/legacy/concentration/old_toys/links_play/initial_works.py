from dbM import initial
from getFromDill import returnXList
import re

def xygen(x,y):
    x0=re.findall(r'^[^_]+',x)[0]
    y0=re.findall(r'[^/]+$',y)[0]
    return (x0,y0,y)

r=returnXList("rock")
# print(r)
f=[]
for x in r.keys():
    for y in r[x]:
        z=xygen(x,y)
        # print(z)
        f.append(z)
initial("projects",f)
print("DONE!")