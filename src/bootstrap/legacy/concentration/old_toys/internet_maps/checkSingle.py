# from dbM2 import
import numpy as np
import cv2
from dbM2 import regcheck, inf
from basepak import getShift
from classic import getRead as batchRead
# use some image reading thing.
from dbM import show
from multiprocessing import Pool, freeze_support
from endmark import windowEndMarkEx as windowEndmarkEx
# TimeoutError?
# use graph query to do this.
# randomly select three?

table_name = "projects"
# use tesseract now!
threshold = 5
batch_size = 10


def parallel(x, v, z):
    with Pool(processes=x) as pool:
        return pool.map(v, z)


# say we've got a sample.
# you can adjust this.


def knock(sample):
    sd = sample[1:3]
    sv = sample[-1]
    sk = sample[0]
    sn = [sample[:-1]]+getShift(sd, sv, sk), sv
    return sn


def get_1(s0, sv):
    assert sv == 1
    assert len(s0) == 2
    # print(type(s0), len(s0))
    s1 = s0[0]
    # s2=cv2.imread(s1)
    # this is not right.
    # oh you may say, let the machine to decode the image!
    # just wait.
    s2 = np.frombuffer(s1, np.uint8)
    s2 = cv2.imdecode(s2, 1)
    s3 = np.frombuffer(s0[1], np.uint8)
    s3 = cv2.imdecode(s3, 1)
    # s4=s3
    h1, w1 = s3.shape[:2]
    h2, w2 = s2.shape[:2]
    res = np.zeros(shape=(max(h1, h2), w1+w2, 3), dtype=np.uint8)
    for i in range(s2.shape[2]):
        res[:h2, :w2, i] = np.ones([h1, w1])*s2[:, :, i]
        res[:h2, w2:w2+w1, i] = np.ones([h1, w1])*s3[:, :, i]
    _, w1 = res.shape[:2]
    w1 = int(w1/4)
    return res[:, w1:w1*3, :]


def get_2(s0, sv):
    assert sv == 2
    assert len(s0) == 2
    # print(type(s0), len(s0))
    s1 = s0[0]
    # s2=cv2.imread(s1)
    # this is not right.
    # oh you may say, let the machine to decode the image!
    # just wait.
    s2 = np.frombuffer(s1, np.uint8)
    s2 = cv2.imdecode(s2, 1)
    s3 = np.frombuffer(s0[1], np.uint8)
    s3 = cv2.imdecode(s3, 1)
    # s4=s3
    h1, w1 = s3.shape[:2]
    h2, w2 = s2.shape[:2]
    res = np.zeros(shape=(h1+h2, max(w1, w2), 3), dtype=np.uint8)
    for i in range(s2.shape[2]):
        res[:h2, :w2, i] = np.ones([h1, w1])*s2[:, :, i]
        res[h2:h2+h1, :w1, i] = np.ones([h1, w1])*s3[:, :, i]
    w1, _ = res.shape[:2]
    w1 = int(w1/4)
    return res[w1:w1*3, :, :]


def get_0(s0, sv):
    assert sv == 0
    assert len(s0) == 1
    s2 = np.frombuffer(s0[0], np.uint8)
    s2 = cv2.imdecode(s2, 1)
    return s2


def get_3(s0, sv):
    assert sv == 3
    assert len(s0) == 4
    # print(type(s0), len(s0))
    s1 = s0[0]
    # s2=cv2.imread(s1)
    # this is not right.
    # oh you may say, let the machine to decode the image!
    # just wait.
    s2 = np.frombuffer(s1, np.uint8)
    s2 = cv2.imdecode(s2, 1)
    s3 = np.frombuffer(s0[1], np.uint8)
    s3 = cv2.imdecode(s3, 1)
    # s4=s3
    h1, w1 = s3.shape[:2]
    h2, w2 = s2.shape[:2]
    res = np.zeros(shape=(h1+h2, max(w1, w2), 3), dtype=np.uint8)
    for i in range(s2.shape[2]):
        res[:h2, :w2, i] = np.ones([h1, w1])*s2[:, :, i]
        res[h2:h2+h1, :w1, i] = np.ones([h1, w1])*s3[:, :, i]
    s4 = np.frombuffer(s0[2], np.uint8)
    s4 = cv2.imdecode(s4, 1)
    s5 = np.frombuffer(s0[3], np.uint8)
    s5 = cv2.imdecode(s5, 1)
    h1, w1 = s5.shape[:2]
    h2, w2 = s4.shape[:2]
    res0 = np.zeros(shape=(h1+h2, max(w1, w2), 3), dtype=np.uint8)
    for i in range(s2.shape[2]):
        res0[:h2, :w2, i] = np.ones([h1, w1])*s4[:, :, i]
        res0[h2:h2+h1, :w1, i] = np.ones([h1, w1])*s5[:, :, i]
    h1, w1 = res.shape[:2]
    h2, w2 = res0.shape[:2]
    res1 = np.zeros(shape=(max(h1, h2), w1+w2, 3), dtype=np.uint8)
    for i in range(s2.shape[2]):
        res1[:h2, :w2, i] = np.ones([h1, w1])*res[:, :, i]
        res1[:h2, w2:w2+w1, i] = np.ones([h1, w1])*res0[:, :, i]
    h1, w1 = res1.shape[:2]
    h1, w1 = int(h1/4), int(w1/4)
    res2 = res1[h1:h1*3, w1:w1*3, :]
    return res2


def getSingle(sample):
    s, sv = knock(sample)
    s0 = show(table_name, s)
    if sv == 0:
        return get_0(s0, sv)
    elif sv == 1:
        return get_1(s0, sv)
    elif sv == 2:
        return get_2(s0, sv)
    elif sv == 3:
        return get_3(s0, sv)
    else:
        raise Exception("shit happens!")
    return


def ver_black(p):
    return np.mean(p) > threshold


def getDouble(sample):
    g = getSingle(sample)
    if ver_black(g):
        return {sample: batchRead(g)}
    else:
        return {sample: ""}


def streamDouble(smp):
    r = parallel(len(smp), getDouble, smp)
    r0 = {}
    for x in r:
        r0.update(x)
    return r0

# there are many dots over the spot.
# result will be inaccurate.


def upDouble(d):
    y = d.keys()
    # for x in y:
    inf(table_name, [(d[x], *x) for x in y])
    # print("imports:", len(y), "contents:", *[d[x] for x in y])
    return
# all shit.


if __name__ == "__main__":
    freeze_support()
    f = regcheck(table_name)
    print("WORKLOAD",len(f))
    # you can set some batch size.
    f0 = windowEndmarkEx(f,batch_size)
    # print(f0)  # working.
    for z in f0:
        print(z)
        s = streamDouble(z)
        upDouble(s)
# you plan to get it all?
# sample = (5, 0, 0, 2)  # to pics.
# s, sv = knock(sample)
# # print(s)
# s0 = show(table_name, s)
# r = get_2(s0, sv)
# sample = (5, 0, 0, 3)  # to pics.
# s, sv = knock(sample)
# # print(s)
# s0 = show(table_name, s)
# r0 = get_3(s0, sv)
# e=[r,r0]
# e0=batchRead(e)
# print(e0)
# skip pure black.
# be it 2.
# sv=sample[-1]
# try different.
# opencv is great but i cannot expolre.
# print(r)
# you will always get only one result.
# p = np.mean(r)
# print(p)
# if this is applied, then return '' instead of None.
# cv2.imshow(" ", r)
# cv2.waitKey(0)
# cv2.imshow(" ",res2)
# cv2.waitKey(0)
# just combine? too much computation.
# not too bad.
# same, do not do that to skimage. it sucks.
# print(s2,s2.shape)
# # not working.
# people tend to freak each other out.
# perform a single shot.
# print(s)
# now, how to get those pics?
# print(sd,sv)
# s=show(table_name,[(0,0,0)])
# just get one?
# print(s)
