from dbM2 import createMain, initial
from basepak import getRange

# format is png.
createMain()


# def verx(a, b):
#     if len(a) == 0:
#         return True
#     else:
#         r = [int(x in b) for x in a]
#         return len(r) == sum(r)
# math won't hurt.

for x in range(11):
    limit = 2**x  # less than this.
    g = getRange(x)
    # initial("projects", g)
    # this is wrong.
    g0 = [(x, a, b, 0) for a, b in g]
    initial("projects", g0)
    g1 = [(x, a, b, 1) for a, b in g if a+1 < limit]
    initial("projects", g1)
    g2 = [(x, a, b, 2) for a, b in g if b+1 < limit]
    initial("projects", g2)
    g3 = [(x, a, b, 3) for a, b in g if ((a+1 < limit) and (b+1 < limit))]
    initial("projects", g3)
    print("configured", x)
