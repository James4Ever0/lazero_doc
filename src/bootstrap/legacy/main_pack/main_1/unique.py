import subprocess
# matter of calculation?
# this is shit. I cannot tell what the fuck is going on.
# what is the mother fucking pattern??
# ant what about the fucking crunching machine?
def searcher(y):
    assert type(y)==str
    s=subprocess.Popen(["rg","--multiline","'{}'".format(y),"/dev/shm/lazero"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    v=s.communicate()
    return v
    # making it hard to redirect the output.
# what the heck? this cannot be done in this way.
def convolutional(a,b):
    return [a[c:c+b] for c in range(len(a)-b)]

def getSearched():
    s=subprocess.Popen(["cat","/dev/shm/lazero"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    v=s.communicate()
    v=v[0]
    for r in range(2,20):
        s=convolutional(v,r)
        for s0 in s:
            # print(s0)
            k=searcher(s0.decode())
            print(k)
            print("_____________________spliter_____________________")
        print("_______end___of____conv_______")
# you want this computer to read shit for you?
if __name__ == '__main__':
    getSearched()
    # this is crazy. I cannot tell what the heck is going on.
    # shall we consider the unicode shit?
# i can hardly tell where to start.
# but this is not going to end anyway. all the fucking code I've wrote, all the fucking books, all the fucking man pages.