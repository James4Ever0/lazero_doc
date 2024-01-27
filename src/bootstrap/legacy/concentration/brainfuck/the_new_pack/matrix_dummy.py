import numpy as np
import random
# the so-called machine learning.
# symbolic logic and some common sense.
from confirm_shape import get_writings

# you know that your code sucks.
def loss(a, b):
    c = a-b
    d = c.reshape(-1)
    d = np.mean(abs(d))
    return d
# you see the shit? huh? that's how you do the fuck!
# you should avoid math. it is not really the part.
# yes, so does your machine.
# once you've got a tool, you've got to use it well.
# so what about abstract logic?
# graph, net?
# just hear the wind's blowing.
# cannot change this.
# maybe the sample is too small?
# misplaced shits?
# get some random output?


# sample = 50
# o = np.matrix([[random.random() for x in range(5)] for z in range(sample)])
actual, o = get_writings()
sample = o.shape[0]
print(o.shape, actual.shape)
hotter = list(sorted(set(actual.reshape(-1).tolist())))
dim_x, dim_y = o.shape[1], len(hotter)
a = np.matrix([[(-0.5+random.random())/255/255/255/255 /
                255 for x in range(dim_y)] for y in range(dim_x)])
# f=np.matrix([[random.random() for x in range(450)] for y in range(10000)])
# g=np.matrix([[random.random() for x in range(dim_y)] for y in range(450)])
# actual = np.matrix([[random.random() for x in range(3)]
# for z in range(sample)])
# # # misplaced shits?
# a = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# o = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# # actual = np.matrix([[random.random() for x in range(3)] for y in range(3)])
# actual = np.matrix([random.random() for x in range(3)])
# b=np.matrix([[random.random()] for y in range(5)])
# very strange.


def one_hotter(am, bm):
    r = [0 for x in range(len(bm))]
    r[bm.index(am)] = 1
    return np.matrix(r)


def dec_one(cm, bm):
    return bm[cm.index(1)]


# what the heck?
# need compare.
# not working. the loss is as high as shit.
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
#       pred0 -> pred1 -> pred2                        pred1*d+pred*g=actual
#  o  *a      *f       *g       cmp: actual            pred0*(d0+f)=actual0
#      cmp:actual1  cmp:actual0 d       pred1.T*(actual-pred2) o*(d1+a)=actual1
# next_op = True                                      actual0*g=actual
# strange. actual0*g/g=actual/g
# this is a strange approach. all about transformation over matricies.
# just try to get the real shit.
# before that, i've tried a lot of shits.
# matries are all about computations.
# matrix lab.
# # your so-called training.
# call it specialized.
# one-hot vector.
for r in range(1):
    for x in range(20):
        # this shit is simply not working.
        # abandon ship!
        # for x in range(1):
        # random number, not going down.
        orange = np.matrix(o[r])
        actual_orange = one_hotter(actual[r], hotter)
        # print(orange.shape,actual_orange.shape)
        pred0 = orange*a
        # pred1=pred0*f
        # pred2=pred1*g
        _loss = loss(pred0, actual)
        # d = o.T*(actual-pred)
        # print(pred0.shape, pred1.shape, pred2.shape)
        # (1, 3) (1, 5) (1, 3)
        # print(a.shape, f.shape, g.shape)
    # (5, 3) (3, 5) (5, 3)
        # what the heck?
        # welcome! this shit is fucking horrible.
        # d=pred1.T*(actual_orange-pred2)  # what the heck is this shit?
        # # print(pred1.T.shape,pred2.shape)
        # # print(d.shape,g.shape)
        # # solve these two values.
        # # print(pred0.T.shape,(pred1*d).shape)
        # # actual0=actual*(g**-1)
        # # it is not going to work.
        # # it is raw data.
        # # is that some sort of compression? compress data altogether?
        # # and yet reusable.
        # actual0=actual_orange*g.T
        # # print(actual0.shape)
        # # this is fucking crazy.
        # # print(actual0.shape,pred1.shape)
        # # this is fucked.
        # d0=pred0.T*(actual0-pred1)
        # actual1=actual0*f.T
        # print("#########################################")
        # print(actual1.shape)
        # of course matlab has some neural networks.
        d1 = orange.T*(actual_orange-pred0)
        # CONSIDER SOME MATH?
        # print(d.shape,d0.shape,d1.shape)
        # this is shit.
        # g += d*c   # wtf
        # f += d0*c
        a += d1*c
        # this is not going to work.
        # you are really funny.
        # print(d.shape,d0.shape,d1.shape)
        # what the fuck!
        # e=
        # this is incredibly horrible. i'm gonna test this shit on mnist?
        # fucking works! what the fucking heck?
        # print(pred1.T.shape,pred2.shape)
        # print(d.shape)
        # print(g.shape)
        # # (5,1), (1,3)
        # fg=actual/g
        # very strange.
        # # print(fg.shape)
        # g += d*c  # believe it or not, it's just a number.
        # # this is not right.
        # print(pred0.shape,d.shape)
        # # print(pred0.T,d)
        # e =pred2*d*pred0.T
        # print(e.shape,f.shape,d.shape)
        # f += e*c
        # f0 = o*e.T
        # a += f0*c
        # # this has an error.
        # #
        # print(f0.shape,e.shape,d.shape)
        # why you do not have loss?
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
