import torch
import numpy as np
from torch.autograd import Variable
import torch.nn.init as init
dtype = torch.FloatTensor
input_size, hidden_size, output_size = 7, 6, 1
epochs = 300
seq_length = 20
lr = 0.1
data_time_steps = np.linspace(2, 10, seq_length+1)
# print(data_time_steps)
# not a rng.
# strange conversion.
# u use sin!
data = np.sin(data_time_steps)
data.resize((seq_length+1, 1))
# print(data.shape)
x = Variable(torch.Tensor(data[:-1]).type(dtype), requires_grad=False)
y = Variable(torch.Tensor(data[1:]).type(dtype), requires_grad=False)
# print(x.shape)
# print(y.shape)
# mismatched thing.
w1 = torch.FloatTensor(input_size, hidden_size).type(dtype)
w1 = Variable(w1, requires_grad=True)
init.normal_(w1, 0.0, 0.4)
# w1.backward()
# w1=w1.mm(w1.T)
# w1=sum(w1)
pred = w1
# target=np.sin(w1*2)
target = Variable(torch.FloatTensor(np.sin(w1.detach().numpy())).type(dtype))
# it sums all shit up.
loss = (pred-target).pow(2).sum()/2
# w1.backward()
loss.backward()
# do it implicitly.
# fucking hell.
# what the heck?
# print(w1.shape)
# 2 dims.
# w1.grad.data.zero_()
wx = w1.grad.data
print(wx)
