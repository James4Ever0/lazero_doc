import re,sys
import pickle
def path_finder(a):
    for x in range(len(a)):
        if a[x] == "/":
            return a[x:-1]
    return ""

dx = {}
for x in sys.stdin:
    rf = re.findall(r"\d+",x)
    if len(rf)>0:
        s = rf[0]+":"
        e = x.replace(s,"")
        pr = path_finder(e)
        dx.update({rf[0]:pr})
# or use some glue.
pickle.dump(dx,sys.stdout.buffer)
# print(dx)
#        print(pr)
#        print(rf[0])
