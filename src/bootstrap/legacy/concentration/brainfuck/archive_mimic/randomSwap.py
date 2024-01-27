# schema: position in word. position in the overall paragraph.
# great for the growth of breast?
import copy
import random
def acquire(a):
    with open(a, "r") as f:
        return f.read()
# i have found something interesting. there always be some obsession toward something.
# like the MNIST. clearly it is overused. everyone wants to learn a bit from it.
# it is the obsession.
# it is all about it.
# you can also do dumplicate, vanish.
def getSwap(k,v=5):
    d=copy.copy(k)
    f=range(len(d))
    for x in range(v):
        x0=random.choice(f)
        x1=random.choice(f)
        d[x0],d[x1]= d[x1],d[x0]
    return d

if __name__ == "__main__":
    r=acquire("decompose_0.py")
    r0=r.split("\n")
    r1=getSwap(r0)
    for x in r1:
        print(x)