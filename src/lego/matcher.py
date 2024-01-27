import re
a = open("candidate.log","r").read()
b = open("pid_matcher.log","r").read().split()
pa = set(b)
r = re.findall(r"\d+",a)
pb = set(r)
#print(dir(pb))
# so we do not know.
ps = pb.intersection(pa)
#print(ps)
ps = [x for x in ps if len(x)>3]
#print(ps)
py = []
for x in ps:
    try:
        ix = int(x)
        py.append(ix)
        print(ix)
    except:
        pass
#print(py)
