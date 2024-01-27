# here we go, fake code.
p=[chr(x) for x in range(500)]
import random
k=""
for x in range(500*500):
    k+=random.SystemRandom().choice(p)
print(k)
