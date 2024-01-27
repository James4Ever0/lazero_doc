from dbM import regcheck, inf
import requests
import requests_ftp
from endmark import windowEndMarkEx
from multiprocessing import Pool, freeze_support


def parallel(v, z):
    with Pool(processes=len(z)) as pool:
        return pool.map(v, z)


def scars(r0):
    try:
        requests_ftp.monkeypatch_session()
        s = requests.Session()
        # really fucking slow?
        r1 = s.get(r0)
        s.close()
        return r1.content
    except:
        return
    return


def wrapper(a):
    b = scars(a)
    print("DONE", a)
    return (b, a)

    # dead code?
# i do not know. maybe it is for http only.
if __name__ == "__main__":
    r = regcheck("projects")
    # print(r)
    r = list(map(lambda x: x[0], r))
    r = windowEndMarkEx(r, 10) # strange
    # do it on cellphone. pack it up.
    # maybe the .gz file really helps.
    for x in r:
        p = parallel(wrapper, x)
        try:
            inf("projects", p)
        except:
            print("___FAILURE___")
        # really no issue?
    # alright. problem occurs.
    # maybe run this on cellphone?
    # pickle issue.
    # print(p)
    # print(type(p))
    # this is really slow as hell.
    # print(len(p))
    # ok now i can prepare for the stuff?
    # just try once.
    # for x in r:
        # do it.
        # r0=r[0]
        # print(r0)
