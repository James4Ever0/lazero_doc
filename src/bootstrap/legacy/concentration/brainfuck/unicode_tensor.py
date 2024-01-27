import torch
import copy


def callMe(a, b):
    c = copy.deepcopy(a)
    c[b] = 1
    return c


def blockMe(a):
    return a.index(1)
# man this is not hard.

def asshole(a):
    return a.index(max(a))

def chrTens(a):
    # how about reducing the size?
    # mini rnn? so cute???
    # interact????
    d = [ord(x) for x in a]
    ops = max(list(set(d)))+1
    c = [0 for x in range(ops)]
    return torch.Tensor([callMe(c, x) for x in d])
# how to shrink model?
# never mind.
def recv(a):
    return "".join([chr(blockMe(x)) for x in a.tolist()])

def sayless(a):
    return "".join([chr(asshole(x)) for x in a])