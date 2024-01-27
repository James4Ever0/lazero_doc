import random, sys
x0=[]
for x in sys.stdin:
    x0+=x.split()
if len(x0)==0:
    print("no avaliable candidate")
else:
    r=random.choice(x0)
    print(r)
