import torch
import torch.nn as nn
import time
import random
# https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# it is not getting any better.
# strange.
# we will check cpu later.
# device = torch.device("cuda")
# total time 113.9896514415741
# ideep, hip, msnpu, mkldnn
# opengl, opencl
device = torch.device("cuda")
# total time 42.38628387451172
# you know, it is not significantly faster.
# middle is for hiddern layer dimension.
n_in, n_h, n_out, batch_size = 10, 5, 1, 10
# is this for verification?
# what if the result is defined in matrix form or some imaginary form?
# just calm down.
# fucking hell.
# wahtever. do it later. always got time to fuck over.
# test the speed first.


def baseIV():
    # x = torch.randn(batch_size, n_in)
    y = torch.tensor([random.choice([[1.0], [0.0]]) for x in range(10)])
    # x = x.to(device)
    y = y.to(device)
    return y


x = torch.randn(batch_size, n_in)
x = x.to(device)
# the model, is it changeable?
model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(),
                      nn.Linear(n_h, n_out), nn.Sigmoid())
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # learning rate
# you always got something to say.
# can we reload it?
# can we use cuda?
# print(model,type(model))
# # you can check it, just for sure.
# always got doc.
# maybe this is how we stay alert?
# and that's why we need to differentiate.
# there's no way to it.
model = model.to(device)
t = time.time()
for epoch in range(50000):
    y = baseIV()  # very strange.
    y_pred = model(x)
    print("prediction", y_pred)
    loss = criterion(y_pred, y)
    print("epoch", epoch, "loss", loss, type(loss))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print("total time", time.time()-t)
# congratudation! a brand new middle ager!
# it is like a function estimator.
# can we change it dynamically?
# you are fucking with me.
# this time we have less accuracy.
# maybe we can speed it up by reducing it?
# it is just not so accurate.
# the result will never be good.
