from endmark import windowEndMarkEx


def createFrozen(a):
    return [frozenset([x for x in y]) for y in a]


def pr(a, d):
    b, c = len(a), len(set(a))
    if b == c:
        print(b, c, d)
    else:
        print(b, c)
# code can be simple or complex. redirect the result to somewhere else?
# you think you might save some time over this.

def chick(a, r):
    pr(windowEndMarkEx(a, r), r)

# def pr(a):
#     print(len(a),len(set(createFrozen(a))))

# def chick(a,r):
#     pr(windowEndMarkEx(a,r))
# you are fucking nuts.

with open("random_interactive.py", "r") as f:
    g = f.read()
    # check data types.
#    g0=windowEndMarkEx(g,1)
#    pr(g0)
#    g1=windowEndMarkEx(g,5)
#    pr(g1)
    for k in range(int(len(g)**0.5)):
        chick(g, k+1)
