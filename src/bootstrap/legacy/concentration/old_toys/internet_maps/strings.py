from dbM import regcheck, inf
import requests
import requests_ftp
import random
# from endmark import windowEndMarkEx
from basepak import getPic
from multiprocessing import Process, freeze_support
import time
from endmark import windowEndMarkEx as windowEndmarkEx
GFC = 45
# does not matter. it is all the same.
# limitation on max connection.
THROTTLE = 10
MAX_PATIENCE = 5
RESETTING = 5
# def parallel(v, z):
#     with Pool(processes=len(z)) as pool:
#         return pool.map(v, z)
# really strange idea.
# will you encounter some overflow issues?
# in theory, no.
# you can also set it to be 20.


def check(a):
    return sum([int(x.is_alive()) for x in a]+[0])


def clean(a):
    return [x for x in a if x.is_alive()]

# def check_w(s, x):
#     while True:
#         try:
#             # r = random.random()*0.1
#             # time.sleep(r)
#             with open(s, "w+") as f:
#                 f.write(str(x))
#             break  # also dead code.
#         except:
#             dum()
#             continue
#     return
# just dead code.


def dum():
    r = random.random()*0.1
    time.sleep(r)


# def check_r(s):
#     while True:
#         try:
#             with open(s, "r") as f:
#                 return int(f.read())
#             break  # also dead code.
#         except:
#             dum()
#             continue
#     return GFC  # dead code.
    # not greater than 10.
# just pass it through.
    # return
# use a database to do the task.
# this sucks.
# it is getting sparsed.


def scars(r0):
    try:
        return getPic(*r0)
        # requests_ftp.monkeypatch_session()
        # s = requests.Session()
        # # really fucking slow?
        # r1 = s.get(r0)
        # s.close()
        # return r1.content
    except:
        return
    return
# no idea where it is heading to.

def checker(a, c):
    d = scars(a)
    inf("projects", [(d, *a)]) # it should be inserted.
    dum()
    # b = check_r(c)-1
    # check_w(c, b)
    print("DONE", b, a)
    return

    # dead code?
# i do not know. maybe it is for http only.
if __name__ == "__main__":
    r = regcheck("projects")
    # # print(r)
    zr = windowEndmarkEx(r, THROTTLE)
    a = []
    # a = "proc_shuffle.log"
    # check_w(a, 0)
    # r = list(map(lambda x: x[0], r))
    # r = windowEndMarkEx(r, 10)  # strange
    # do it on cellphone. pack it up.
    # maybe the .gz file really helps.
    print("REMAINING WORK", len(r))
    pxx = 0
    pb = None
    for x in zr:
        a = clean(a)
        b = check(a)
        # b = check_r(a)
        if b < GFC:
            for y in range(len(x)):
                c = b+y  # just a hint.
                print("dispached", c)
                # cannot pass this around?
                # strange.
                # just do not make the fucking same mistake.
                p = Process(target=checker, args=(x[y], c))
                p.start()
                a.append(p)
            # b += 1
            # check_w(a, b)
        else:  # do a purge logic.
            if pb == b:
                pxx += 1
            else:
                pxx = 0
            pb = b
            if pxx >= MAX_PATIENCE:
                counter = 0
                skip_counter = 0
                for f0 in a:
                    try:
                        f0.terminate()
                        print("purge", counter)
                        # that process does not indicate shit.
                        counter += 1
                    except:
                        print("skip", skip_counter)
                        skip_counter += 1
                        pass
                print("kill", counter, "skip", skip_counter)
                a = []
                time.sleep(RESETTING)
                print("RESETTING FOR", RESETTING, "SECS")
                # reset the pxx.
                pxx = 0
            else:
                print("waiting", b, "patience", MAX_PATIENCE-pxx)
                time.sleep(1)
        # else:
        #     print("OVERLOAD!", b)
        #     print("RESETTING TO ZERO!")
        #     check_w(a, 0)
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
