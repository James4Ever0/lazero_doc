from getFromDill import returnXList
import random
def choice(s):
    rng=random.SystemRandom()
    return rng.choice(s)
f=returnXList("within")
print(choice(f))
