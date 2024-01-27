import os
def checkBuffer(a,b):
    # assert type(a)==str and "/" not in a and len(a)>0
    assert b>0 and type(b)==int
    k=0
    with open("/dev/shm/"+a,"r+") as f:
        k=len(f.read())
    if k>b:
        os.remove("/dev/shm/"+a)
# there is no way you can get shit.
# all days talking about shit, and where the fuck is the fucking end?
def updateBuffer(a,b,c=10000):
    # first check the size, then decide the shit.
    # well,well, you really want to insert some binary data into it???
    # keeping it small.
    assert type(a)==str and "/" not in a and len(a)>0
    assert type(b)==str
    checkBuffer(a,c)
    # always the decoding problem.
    # sure sir, there is operate system, but there is no system on how to write OS.
    # but we shall not fix it. at least not on our own.
    # if type(b)==str:
    #     with open("/dev/shm/"+a,"ab+") as f:
    #         f.write(b.encode())
    # else:
    # can we just debug the tensorflow framework?
    # you really want to know how to get the size of the file?
    # or you really want to understand everything?
    # bringing you to the fucking library is not for fun. it is a way to realize how fucking limited resources you've got.
    with open("/dev/shm/"+a,"a+") as f:
        f.write(b[-c-1:])
def initBuffer(a):
    assert type(a)==str and "/" not in a and len(a)>0
    f="/dev/shm/"+a
    if os.path.exists(f):
        os.remove(f)
    os.system("touch "+f)
    # whatever you might want to do.