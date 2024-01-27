import numpy as np
import random
a = np.matrix([[random.random() for x in range(5)] for y in range(5)])
c = np.matrix([[random.random() for x in range(5)] for y in range(5)])
b = np.matrix([[random.random() for x in range(5)] for y in range(5)])
# suppose unknown*c = b, then unknown = b/c
# e*c=b
# e=b*(c**-1)
# # print(e)
# pred=e*c
# print(pred,b)
# it is alright.
# c*e=b
# et*ct=bt
e=(b.T*(c.T**-1)).T
pred=c*e
print(pred,b)
# same shit/