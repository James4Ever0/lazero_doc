# string first.
#from numba import jit as  autojit
import multiprocessing
import time

#@autojit(nopython=True, nogil=True)
def blackwhite(a,b,c=True):
    byte=False
    if type(a)==str:
        assert type(b)==str
    elif type(a)==bytes:
        assert type(b)==bytes
        byte=True
    else:
        return None
    assert type(c)==bool
    buf="" if not byte else b""
    cb=[]
    t=len(a)
    for d in range(t):
        x=a[d:d+1]
        """if d%1000==0:
            print("byte",d,"total",t)"""
        if c:
            if x in b:
                buf+=x
            elif (buf!="" and not byte) or (buf!=b"" and byte):
                cb.append(buf)
                buf="" if not byte else b""
        else:
            if x not in b:
                buf+=x
            elif (buf!="" and not byte) or (buf!=b"" and byte):
                cb.append(buf)
                buf="" if not byte else b""
    if (buf!="" and not byte) or (buf!=b"" and byte):
        cb.append(buf)
    return cb

#@autojit(nopython=True, nogil=True)
def bw(a,b,d,e,c=True):
    s=blackwhite(a,b,c)
    e[d]=s

#@autojit(nopython=True, nogil=True)
def multibw(a,b,d,c=True):
    byte=False
    if type(a)==str:
        assert type(b)==str
    elif type(a)==bytes:
        assert type(b)==bytes
        byte=True
    else:
        return None
    assert type(c)==bool 
    l=len(a)
    assert d<=l and d>1 and type(d)==int
    r=l%d
    s=l//d
    k=[(x*s,(x+1)*s) for x in range(d-1)]
    k+=[((d-1)*s,d*s+r)]
    #param={x:None for x in range(d)}
    mgr = multiprocessing.Manager()
    param = mgr.dict()
    for x in range(d):
        param[x]=None
    jobs = [multiprocessing.Process(target=bw, args=(a[k[x][0]:k[x][1]],b,x,param,c)) for x in range(d)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    """for x in range(d):
        k0,k1=k[x]
        print(k0,k1)
        threading.Thread(target=bw,args=(a[k0:k1],b,x,param)).start()
    while True:
        su=sum([int(param[x]==None) for x in range(d)])
        print(su)
        if su==0:
            break
        else:
            time.sleep(1)"""
    result=[param[x] for x in range(d)]
    result=[x for y in result for x in y]
    # can increase complexity.
    return result
    #print(result)
    # use multiprocessing.
    """if byte:
        return b"".join(result)
    else:
        return "".join(result)"""
