import sys
v=""
for x in sys.stdin:
    v+=x
v = v.split()
v = set(v)
v = " ".join(v)
print(v)
