from sympy import *
import numpy as np
import random
# d=np.exp(1)
# x=symbols("x")
# works. but not for matrix.
b=np.array([[symbols('d{}{}'.format(x,y)) for x in range(6)] for y in range(5)])# <
e=np.e
print(e**b)
# what the fuck?
# this is shit.
# whatever. it is not always perfect.