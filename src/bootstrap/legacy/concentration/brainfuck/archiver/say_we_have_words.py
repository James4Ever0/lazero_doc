# we have a list of parameters!
# they have work to do!
# to emulate the brain? no need. we just need a cyber brain!
# swap the values when you want to.
# keep, swap, eliminate
# random actions, not taking account.
import random
import copy
import numpy as np
import time
# really strange artifact.
# so we does not need random swapping.
# it is not random at all.
# we can even create value specific rules!
# REMEMBER: SPARSE IS BETTER THAN DENSE.

def still(a, b):
    return a, b


def keep(a, b):
    return a, a


def swap(a, b):
    return b, a


def eliminate(a, b):
    return b, b


def init(a):
    b = np.array([[random.choice([True, False])
                   for y in range(10)] for x in range(10)])
    return b


def train(a):  # you can print the difference.
    # time.sleep(0.1)
    b = copy.copy(a)
    for x in range(len(a)**2):
        xa = random.choice(list(range(len(a))))
        # for y in range(len(a)):
        # nonsense = x+y
        xb = random.choice(list(range(len(a))))
        ax = random.choice(list(range(len(a))))
        # for y in range(len(a)):
        # nonsense = x+y
        bx = random.choice(list(range(len(a))))
        f = random.choice([keep, swap, eliminate, still])
        # f = random.choice([keep, swap])
        # f = random.choice([swap, eliminate])
        # f = random.choice([keep, eliminate])
        # why it is the same?
        # it is about swapping column.
        # you will get the same column.
        # print(b[xa], b[xb], f.__name__)
        b[xa][ax], b[xb][bx] = f(b[xa][ax], b[xb][bx])
        # print(b[xa], b[xb])
    if np.all(a == b):
        print("same")
    else:
        print("not same")
    return b


# always remains Equilibrium.
# i need to check it. what the heck is going on.
    # a0=list(range(len(a)))
    # a1=copy.copy(a0)
    # for x in a0:
    #     xa=random.choice(list(range(len(a1))))
    #     a2=copy.copy(a0)
    #     for
# that is another alternative.
epoch = 20000
dim = 10
i = init(dim)
for x in range(epoch):
    # print(i.sum())
    print(i)
    i = train(i)
print("final")
print(i)
# stack the whole thing into a meta-block?
# but it can only interact with meta-blocks.
# so what the heck? must need outside stimulation?
# we can calculagte how long we can maintain the state.
# this is for one-dimension.
# [[False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]
#  [False  True False False  True False  True False False  True]]
# [[False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]
#  [False  True  True False  True False  True  True  True False]]
# for two-dimentional swap.
# [[ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True  True  True]]