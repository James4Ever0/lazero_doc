import random
# import math
import numpy as np
# rule: strenghten the connection proportion to closeness.
# no negative things?
# whatever.
# fucking shit.
# start along?
import copy


def judge(a, b, sigma=2):
    k = a+b
    # k2=math.sign(k)
    # random choice?
    # k2 = -1 if k < 0 else 1
    k2 = random.choice([-1, 1])
    k3 = min(sigma, sigma/(abs(k)+0.01))
    k4 = k3*k2
    return k4


def mod(a, b, c):
    if c > 0:
        return (a, b)
    else:
        return (b, a)


def cluster(a, b):
    ax, ay, at = a
    bx, by, bt = b
    j = judge(at, bt)
    m = mod((ax, ay), (bx, by), j)
    return (m, j)


def initMatrix(a):
    return np.matrix([[random.choice(np.linspace(-1, 1, 20)) for x in range(a)] for y in range(a)])


def fasb(a, k=50, e=5, l=50):
    return [(random.choice(range(a)), random.choice(range(a)), random.choice(np.linspace(0.1, e, k))) for x in range(l)]
# should plus but not minus.


def gencode(a):
    l = len(a)
    f = []
    for x in range(len(a)//2):
        f0 = x*2
        t = a[f0]
        if x == 0:
            f.append(cluster(t, a[f0+1]))
        elif x*2 == l-1:
            f.append(cluster(a[f0-1], t))
        else:
            f.append(cluster(t, a[f0+1]))
            f.append(cluster(a[f0-1], t))
    return f


def chg_mat(a, b):
    c, d, e = b
    a[c, d] += e
    # a[d[0]][d[1]] -= e
    return a


    # r=a[:-1]
    # r0=a[1:]
if __name__ == '__main__':
    z = 10
    im = initMatrix(z)
    print("init", im.shape)
    print(im)
    buf = copy.deepcopy(im)
    for x in range(5):
        f = fasb(z)
        g = gencode(f)
        for y in range(z):
            k = f[y]
            # print(k)
            im = chg_mat(im, k)
            print("session", x, "task", y)
            print("same?", np.all(buf == im))
            # print("same?",buf==im)
            # np array is mutable.
            # print(im)
            print(sum(sum(im)))
            # print(sum(im.tolist()))
            buf = copy.deepcopy(im)
    print("DONE?")
