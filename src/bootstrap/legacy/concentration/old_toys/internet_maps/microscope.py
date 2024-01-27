from multiprocessing import Process, freeze_support
import time
import random


def dum():
    r = random.random()*0.1
    time.sleep(r)


def f(a):
    time.sleep(10)
    print("I AM DEAD", a)
    dum()


def check(a):
    return sum([int(x.is_alive()) for x in a]+[0])

def clean(a):
    return [x for x in a if x.is_alive()]

if __name__ == "__main__":
    a = []
    # m = 0
    while True:
        a=clean(a)
        m=check(a)
        if m<10:
            print("dispached",m)
            p = Process(target=f, args=(m,))
            p.start()
            a.append(p)
            # break
        else:
            print("waiting",m)
            time.sleep(1)