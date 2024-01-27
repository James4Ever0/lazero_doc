import numpy as np

def sigmoid(a):
    return np.matrix((1/(1+np.e**-(np.array(a))))-0.5)
    # this value is a symbol!
a=np.matrix([[0 for x in range(2)] for y in range(2)])
b=sigmoid(a)
print(b)