import torch
import torch.nn as nn
import time
# it is not getting any better.
# strange.
# we will check cpu later.
# device = torch.device("cuda")
# total time 113.9896514415741
# ideep, hip, msnpu, mkldnn
# opengl, opencl
# language is a sparse matrix.
# many things are sparse. just wait and see.
device = torch.device("cpu")
# total time 42.38628387451172
# you know, it is not significantly faster.
# middle is for hiddern layer dimension.
n_in, n_h, n_out, batch_size = 10, 5, 1, 10
x = torch.randn(batch_size, n_in)
# is this for verification?
# what if the result is defined in matrix form or some imaginary form?
# just calm down.
# fucking hell.
# wahtever. do it later. always got time to fuck over.
# test the speed first.
y = torch.tensor([[1.0], [0.0], [0.0], [1.0], [1.0],
                  [1.0], [0.0], [0.0], [1.0], [1.0]])
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
model = model.to(device)
x = x.to(device)
y = y.to(device)
t = time.time()
for epoch in range(50000):
    y_pred = model(x)
    print("prediction", y_pred)
    loss = criterion(y_pred, y)
    print("epoch", epoch, "loss", loss, type(loss))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print("total time", time.time()-t)
# it is like a function estimator.
# can we change it dynamically?
# you are fucking with me.
# this time we have less accuracy.
# maybe we can speed it up by reducing it?
# it is just not so accurate.