import torch
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# hard to find complex parameters.
# plenty of fuck.
import seaborn as sns
import pandas as pd
# %matplotlib inline
import torch
import torch.nn as nn
from torch.autograd import Variable
# this is for jupyter.
# maybe this machine needs some rest?
# yeah, just maybe.


class Lin(nn.Module):
    # TODO: unfinished!
    def __init__(self, input_dim, output_dim):
        # super(Lin,self)
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, s):
        out = self.linear(s)
        return out

    def dump(self):
        return self.linear


m = 2
c = 3
x = np.random.rand(256)
noise = np.random.rand(256)/4
y = x*m+c+noise
df = pd.DataFrame()
df['x'] = x
df['y'] = y
x_train = torch.tensor(x.reshape(-1, 1).astype("float32"))
# they always hide the dimension.
# print(x_train.shape,x.shape)# does not have second dimension.
# hell. then we will only get one fucking neuron.
y_train = torch.tensor(y.reshape(-1, 1).astype("float32"))
# not tensor.
input_dim = x_train.shape[1]
output_dim = y_train.shape[1]
model = Lin(input_dim, output_dim)
criterion = torch.nn.MSELoss()  # anything else?
# device = torch.device("cuda")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
device = torch.device("cpu")
x_train = x_train.to(device)
y_train = y_train.to(device)
model= model.to(device)
# no fucking cache?
# it is sitting still. strange.
# print(x_train)
# remove the thing first.
for epoch in range(5000):
    y_pred = model.forward(x_train)
    # print("prediction", y_pred)
    loss = criterion(y_pred, y_train)
    print("epoch", epoch, "loss", loss, type(loss))
    # optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    # does position matters?
    # does not matter.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
# you know the shape, and the rule.
fwb=list(model.parameters())
print(fwb)
# 2 and 3. correct.
# used to use some other shits.
# you know it will.
# complex tensors always have weird shape.
# print(fwb)
# has random init values.
# print(input_dim,output_dim)
# strange.
# sns.lmplot(x='x',y='y',data=df)
# plt.show()
# what the heck.
# with regression model.
# you always got options.
# leaving this for too damn long will cause I/O error.
# fine. i will buy you a thing.
