import networkx as nx
# import random
a=""
G=nx.Graph()
# non-standard. but we've got bytes.
# you mean char-level? pix-level?
with open("links.log","r") as f:
    a=f.read()
# for x in a:
#     print(x)
# FAIL: stdin waiting; stdout nothing (when expecting something); stderr something.
# RULE: time, space.
# that's how you comprehend things?
# what is the fucking work here?
# how to do the work? finding the way to crack the parameter?
# assemble them together? making some concept nodes?
# well, you say that.
# print(a.split())
# i did found some universial function works for every shit.
# s=a.split()
# f=[lambda x: x==b for b in s]
# z=[list(map(k,s)) for k in f]
# print(z)
# print(random.choice(a.split()))
s=a.split()
for x in range(len(s)-1):
    G.add_edge(a[x],a[x+1])
nx.write_gpickle(G,"/dev/shm/randomFuck.gpickle")
# i read shit and I write shit.