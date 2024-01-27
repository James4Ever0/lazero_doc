from getFromDill import returnXList
from storeADill import storeXList
# virtual keyboard?


def scanner(a, x0):
    # type theory is all about law works.
    # trust me. just some lawyers' theory, easy to learn.
    b = ""
    c = []
    for x in a:
        if x not in x0:
            b += x
        else:
            if b != "":
                c.append(b)
                b = ""
    if b != "":
        c.append(b)
        b = ""
    return c


r = returnXList("invisible_0")
f = ""
with open("trench.log", "r") as f0:
    f = f0.read()
f = scanner(f, r)
# with open("trencher.log","w+") as f0:
#     # f=f0.read()
#     for x in f:
#         f0.write(x+"\n")
storeXList({x: False for x in f}, "rockstar")
# immortal internet?
# now, get to it!
# there are non-english word inside.
