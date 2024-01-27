import random
#demo=[]
# no right or wrong? five/five?
rng=random.SystemRandom()
a=lambda x: x+x
b=lambda x: x[0]
c=lambda x: rng.choice(list(x))
d=lambda x: x[-1]
demo=[a,b,c,d]
while True:
    get=input("enter a string, we'll output some result for you.\n")
    r=rng.choice(demo)(get)
    print("reselt:",r)
