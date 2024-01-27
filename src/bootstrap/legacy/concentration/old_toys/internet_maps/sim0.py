# make set.
from dbM2 import regcheck
# a,b,c,d


def commPat(a, b):
    c = []
    buf = None
    for x in a:
        if buf == None:
            c.append(x == b)
            buf = x
        else:
            if x == buf:
                pass
            else:
                c.append(x == b)
                buf = x
    return c
# what the heck is actually going on?
# why it cannot be done?
# it is sorted, but undone.
# count!
# remember these numbers.
r = regcheck("projects")
r = [x[0] for x in r]
r0 = set(r)
r1 = {x: commPat(r, x) for x in r0}
for x in r1.keys():
    print(x, r1[x],r.count(x))
    print("_____________________SPLITER_____________________")
# what the fuck is going on?