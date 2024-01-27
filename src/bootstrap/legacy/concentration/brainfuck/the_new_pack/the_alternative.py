import torch.nn.init as init
import torch
from confirm_shape import get_writings
# import
# red-lang?
# we just want the machine to feel the difference.
import random
from torch.autograd import Variable
# no neural network.
actual, o = get_writings()
# one-hot.
# device = torch.device("cuda")
# all the same.
# cannot use cuda this time, don't know why.


def one_hotter_R(bm):
    r = [0 for x in range(len(bm))]
    # r[bm.index(am)] = 1
    r[random.choice(range(len(r)))] = 1
    return r


# holy shit! infinite neural networks!
# we have even changed the input!
epochs = 500
hotter = list(sorted(set(actual.reshape(-1).tolist())))
dtype = torch.FloatTensor
# just take 100 inputs.
# gonna first change the output.
# input_size, hidden_size, output_size = 7, 6, 1
n_in, n_h, n_out, batch_size = o.shape[1], 25, 10, o.shape[0]
lr = 0.01
# _lr = 0.01
lry = 0.1
# lrx = 0.001
# we're gonna change this. using alternative thing?
# x = Variable(torch.Tensor(o.tolist()).type(dtype), requires_grad=True)
# faster when this is on.
x = Variable(torch.Tensor(o.tolist()).type(dtype), requires_grad=False)
# primary problem: too damn many grads.
# what about some chained net? suppose some long evil shitty chained conv nets, need for concrete GPU cards to perform the task.
y = torch.autograd.Variable(torch.Tensor(
    [one_hotter_R(hotter) for x0 in actual.tolist()]).type(dtype), requires_grad=True)
# x = Variable(torch.Tensor(o.tolist())[
#              :100, :].type(dtype), requires_grad=False)
# y = torch.autograd.Variable(torch.Tensor([one_hotter_R(hotter) for x0 in actual.tolist()])[
#                             :100, :], requires_grad=True)  # this one is dummy data
# it is getting shit.
w1 = torch.FloatTensor(n_h, n_in).type(dtype)
init.normal_(w1, 0.0, 0.4)
# standard_deviation for second.
# do not know the range.
w1 = torch.autograd.Variable(w1, requires_grad=True)
w2 = torch.FloatTensor(n_out, n_h).type(dtype)
# fucking stat.
# never mind, just train it.
# LOAD THEM ALL.
# cuda has higher error rate.
init.normal_(w2, 0.0, 0.3)
w2 = torch.autograd.Variable(w2, requires_grad=True)
# optimizer_x = torch.optim.SGD([x], lr=lrx) # this is very slow.
# optimizer_y = torch.optim.SGD([y], lr=lry)
# # we should not use optim.
# # just how the fuck does it work?
# # it is about 10000 samples.
# optimizer_w = torch.optim.SGD([w1, w2], lr=_lr)
# not working at all.
# optimizer_w2 = torch.optim.SGD(w2, lr=_lr)
# you can create another thing.
# learning rate
# x = x.to(device)
# y = y.to(device)
# w1 = w1.to(device)
# w2 = w2.to(device)
# # different tricks.
# you are making your net into nuts.


def forward(input, w1m, w2m):
    # same as my process.
    # i do the same.
    # xh = torch.cat((input, context_state), 1)
    # input not right.
    # print(input.shape,w1.shape,w2.shape)
    i = w1m.mm(input)
    # print(i)
    context_state = torch.tanh(i)
    out = w2m.mm(context_state)
    return out


for i in range(epochs):
    total_loss = 0
    # context_state = Variable(torch.zeros(
    #     (1, hidden_size)).type(dtype), requires_grad=True)
    # # cleared at first.
    for j in range(x.size(0)):
        input_ = x[j, :].reshape(-1, 1)
        target = y[j, :].reshape(-1, 1)
        # print(input_.shape,target.shape)
        pred = forward(input_, w1, w2)
        # loss = (pred-target).pow(2+0.1j).sum()
        # not working.
        # consider some complex tensors?
        loss = (pred-target).pow(2).sum()
        # loss of context?
        # we alter this.
        # i know that minus sign.
        # it is going down, but not very fast.
        total_loss += loss  # overall thing.
        # optimizer_x.zero_grad()
        # optimizer_y.zero_grad()
        # optimizer_w.zero_grad()
        # optimizer_w2.zero_grad()
        loss.backward()  # add gradient to it?
        # optimizer_w.step()
        # gonna check.
        # if j%100 == 0:
        #     print("sample",j)
        # # optimizer_w2.step()
    # # loss.backward()
    # optimizer_x.step()
    # optimizer_y.step()
    # optimizer_x.zero_grad()
    # optimizer_y.zero_grad()
    # # not changing?
        # # this is crazy.
        w1.data -= lr*w1.grad.data  # would you print it?
        w2.data -= lr*w2.grad.data
        # working?
        # you are like some crazy mathematician, cannot limit the form of the thing.
        # is this transformer? or likely be?
        w1.grad.data.zero_()
        w2.grad.data.zero_()
    y.data -= lry*y.grad.data
    # better use some method to change this thing, instead of just adding things up.
    y.grad.data.zero_()
        # does that count?
    # y.data -= lry*y.grad.data
    # y.grad.data.zero_()
    # sometimes, i think i need to take a look at it, see if it is independent gradient.
        # it is been reduced, much better than that fucking optimizer.
        # x.grad.data.zero_()  # is this going to work anyway?
        # x.data -= lrx*x.grad.data
        # # cannot using cuda?
        # # not going to work. it is going to be killed.
        # using cuda instead?
        # we'll use optim.
        # let me suppose, it is because the variable dependency chain is too damn long.
        # not even once.
        # /usr/local/lib/python3.8/dist-packages/torch/tensor.py:746: UserWarning: The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad attribute won't be populated during autograd.backward(). If you indeed want the gradient for a non-leaf Tensor, use .retain_grad() on the non-leaf Tensor. If you access the non-leaf Tensor by mistake, make sure you access the leaf Tensor instead. See github.com/pytorch/pytorch/pull/30531 for more informations.
#   warnings.warn("The .grad attribute of a Tensor that is not a leaf Tensor is being accessed. Its .grad "
        # what the heck?
        # context_state = Variable(context_state.data)
        # how about not printing?
    # if i % 10 == 0:
    print("epoch", i, "total_loss", total_loss)
# can we try them all?
# i do not know whether this is the correct answer.
# maybe we just established some sort of agreement.
# this is crazy.
