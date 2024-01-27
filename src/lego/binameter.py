# some tool to indicate the binary percentage. not absolutely reliable.
import sys
b= b""
for x in sys.stdin.buffer:
    # so there are bytes.
    #print(type(x),len(x))
    b+=x
#print(len(b))
#open("libj.so","wb+").write(b)
# check if this works.
# now do the stuff.
x0=0
# so we try this anyway?
# trying to decode part of the string?
bs = b.split()
bx = sum([len(x) for x in bs])
for x in bs: 
    try:
#        print(type(x),x)
        x.decode()
        x0+=len(x)
    except:
#        print("error decoding")
        pass
# shall also check binary distribution."
# or not.
pr = 1-x0/bx
print("binary percentage", pr)
