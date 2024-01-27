import torch
import torch.nn as nn
import time
import random
# it is not getting any better.
# strange.
# googledrivedownloader, llvmlite, numba, plyfile, isodate, rdflib, imagecodecs, tifffile, PyWavelets, imageio, scikit-image, torch-geometric
# Successfully installed PyWavelets-1.1.1 googledrivedownloader-0.4 imagecodecs-2020.2.18 imageio-2.8.0 isodate-0.6.0 llvmlite-0.32.1 numba-0.49.1 plyfile-0.7.2 rdflib-5.0.0 scikit-image-0.17.2 tifffile-2020.5.11 torch-geometric-1.4.3
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
# there is autokeras, but no need to worry.
# just be patient.
# you could implement some highlighter. npm.

def baseIV():
    x = torch.randn(batch_size, n_in)
    # y = torch.tensor([random.choice([[1.0], [0.0]]) for x in  range(10)])
    x = x.to(device)
    # y = y.to(device)
    return x


# the model, is it changeable?
model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(),
                      nn.Linear(n_h, n_out), nn.Sigmoid())
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # learning rate
# you always got something to say.
# can we reload it?
# can we use cuda?
# print(model,type(model))
y = torch.tensor([[1.0], [0.0], [0.0], [1.0], [1.0],
                  [1.0], [0.0], [0.0], [1.0], [1.0]])
# # you can check it, just for sure.
y = y.to(device)
# always got doc.
# fucking hell. we cannot develop any abstraction from it.
model = model.to(device)
t = time.time()
for epoch in range(50000):
    x = baseIV()  # very strange.
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
# it sounds stupid, but i have to try it out.