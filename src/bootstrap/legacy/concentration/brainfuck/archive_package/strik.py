import torch
from sub2 import timeout
xo=timeout(2)(torch.randn)
# xo=xo((300,300,300,2))
# xo=xo((47,48,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[47, 48, 48, 48] to have 3 channels, but got 48 channels instead
# xo=xo((48,47,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 47, 48, 48] to have 3 channels, but got 47 channels instead
# xo=xo((48,48,47,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 48, 47, 48] to have 3 channels, but got 48 channels instead
xo=xo((100,3,48,48))
# xo=xo.stride()
# print(dir(xo))
# this is used when it is flatterned.
print(type(xo))
# print(xo.shape)
# print(type(xo),xo)
    # Stride is the jump necessary to go from one element to the next one in the
    # specified dimension :attr:`dim`. A tuple of all strides is returned when no
    # argument is passed in. Otherwise, an integer value is returned as the stride in
    # the particular dimension :attr:`dim`.