# sample to perform a truth table. linear and more.
import random
import numpy as np
# a=[random.choice([True,False]) for x in range(10)]
# a=np.array([[x==y for x in a] for y in a])
# nothing about perceptions here. all about matrix.
a=np.array([[random.choice([True,False])  for y in range(10)] for x in range(10)])
print("is it a cat?")
print(a)