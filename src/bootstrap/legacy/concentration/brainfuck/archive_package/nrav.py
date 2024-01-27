import numpy as np
import torch
from sub2 import timeout
# n=np.array()
xo = timeout(2)(torch.randn)
# xo=xo((300,300,300,2))
# xo=xo((47,48,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[47, 48, 48, 48] to have 3 channels, but got 48 channels instead
# xo=xo((48,47,48,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 47, 48, 48] to have 3 channels, but got 47 channels instead
# xo=xo((48,48,47,48))
# RuntimeError: Given groups=1, weight of size [18, 3, 3, 3], expected input[48, 48, 47, 48] to have 3 channels, but got 48 channels instead
xo = xo((100, 3))
# print([x for x in dir(xo) if "numpy" in x])
# ["numpy"]
# this is shit.
xo=xo.numpy().ravel()
xo=xo.ravel()
# fuck.
print(xo)
print(xo.shape)