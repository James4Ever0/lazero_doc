from unicode_tensor import chrTens, recv, sayless
import torch
# red-lang?
from torch.autograd import Variable
# import numpy as np
# import pylab as pl
import torch.nn.init as init


def getBin(a):
    with open(a, "r") as f:
        return f.read()  # k=getBin("Monitor.db")

# you have to read this?
device = torch.device("cuda")
# it is so easy, you suppose?
# must be done in a universial way.
# usually utf-8
# different type def? just a joke. man do not be too damn serious to this shit.
# is it a brute-force program?
# you try to predict this?
index = getBin("/media/root/Seagate1000/adobe_references/after_effects.txt")
data = chrTens(index[:400])
print("length of this context:", data.shape[0])
# not even working to this step.
# does this model supports unicode?
# for x in i
# all kinds of bullshit.
dtype = torch.FloatTensor
input_size = data.shape[1]
hidden_size, output_size = int(input_size**0.7), input_size
input_size += hidden_size
epochs = 100
# what is that?
# seq_length = 20  # what the fuck?
lr = 0.01
# nothing learned.
# data_time_steps = np.linspace(2, 10, seq_length+1)
# print(data_time_steps)
# not a rng.
# strange conversion.
# # u use sin!
# data = np.sin(data_time_steps)
# data.resize((seq_length+1, 1))
# print(data.shape)
x = Variable(torch.Tensor(data[:-1]).type(dtype), requires_grad=False)
y = Variable(torch.Tensor(data[1:]).type(dtype), requires_grad=False)
# # you can make it true.
# print(x.shape)
# print(y.shape)
x.to(device)
y.to(device)

# mismatched thing.
w1 = torch.FloatTensor(input_size, hidden_size).type(dtype)
init.normal_(w1, 0.0, 0.4)
# standard_deviation for second.
w1 = torch.autograd.Variable(w1, requires_grad=True)
# w2=torch.
w2 = torch.FloatTensor(hidden_size, output_size).type(dtype)
# fucking stat.
init.normal_(w2, 0.0, 0.3)
w2 = torch.autograd.Variable(w2, requires_grad=True)

w1.to(device)
w2.to(device)
# shit. man what the heck?

def forward(input, context_state, w1, w2):
    # same as my process.
    # i do the same.
    xh = torch.cat((input, context_state), 1)
    context_state = torch.tanh(xh.mm(w1))
    out = context_state.mm(w2)
    return (out, context_state)


for i in range(epochs):
    total_loss = 0
    context_state = Variable(torch.zeros(
        (1, hidden_size)).type(dtype), requires_grad=True)
    # cleared at first.
    for j in range(x.size(0)):
        input_ = x[j:(j+1)]
        target = y[j:(j+1)]
        (pred, context_state) = forward(input_, context_state, w1, w2)
        # loss = (pred-target).pow(2+0.1j).sum()
        # not working.
        # consider some complex tensors?
        loss = (pred-target).pow(2).sum()
        # loss of context?
        # we alter this.
        total_loss += loss
        loss.backward()  # add gradient to it?
        w1.data -= lr*w1.grad.data  # would you print it?
        w2.data -= lr*w2.grad.data
        w1.grad.data.zero_()
        w2.grad.data.zero_()
        context_state = Variable(context_state.data)
    if i % 10 == 0:
        print("epoch", i, "loss", loss, type(loss))

context_state = Variable(torch.zeros(
    (1, hidden_size)).type(dtype), requires_grad=False)
predictions = []

for i in range(x.size(0)):
    input = x[i:i+1]
    (pred, context_state) = forward(input, context_state, w1, w2)
    # not moving?
    context_state = context_state  # what the heck?
    predictions.append(pred.data.numpy().reshape(-1).tolist())  # what is this fuck?
# heck?
# print(torch.Tensor(predictions).shape)
# pl.scatter(data_time_steps[:-1],)
# # what is this s?
# pl.scatter(y.data.numpy(),x.data.numpy(),s=90,label="Actual")
# # fucking shit.
# pl.scatter(predictions,x.data.numpy(),label="Predicted")
# data_time_steps = list(range(400))
# print(len(data_time_steps),x.shape)
print("original:",recv(x))
print("fos:",recv(y))
print("sayless:",sayless(predictions))
# print()
# we can return the shape.
# pl.scatter(data_time_steps[:-1], x.data.numpy(), s=90, label="Actual_P")
# pl.scatter(data_time_steps[1:], y.data.numpy(), s=45, label="Actual_F")
# # fucking shit.
# pl.scatter(data_time_steps[1:], predictions, label="Predicted")
# # all fucking twisted code.
# pl.legend()
# pl.show()
# fucking hell.
# numpy.ndarray.ravel = ravel(...)
# a.ravel([order])
# Return a flattened array.
# Refer to `numpy.ravel` for full documentation.
# See Also
# --------
# numpy.ravel : equivalent function
# holy shit.
# chain rule.
# don't you need to discover more shits?
# what the heck is this?
# remember, imitate, repeat.
# what is this?
# print(w1)
