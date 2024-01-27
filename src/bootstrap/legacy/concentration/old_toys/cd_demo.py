from endmark import windowEndMarkEx

# almost the same?
# does it really help?
# do we need fuzzy logic?
# shall we group things together?

def pr(a, d):
    b, c = len(a), len(set(a))
    if b == c:
        print(b, c, d)
    else:
        print(b, c)


def chick(a, r):
    pr(windowEndMarkEx(a, r), r)


with open("random_interactive.py", "r") as f:
    g = f.read()
    # check data types.
#    g0=windowEndMarkEx(g,1)
#    pr(g0)
#    g1=windowEndMarkEx(g,5)
#    pr(g1)
    for k in range(int(len(g)**0.5)):
        chick(g, k+1)
