# i do not know shit about bradient descent.
import torch
import torch.nn as nn
import numpy as np
from confirm_shape import get_writings
import time
import random
device = torch.device("cuda")
# total time 42.38628387451172
# you know, it is not significantly faster.
# middle is for hiddern layer dimension.
actual, o = get_writings()
# one-hot.
hotter = list(sorted(set(actual.reshape(-1).tolist())))
n_in, n_h, n_out, batch_size = o.shape[1], 25, 10, o.shape[0]


def one_hotter(am, bm):
    r = [0 for x in range(len(bm))]
    r[bm.index(am)] = 1
    return r

def one_hotter_R(bm):
    r = [0 for x in range(len(bm))]
    # r[bm.index(am)] = 1
    r[random.choice(range(len(r)))]=1
    return r

# one extra recommendation: when not importable, release this thing to another category: unknown.
# and when shape problem occurs, raise the exception.
def dec_one(cm, bm):
    return bm[cm.index(1)]
# i know the principles. i just hate to manually check all the shits.
# how about some free-grad?
model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(),
                      nn.Linear(n_h, n_out), nn.Sigmoid())
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # learning rate
x = torch.Tensor(o.tolist())[:100,:]
# y = torch.Tensor([one_hotter(x0[0],hotter) for x0 in actual.tolist()])[:100,:]
y = torch.Tensor([one_hotter_R(hotter) for x0 in actual.tolist()])[:100,:] # this one is dummy data
print(x.shape,y.shape)
# we cannot set parameter here.
# print(y)
# but no avaliable optimizer.
# can we use the same thing?
# at least the sample has to be 20.
# contain all 20 categories.
# teaching the wrong thing?
# this random thing is not as good as previous thing.
# still got high error rate.
# there tends to be a difference here.
# i think one should also consider taking the derivative of the target, to reduce the overall loss rate.
# cause it is only the source material that is immutable.
# but do you really think the source is immutable? well, we can change the source too.
# and that's how the magic happens. all we need is some kind of agreement.
y = y.to(device)
x = x.to(device)
model = model.to(device)
t = time.time()
for epoch in range(500):
    # y = baseIV()  # very strange.
    y_pred = model(x)
    # print("prediction", y_pred)
    loss = criterion(y_pred, y)
    print("loss",loss)
    # print("epoch", epoch, "loss", loss, type(loss))
    optimizer.zero_grad() # what are those two?
    loss.backward() # to initialize the state. clear all grad.
    optimizer.step() # what are those two?
    # to add some grad to the thing. alright. nothing new.
    # the callback function: check whether the optimization is useful.
print("total time", time.time()-t)
# 0.07 versus 0.03, and that's the difference.
# false answers tends to have shitty loss rate.
# trying to get the answer?
# use some metalearning models?