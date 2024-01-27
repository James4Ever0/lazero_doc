# import re
# re.findall(r"/+")
def getPath(x):
    # maybe it is not the time?
    f = x.split()
    for y in f:
        if "/" not in f or "\\" not in f:
            del y
    return f


# all those false shits. can you really get it right?
if __name__ == "__main__":
    with open("/dev/shm/terminal", "r") as f:
        g = f.read()
        g = getPath(g)
        print(g)
