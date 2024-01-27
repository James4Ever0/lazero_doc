import re
# /sys/fs/cgroup to find it.
def readFile(a):
    with open(a,"r") as f:
        return f.read()

def splitlines(a):
    return a.split("\n")

def verifier(a,b):
    for c in b:
        if c in a:
            return a
    return

def checker(a,b):
    return list(filter(lambda x: x!=None,[verifier(c,b) for c in a]))

def reader(a):
    custom=["is not set","=y","=m"]
    return checker(splitlines(readFile(a)),custom)

def classifier(a):
    custom=["=y","=m"]
    for c in custom:
        if c in a:
            return(a.replace(c,""),True)
    return (a.replace("is not set","")[2:-1],False)

def batcher(a):
    return [classifier(b) for b in a]

def unifier(a):
    u={"True":[],"False":[]}
    for b in a:
        if b[1]:
            u["True"].append(b[0])
        else:
            u["False"].append(b[0])
    u["True"]=list(set(u["True"]))
    u["False"]=list(set(u["False"]))
    return u

def compare(a,b):
    a0,a1=a["True"],a["False"]
    b0,b1=b["True"],b["False"] # b is the standard.
    # check the difference?
#    u={"Possible":[],"Missing"[]}
    u=[]
    for c0 in b0:
        if c0 not in a0:
#            u["Missing"].append(c0)
            if c0 in a1:
                u.append((c0,True)) # possible.
            else:
                u.append((c0,False))
    return u


fileSet={"android":"config","kali":"config-5.6.0-kali1-amd64"}

f0=reader(fileSet["android"])
f1=reader(fileSet["kali"])

b0=batcher(f0)
b1=batcher(f1) # kali

u0=unifier(b0)
u1=unifier(b1)

c=compare(u0,u1)

print("++++++++++++++++++++++")
print()
print("_____BRIEF REPORT_____")
print()
print("++++++++++++++++++++++")
print()
for u in c:
    x=u[1]
#    if x:
#        print(">> "+u[0]+" << [POSSIBLE]")
#    else:
    print(u[0])
    # too much.
