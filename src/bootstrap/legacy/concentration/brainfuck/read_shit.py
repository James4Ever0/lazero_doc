# we're gonna open some file?
# reversing time is important in intelligence.
def getBin(a):
    with open(a,"rb") as f:
        return f.read()# k=getBin("Monitor.db")
# it is so easy, you suppose?
# must be done in a universial way.
k=getBin("Monitor.db")
for x in k:
    print(hex(x),type(x))
    # we have integers now! cannot believe it!