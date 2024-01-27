import re
from storeADill import storeXList
# just assemble them.


def getCode(a):
    b = a.split("\n")
    b = list(map(lambda x: re.findall(r'[^ ]+$', x), b))
    b = list(filter(lambda x: len(x) == 1, b))
    # print(len(b))
    b = list(map(lambda x: x[0], b))
    b = list(filter(lambda x: ".arpa" in x and (
        ".asc" not in x and ".md5" not in x and ".sha1" not in x and ".gz" not in x), b))
    return b
# highlighter can be in trouble?
# what about other registries?
# do the same.
# it could not be good.
# we need to deal with them differently. may have duplicated names across servers.


def openText(a):
    with open(a, "r") as f:
        return f.read()

# "apnic_rdns.log"


def getCoords(a):
    a = openText(a)
    a = getCode(a)
    return a


def genDict(a):
    return {x+"_rdns.log": "ftp://ftp."+x+".net/pub/zones/" for x in a}


# for x in a:
#     print(x)
# all the same.
# add them together.
a = ["afrinic", "apnic", "lacnic", "arin", "ripe"]
a = genDict(a)
a = {x: list(map(lambda y: a[x]+y, getCoords(x))) for x in a.keys()}
# i said, put it into database.
storeXList(a,"rock")
# think about it.
# print(a)
# a=[y for z in [a[x] for x in a.keys()] for y in z]
# for x in a:
#     print(x)
# we'd better flattern this thing.
# check if it is done?
# use batch worker.
