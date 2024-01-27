import numpy as np
r=[1,2,3,4,3,2,1]
r=np.array(r)
for x in range(3):
    print(x,np.diff(r,n=x))
