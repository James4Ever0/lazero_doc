import numpy as np
import random
a= np.matrix([[random.random() for x in range(5)] for y in range(5)])
b= np.matrix([[random.random() for x in range(5)] for y in range(5)])
print(b/a)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(a.T*b)
# what the heck?