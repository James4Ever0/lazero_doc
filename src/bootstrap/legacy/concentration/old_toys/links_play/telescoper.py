from multiprocessing import Process, freeze_support
import time
import random
# prevent collision.

# global failsafe: 10
GFC = 10


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

def checker(a):
    # global a
    time.sleep(10)
    # a[0] -= 1
    dum()
    b = check_r(a)-1
    check_w(a, b)
    # it is final process.
    print("process is here", b)


if __name__ == '__main__':
    # a = [0]
    a = "proc_shuffle.log"
    check_w(a, 0)
    while True:
        b = check_r(a)
        if b < GFC:
            print("dispached", b)
            p = Process(target=checker, args=(a,))  # cannot pass this around?
            p.start()
            b += 1
            check_w(a, b)
        else:
            print("waiting", b)
            time.sleep(1)
    # checker(a)
    # print(a)
    # you can do some memory task.
# does work.
# use some mutable object, like list, set.
