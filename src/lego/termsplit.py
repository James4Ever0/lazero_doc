import sys
# must be a matrix.
def transform(a):
    x,y = len(a),len(a[0])
    return [[a[z1][z0] for z1 in range(x)] for z0 in range(y)]
#    for x in a:
#        for y in x:
def counter(a):
    return {x:a.count(x) for x in set(a)}
xp = []
xa = []
for x in sys.stdin:
    xa.append(len(x))
    xp.append(x)
# transform.
print("longest",max(xa),"average",sum(xa)/len(xa),"minimum",min(xa))
# so this time do the minimum.
# not too short.
lx = len(xp)
xs = []
for x in xp:
    xs.append(x[:min(xa)])
xs = transform(xs)
xs = [counter(x) for x in xs]
#print(xs)
asm = [" "]
def compare(a,b):
    if len(a)==1:
        return a[0] in b
    else:
        return False

for x in range(len(xs)):
    mx = xs[x]
    # assume some are the spliters.
    md = max([mx[y] for y in mx.keys()])
    my = [y for y in mx.keys() if mx[y] == md]
#    print("standard",lx,"max",mx)
# assume some are meaningful?
    print("column",x,"ratio",md/lx,"spliter",compare(my,asm))
# so analyze the pattern.
#purity indicator.
