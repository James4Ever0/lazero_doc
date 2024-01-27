# unlike human, computer will not type word by word.
# check the multi-editing enviorment?
# that's how we get the elephant and cooperation!
import time
import copy
# passing to multiple clients or threads?
from multiprocessing import Process, freeze_support
import multiprocessing
# stop thinking about real-time ML or any other real-time stuff. just focus on the basics.
# or, more likely, the 10000x times slower rule.


class PublicDocument:
    def __init__(self, a):
        self.a = a
        self.t = time.time()

    def commit(self, d):
        self.a = d
        t = time.time()
        self.t = t
        return t

    def changeSingle(self, b, c):
        a = self.a
        # a for string. immutable.
        # b for range.
        # c for replaced things.
        return a[:b[0]]+c+a[b[1]:]

    def viewSingle(self, b):
        a = self.a
        return a[b[0]:b[1]], self.t

    def viewMultiple(self, b):
        # a = self.a
        return {x: self.viewSingle(x) for x in b}

    def checkChange(self, t):
        return t == self.t

    def dumpAll(self):
        return self.a, self.t

    # def dumpTime(self):
    #     return self.t

    def atomicChange(self, b, c, t):
        if t == self.t:
            a = copy.deepcopy(self.a)
            # print("deepcopy", a)
            # print("parameter", b, c)
            d = self.changeSingle(b, c)
            # print("what is this?", d)
            v = self.commit(d)
            if v == self.t:
                # print("here")
                return True
            else:
                self.commit(a)
                # print("there")
                return False
        else:
            return False

        # must have the view.

        # def changeMultiple(a,b):
        #     # who is first?
        #     # might introduce error?
        #     # check last change date. important.
        #     # but can we resolve this?
        #     for c,d in b:
        # run two threads at a time?

# shit?


def generalQuest(e, n):
    # working again.
    namespace, b, c = e
    sample = namespace.sample
    assert type(sample) == PublicDocument
    g = sample.t
    d = sample.viewSingle(b)
    smp = sample.changeSingle(b, c)
    # shit.
    print("sample", smp)
    print(g, n)
    print(c, d, n)
    s = sample.atomicChange(b, c, g)
    print(s, sample.a, n)
    print(sample.a, n)
    # q.put(sample)
    namespace.sample=sample
    # return

# anyway.
if __name__ == "__main__":
    # not sharing document.
    # let them share the same object.
    # but it usually needs some logic? network? check how database works?
    # that's different.
    # have fun in math. just like that.
    freeze_support()
    sample = PublicDocument("5556, 5557, 5558")
    # v = (sample, (2, 4), "")
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    # print(namespace,dir(namespace))
    namespace.sample=sample
    # print(namespace.sample)
    # great?
    v = (namespace, (-2, -4), "hello")
    g = Process(target=generalQuest, args=(v, 0))
    g0 = Process(target=generalQuest, args=(v, 1))
    g01 = Process(target=generalQuest, args=(v, 2))
    g02 = Process(target=generalQuest, args=(v, 3))
    g03 = Process(target=generalQuest, args=(v, 4))
    x = [g, g0, g01, g02, g03]
    for f in x:
        f.start()
    while True:
        if sum([int(y.is_alive()) for y in x]) == 0:
            print("final:", sample.a)
            break
        else:
            time.sleep(1)
            print("await")
            # not working.