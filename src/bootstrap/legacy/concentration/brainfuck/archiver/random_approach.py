import random
import math
import copy
import statistics
def approach(target,error):
    assert target>0
    assert error>0 and error<0.1
    s=math.ceil(target*2)
    s0=int(s+1)
    s1=list(range(s0))
    s2=[x for x in s1 if x > target]
    s3=[x for x in s1 if x not in s2]
    mean=copy.deepcopy(s1)
    # ep=-error
    e=error*2
    while True:
        m=statistics.mean(mean)
        e=m-target
        # print(m,target,e)
        # print(mean)
        # print(e)
        if abs(e)>error:
            if e>0:
                mean.append(random.choice(s3))
            elif e<0:
                mean.append(random.choice(s2))
        else:
            break
            # return mean
    return mean
# final result is shit.
if __name__ == "__main__":
    # demo.
    # allow error otherwise there's no need to pose this solution.
    target=12.7
    error=0.01
    a=approach(target,error)
    # print(a)
    b=statistics.mean(a)
    print(b)