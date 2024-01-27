import torch
import torch.nn as nn
import time
from pytorch_complex_tensor import ComplexTensor
# import numpy as np
# it is not getting any better.
# strange.
# we will check cpu later.
# device = torch.device("cuda")
# total time 113.9896514415741
# ideep, hip, msnpu, mkldnn
# opengl, opencl
# upper case!
# there's thing called language server!
# also shell server, database server, and finally, nerual network server!
device = torch.device("cpu")
# total time 42.38628387451172
# you know, it is not significantly faster.
# middle is for hiddern layer dimension.
n_in, n_h, n_out, batch_size = 10, 5, 1, 10
# wrong fuckiung def,
x0 = torch.randn(batch_size, n_in).tolist()
x1 = torch.randn(batch_size, n_in).tolist()
# # # print(dir(x1))
# # # print(x1)
# x = torch.randn(batch_size, n_in)
x = ComplexTensor([x0, x1])
# loss=0.07
# really? but how does it directly being applied?
# is this fraud?
######################################
# LOSS MATRIX: UNDER BATCH SIZE 5000 #
# Y \ X    REAL   COMPLEX            #
# REAL     0.19   0.0464             #
# COMPLEX  0.17   0.07               #
######################################
# does this really matter?
# wrong.
# this can still fucking work. i do not know why.
# to list first.
# print(x)
# is this for verification?
# what if the result is defined in matrix form or some imaginary form?
# just calm down.
# fucking hell.
# wahtever. do it later. always got time to fuck over.
# test the speed first.
# y=torch.tensor([ 1. +1.j ,  0. +0.j ,  0. +0.j ,  1. +1.j ,  1. +1.j ,  0.5-0.2j,  -0.2+0.8j, -0.5+0.5j, -0.3-0.1j,  1. +0.1j], dtype=torch.complex64)
# y = ComplexTensor([[1.0, 0.0, 0.0, 1.0, 1.0,
#                   1.0, 0.0, 0.0, 1.0, 1.0],[0.5, -0.2, -0.5, -0.3, 1.0,
#                   -0.2, 0.8, 0.5, -0.1, 0.1]])
# according to the batch size.
y = ComplexTensor([[[1.0], [0.0], [0.0], [1.0], [1.0],
                    [1.0], [0.0], [0.0], [1.0], [1.0]], [[0.5], [-0.2], [-0.5], [-0.3], [1.0],
                                                         [-0.2], [0.8], [0.5], [-0.1], [0.1]]])
# y = torch.tensor([[[1.0], [0.0], [0.0], [1.0], [1.0],
#                     [1.0], [0.0], [0.0], [1.0], [1.0]], [[0.5], [-0.2], [-0.5], [-0.3], [1.0],
#                                                          [-0.2], [0.8], [0.5], [-0.1], [0.1]]])
# the model, is it changeable?
# just by making it different.
# not working though.
model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(),
                      nn.Linear(n_h, n_out), nn.Sigmoid())
# out is five.
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # learning rate
# you always got something to say.
# can we reload it?
# can we use cuda?
# print(model,type(model))
# # you can check it, just for sure.
# always got doc.
# cast it to list then.
# does not support complex datatype.
# we will check it later.
# better print it here.
model = model.to(device)
x = x.to(device)
y = y.to(device)
t = time.time()
# get the params out!
for epoch in range(5000):
    y_pred = model(x)
    # print(y)
    # s=y_pred.tolist()
    # # print(s)
    # y_pred=ComplexTensor(s)
    # print("prediction", y_pred.size())
    # print("target",y.size())
    yz = y.tolist()
    # print("prediction",ComplexTensor(y_pred.tolist()))
    # print("target", y)
    loss = criterion(y_pred, torch.tensor(yz))  # here is the problem.
    # two parts.
    # what the heck?
    print("epoch", epoch, "loss", loss, type(loss))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print("total time", time.time()-t)
meta=list(model.parameters())
print(meta,[type(x) for x in meta])
# does not have complex tensor inside.
# it is like a function estimator.
# can we change it dynamically?
# you are fucking with me.
# this time we have less accuracy.
# maybe we can speed it up by reducing it?
# it is just not so accurate.
# i do not know what is the way to it.