# no such package.
# reversed learning: upside-down RL
# this is how we become responsible: we'd like to take the hit.
import torch
from torch.autograd import Variable
# does this work?
from sub2 import timeout
import torch.nn.functional as F
# ?????
# import functools
# fit-in, fit-out, run.
import numpy as np
# it nearly kills me.
# what the heck is going on?
# what the heck is going on?
def checkFlow(a):
    return a.in_channels, a.out_channels
# what the heck is going on?
# what the heck is going on?
# moduledict? what the heck?
# i'm gonna fuck.
xo = timeout(2)(torch.randn)
# xo=xo((300,300,300,2))
# xo=xo((47,48,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[47, 48, 48, 48] to have 3 channels, but got 48 channels instead
# xo=xo((48,47,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 47, 48, 48] to have 3 channels, but got 47 channels instead
# xo=xo((48,48,47,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 48, 47, 48] to have 3 channels, but got 48 channels instead
xo = xo((100, 3, 48, 48))
# tensorflow will become another battlefield.
# print(dir(xo))
# print(xo)
# strange shit.
# first for sample.
# second for channels.
# this is weird. magic.
# Traceback (most recent call last):
#   File "csdn.py", line 14, in <module>
#     xo=xo((300,300,300,300))
#   File "/root/AGI/lazero/brainfuck/sub2.py", line 28, in wrapper
#     raise ret
# Exception: function [randn] timeout [2 seconds] exceeded!
# this is considered as a problem. major problem.
# xo=torch.randn((18,3,3,3))
# print(xo)
# print(xo.shape)
# need experiment here. what the fuck?
# a=torch.nn.Conv2d(3,18,kernel_size=3,stride=1,padding=1)
a = torch.nn.Conv2d(3, 18, kernel_size=3, stride=4, padding=2)
# you jump too damn far.
# what the heck?
# is it makeup?
# it reduces the dimensions after that?
# a=torch.nn.Conv2d(3,18,kernel_size=7,stride=1,padding=1)
# it matters to the size.
# what about the stride here?
# print(dir(a))
# the computer is really heated.
# if you get some screws bounced off, you will be screwed.
# print(checkFlow(a))
# b=torch.nn.Conv2d(3,18,kernel_size=3,stride=1,padding=1)
b = torch.nn.MaxPool2d(kernel_size=2, stride=(2, 1), padding=0)
# it is for different rows. the stride.
# DIFFERENT ROWS!
# just how about three dimentional or n-dimentional shit?
# print(checkFlow(b))
# print(dir(b))
# try arbitrary data?
# i am bad at math.
a.__name__ = "arbitrary"
b.__name__ = "arbitrary"
# AttributeError: 'Conv2d' object has no attribute '__name__'
# fucking hell.
# i do not trust you guys.
z = timeout(2)(a)
z = z(xo)
x = timeout(2)(F.relu)(z)
# always have endless errors.
print(x.shape)
# what the heck?
# second shit: 3 -> 18
x = timeout(2)(b)(x)
print(x.shape)
xd=x.shape[1:]
print(xd)
# y0 = eval("*".join([str(y) for y in x.shape[1:]]))
# fucking hell.
# y0=functools.reduce(lambda x,y:x*y,x.shape[1:])
# really strange.
y0=np.array(xd).prod()
print(y0)
# this is no exception.
x = x.view(-1, y0)
# print(x.shape)
z0=torch.nn.Linear(y0,64)
z0.__name__ = "arbitrary"
# internal logic applies.
x= timeout(2)(z0)(x)
x= timeout(2)(F.relu)(x) # why different names?
z1=torch.nn.Linear(64,10)
z1.__name__= "arbitrary"
x= timeout(2)(z1)(x)
# print(x)
print(x.shape)
# that is one-hot vector.
# it marks my machine.
# put the training later on.
# time to pause.
# either you work to death or computer.
# fuck.
# the third and forth shit -> cut half.
# you even want 4 dimensional shit?
# what the heck?
# print(a.shape)??
# ['__annotations__', '__call__', '__class__', '__constants__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_apply', '_backward_hooks', '_buffers', '_conv_forward', '_forward_hooks', '_forward_pre_hooks', '_get_name', '_load_from_state_dict', '_load_state_dict_pre_hooks', '_modules', '_named_members', '_padding_repeated_twice', '_parameters', '_register_load_state_dict_pre_hook', '_register_state_dict_hook', '_replicate_for_data_parallel', '_save_to_state_dict', '_slow_forward', '_state_dict_hooks', '_version', 'add_module', 'apply', 'bfloat16', 'bias', 'buffers', 'children', 'cpu', 'cuda', 'dilation', 'double', 'dump_patches', 'eval', 'extra_repr', 'float', 'forward', 'groups', 'half', 'in_channels', 'kernel_size', 'load_state_dict', 'modules', 'named_buffers', 'named_children', 'named_modules', 'named_parameters', 'out_channels', 'output_padding', 'padding', 'padding_mode', 'parameters', 'register_backward_hook', 'register_buffer', 'register_forward_hook', 'register_forward_pre_hook', 'register_parameter', 'requires_grad_', 'reset_parameters', 'share_memory', 'state_dict', 'stride', 'to', 'train', 'training', 'transposed', 'type', 'weight', 'zero_grad']
# class smpC(torch.nn.Module):
#     def __init__(self):
#         super().__init__()
#         # man i got shit!
#         # yes then you create shit for us!
#         # in and out.
#         self.conv1=torch.nn.Conv2d(3,18,kernel_size=3,stride=1,padding=1)
#         # immediately after?
#         self.pool=torch.nn.MaxPool2d(kernel_size=2,stride=2,padding=0)
#         # how to calculate the feature?
#         self.fc1=torch.nn.Linear()