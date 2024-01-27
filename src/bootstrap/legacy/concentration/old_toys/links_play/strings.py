from dbM import regcheck, inf
import requests
import requests_ftp
import random
# from endmark import windowEndMarkEx
from multiprocessing import Process, freeze_support
import time
GFC = 20
# def parallel(v, z):
#     with Pool(processes=len(z)) as pool:
#         return pool.map(v, z)
# really strange idea.
# will you encounter some overflow issues?
# in theory, no.
# you can also set it to be 20.

def check_w(s, x):
    while True:
        try:
            # r = random.random()*0.1
            # time.sleep(r)
            with open(s, "w+") as f:
                f.write(str(x))
            break  # also dead code.
        except:
            dum()
            continue
    return
# just dead code.


def dum():
    r = random.random()*0.1
    time.sleep(r)


def check_r(s):
    while True:
        try:
            with open(s, "r") as f:
                return int(f.read())
            break  # also dead code.
        except:
            dum()
            continue
    return GFC  # dead code.
    # not greater than 10.
# just pass it through.
    # return
# use a database to do the task.
# this sucks.
# it is getting sparsed.


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


def checker(a, c):
    d = scars(a)
    inf("projects", [(d, a)])
    dum()
    b = check_r(c)-1
    check_w(c, b)
    print("DONE", b, a)
    return


    # dead code?
# i do not know. maybe it is for http only.
if __name__ == "__main__":
    r = regcheck("projects")
    # print(r)
    a = "proc_shuffle.log"
    check_w(a, 0)
    r = list(map(lambda x: x[0], r))
    # r = windowEndMarkEx(r, 10)  # strange
    # do it on cellphone. pack it up.
    # maybe the .gz file really helps.
    for x in r:
        b = check_r(a)
        if b < GFC:
            print("dispached", b)
            # cannot pass this around?
            p = Process(target=checker, args=(x, a))
            p.start()
            b += 1
            check_w(a, b)
        else:
            print("waiting", b)
            time.sleep(1)
        # p = parallel(wrapper, x)
        # try:
        #     inf("projects", p)
        # except:
        #     print("___FAILURE___")
        # # really no issue?
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
