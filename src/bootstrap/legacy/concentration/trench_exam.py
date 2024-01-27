from getFromDill import returnXList
# import pywalk
# check if these things are visible?
# we can determine the shape of these chars?
from storeADill import storeXList
from klean import klean
def virtual(r1,v):
    assert type(v)==int and v>=0
    k = klean(r1)
    # print(k)
    k=list(map(lambda x: x[0],k))
    # print(k)
    # all shit.
    k=list(filter(lambda x: x in [True,False],k))
    # k=list(filter(lambda x: type(x) is bool,k))
    # all shit.
    k=list(map(int,k))
    k=sum(k)
    return k>v
    # what the heck?
# def sumOne(a):
#     if type(a)==dict:
#         return
# # get all values?
r = returnXList("trench")
# r0 = [x for x in r.keys()][0]
r={x:virtual(r[x],0) for x in r.keys()}
p=[x for x in r.keys() if r[x]==False]
storeXList(p,"invisible_0")
# it would be great measurement if used to all unicode chars.
# ok! now use it to do our task!
# r1 = r[r0]
# # print(r1)
# r1 = (1, 2, 3, 4, {"json": [1, 2, 3, 4, [2, 2, 3, 4, [3, 2, 3, 4]]], "nothing":(1, 2, 3, 4, (2, 2, 3, 4))}, (2, 2, 3, 4))
# really strange.
# ca we just preserve the path?
# xrange not defined. modify it!
    # ak(pywalk.walk(node))?
    # iterator?
    # what if we have the list?
    # what the heck?
# alright. problem solved.
# we are removing it.


