# it is all ahout directing some input toward some same outout.
# purposefully
import numpy as np
import random
# all disqualified shit. which is great.
def nonsense(a):
    return [np.array([[random.choice([True, False]) for y in range(10)] for x in range(10)]) for x in range(a)]


def same_nonsense(x, a):
    return [x for y in range(a)]


def flat(a):
    return [x for y in a for x in y]

a = [5, 4, 3, 2, 1]
d = list(reversed(a))
nons = [np.array([[random.choice([True, False]) for y in range(10)]
                  for x in range(10)]) for z in range(len(a))]
nons = [same_nonsense(nons[x], d[x]) for x in range(len(a))]
nd=[nonsense(x) for x in a]
nons,nd=flat(nons),flat(nd)
nx=zip(nons,nd)
for z,f in nx:
    print(z)
    print("match")
    print(f)
    print("######################################################################")