import networkx as nx
import torch
import numpy as np
import random

def returnAdj():
    n = nx.read_gpickle("noneTheLess.gpickle")
    d = nx.to_numpy_array(n)
    # can we really load this thing?
    return torch.FloatTensor(d)
# not so good!
# but we need to change the feature and the test set, and that will get the chance of winning.

def returnLab(a, b=5):
    k = list(range(b))
    return torch.LongTensor([random.choice(k) for x in range(a)])
# this lable is not good.

def returnRandomFeature(a, b=100, c=0.5):
    k = np.linspace(0, 1, 100)
    return torch.FloatTensor([[int(random.choice(k) > c) for y in range(b)] for x in range(a)])


def returnProp(a, b=0.1, c=0.3):
    assert b > 0 and c > b and c < 1
    x_, y_ = int(b*a), int(c*a)
    d = range(0, x_)
    e = range(x_, y_)
    f = range(y_, a)
    return list(map(lambda x: torch.LongTensor(list(x)), [d, e, f]))


def collection():
    f = returnAdj()
    e = f.shape[0]
    return f, returnRandomFeature(e), returnLab(e), *returnProp(e)
# print(d)
# print(d.shape)
# def returnSliceIndex()
# not bad?
# d=returnAdj()
# t=torch.LongTensor(d)
# print(t)
# print(t.shape,type(t))
# 49,49
# this is freaky.
# so social things are just some kind of fucking staying put?
# it is just useless, but it is still computable.
# along with your useless data, all computable and trainable.
# so how to process the data?
# print(n,type(n))
# print(dir(n))
# p=n.nodes()
# directed graph.
# first, get the matrix.
# p=n.edges()
# for x in p:
    # print(x)
