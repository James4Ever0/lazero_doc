import traceback
a=[]
b=lambda x: "".join(x)
a.append(b)
c=lambda x: x*2
a.append(c)
d=lambda x:"hello "+x+" world"
a.append(d)
sample=1
for x in a:
    try:
        z=x(sample)
        print("result:",z,type(z))
    except:
        e= traceback.format_exc()
        print(e)
# it is not always aboout numbers.
# this emulates my fucking brain.
# only a fraction of it.
# ONLY A FUCKING FRACTION!