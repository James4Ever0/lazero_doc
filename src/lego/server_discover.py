import sys
from parse import *
px = None
ps = {}
for x in sys.stdin:
#    print("original",x)
    pr = parse("info from {}",x)
    try:
        if pr is not None:
#            print(type(pr),dir(pr))
            pr = [x for x in pr]
#            print(pr)
            if len(pr)==1:
                pr = int(pr[0])
#            print(pr)
        # nope.
                px = pr
                ps.update({px:[]})
        else:
            if px is not None:
                ps[px].append(x)
    except:
#        if px is not None:
#            ps[px].append(x)
        pass
#print(ps)
# so this is a dict.
#py = {}
# check the uuid format?
for x in ps.keys():
    xn = ps[x]
    for y in xn:
        p = parse("hello from server! UUID:{}",y)
        if p is not None:
            p = [x for x in p]
            if len(p)==1:
#                print(p[0])
                print(x)
#                py.update({x:p[0]})
#print(py)
# you are gonna print the thing out.
    # this is the working area.
#    print(pr)
