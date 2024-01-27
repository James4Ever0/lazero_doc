import sys
c=0
# so, the missing bit.
y=[]
yk = 0
for x in sys.stdin:
    if c%2==1:
        pass
    else:
        if c == 0:
            pass
        else:
#            l=len(x)
#            if yk>l:
#                yk=l
            y.append(x)
#    print([x])
    c+=1
print(y)
