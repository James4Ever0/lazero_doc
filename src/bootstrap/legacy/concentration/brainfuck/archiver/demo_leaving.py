# demostration on how to store data in neurons.
a=[[None,None] for x in range(100)]
b="hello world"
c="hello world"
for x in range(len(b)):
    if x==0:
        a[x][0]=b[x]
        a[x][1]=b
    else:
        a[x][0]=a[x-1][1][1]
        a[x][1]=a[x-1][1][1:]
        a[x-1][1]=None
    print(a)
a[len(b)-1][1]=None
print(a)