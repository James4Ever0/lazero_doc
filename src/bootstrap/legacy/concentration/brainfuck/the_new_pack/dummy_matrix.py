import numpy as np
import random
# the so-called machine learning.
# symbolic logic and some common sense.

def loss(a, b):
    c = a-b
    d = c.reshape(-1)
    d = np.mean(abs(d))
    return d
# once you've got a tool, you've got to use it well.
# so what about abstract logic?
# graph, net?
# just hear the wind's blowing.
# cannot change this.
# maybe the sample is too small?
# misplaced shits?
a = np.matrix([[random.random() for x in range(3)] for y in range(5)])
o = np.matrix([random.random() for x in range(5)])
actual = np.matrix([random.random() for x in range(3)])
# # # misplaced shits?
# a = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# o = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# # actual = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# actual = np.matrix([random.random() for x in range(3)])
# b=np.matrix([[random.random()] for y in range(5)])
# very strange.
# what the heck?
# need compare.
c = 0.001
# same shit.
# d = b-a
# how about taking direct approach?
# o*a' = actual
# o*a = pred
# it needs to be square, to get the inverse.
# this is quick.
# e=(actual.T*(o.T**-1)).T
# gen=o*e
# print(gen,actual)
# (pred-actual) = o*a - o*a' = o*(a-a')
# it increases!
# loss_mem = None
# next_op = True
# strange.
# this is a strange approach. all about transformation over matricies.
# just try to get the real shit.
# before that, i've tried a lot of shits.
# matries are all about computations.
# matrix lab.
# # your so-called training.
for x in range(1000000):
    pred=o*a
    # d = o.T*(actual-pred)
    d=o.T*(actual-pred) # what the heck is this shit?
    a += d*c # believe it or not, it's just a number.
    _loss=loss(pred, actual)
    print("loss", _loss)
    # if loss_mem is not None:
    #     if next_op:
    #         a += d*c
    #         _loss = loss(pred, actual)
    #         if _loss >= loss_mem:
    #             next_op = False
    #     else:
    #         a -= d*c
    #         _loss = loss(pred, actual)
    #         if _loss >= loss_mem:
    #             next_op = True
    # else:
    #     a += d*c
    #     _loss = loss(pred, actual)
    # print("loss", _loss)
    # loss_mem = _loss
    # that is very strange.
    # really strange.
# is this my fucking machine learning???
# it is like bruteforcing the human brain!