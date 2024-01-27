import numpy as np

s=np.random.randint(low=0, high=500, size=500*500)
d="".join([chr(x) for x in s])
print(d)
