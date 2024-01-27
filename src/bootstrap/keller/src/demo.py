import random
#demo=[]
# no right or wrong? five/five?
a=lambda x: x+1
b=lambda x: x-1
c=lambda x: x*2
d=lambda x: x/2
rng=random.SystemRandom()
demo=[a,b,c,d]
while True:
    get=input("enter a number, we'll output some result for you.\n")
    r=rng.choice(demo)(int(get))
    print("reselt:",r)
