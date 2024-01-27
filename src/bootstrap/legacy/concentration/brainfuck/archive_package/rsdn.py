import torch
# red-lang?
from torch.autograd import Variable
import numpy as np
import pylab as pl
import torch.nn.init as init
# all kinds of bullshit.
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
# you can make it true.
# print(x.shape)
# print(y.shape)
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
    predictions.append(pred.data.numpy().ravel()[0])  # what is this fuck?

# pl.scatter(data_time_steps[:-1],)
# # what is this s?
# pl.scatter(y.data.numpy(),x.data.numpy(),s=90,label="Actual")
# # fucking shit.
# pl.scatter(predictions,x.data.numpy(),label="Predicted")

pl.scatter(data_time_steps[:-1], x.data.numpy(), s=90, label="Actual_P")
pl.scatter(data_time_steps[1:], y.data.numpy(), s=45, label="Actual_F")
# fucking shit.
pl.scatter(data_time_steps[1:], predictions, label="Predicted")
# all fucking twisted code.
pl.legend()
pl.show()
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
