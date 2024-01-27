# demo for my so-called recursive net.
# we are gonna randomly spark these things.
# can we use some hidden nodes?
# they just pass data directly to another.
# no way.
import numpy as np
import random
# this is an unfinished script.
# maybe useful to some extent.

class data_overlay:
    def __init__(self, data, forward_ratio, remaining_life, direction):
        self.data = data
        self.forward_ratio = forward_ratio
        self.remaining_life = remaining_life
        self.direction = direction

    def dump(self):
        return self.data, self.forward_ratio, self.remaining_life, self.direction


class data_final:
    def init(self, data):
        self.data = data

    def dump(self):
        return self.data


class node:
    def __init__(self, node_coord, node_neighbor):
        # self.node_direction=node_direction
        # different for different neighbors.
        # they do not do anything to the data. therefore, it is waiting for further modification.
        self.node_neighbor = node_neighbor
        self.node_coord = node_coord

    def returnCoord(self):
        return self.node_coord

    def returnNeighbor(self):
        return self.node_neighbor

    def updateCoord(self, new_coord):
        self.node_coord = new_coord

    def updateNeighbor(self, new_neighbor):
        self.node_neighbor = new_neighbor

    def process(self, data_struct,candidates):
        s = self.rep(data_struct)
        if s != None:
            if type(s).__name__ == "data_overlay":
                data, forward_ratio, remaining_life, direction = s.dump()
                # the probability.
                f0 = [x[1] for x in self.node_neighbor if x[0] == direction]
                v = min(forward_ratio, len(f0))
                f1 = [f0[x] for x in random.sample(range(len(f0)), v)]
                # just build a static one. we will consider something else later.
                # there is a evil math.
                return (s, tuple(f1))
            elif type(s).__name__ == "data_final":
                return (s, None)
            elif s is None:
                return (s, None)
            else:
                raise Exception("node error!")
        # if rep right, then we do the thing.

    def rep(self, dstruct):
        if type(dstruct).__name__ == "data_overlay":
            data, forward_ratio, remaining_life, direction = dstruct.dump()
            assert remaining_life >= 0
            # do we have a direction for each node?
            # can it alter?
            # we can define the type of it.
            if remaining_life > 1:
                return data_overlay(data, forward_ratio, remaining_life-1, direction)
            else:
                return data_final(data)
        elif type(dstruct).__name__ == "data_final":
            return None
        else:
            raise Exception("inproper datastruct.")

# def transmit(n,n0,n1):
#     a,b=n0
#     c,d=n1
#     # just map it rightly.
#     if a is not None:
#         if b is not None:
#             if b == (): # you can do this again.
#                 # print(a.dump())
#                 s1=[n[x].process(a) for x in d]
#                 # this time it is the same result.
#                 s2=s1[0][0]
#                 s3=(x for y in list(map(lambda x:x[1],s1)) for x in y)
#                 return (s2,s3,n1)
#                 # print(a)
#                 # s=n[r].process(a)
#                 # return s
#             else:
#                 # merge the thing.
#                 s1=[n[x].process(a) for x in b]
#                 # this time it is the same result.
#                 s2=s1[0][0]
#                 s3=(x for y in list(map(lambda x:x[1],s1)) for x in y)
#                 return (s2,s3,n0)
#         else:
#             print("content:",a)
#             return (*n0,n0)
#     else:
#         print("the end!")
#         return (*n0,n0)
# all six types:
# ->->->|  ->->->| |<-<-<-  |<-<-<-  ->->->| |<-<-<- |<- ->|
#   ->->|  ->->    |<-<-       <-<-
#     ->|  ->      |<-           <-
#     ->|  ->      |<-           <-
if __name__ == "__main__":
    n = {(x, y): node((x, y), None) for x in range(10) for y in range(10)}
    sn = list(n.keys())
    for x in n.keys():
        n[x].updateNeighbor(
            list(map(lambda y: (random.choice([True, False]), y), random.sample(sn, 10))))
    r = random.choice(sn)
    v = (data_overlay("hello world", 1, 5, True),(r,))
    # not sending, so you need to solve it?
    # dead, so you need not to solve?
    print(v)
    # can we predict it?
    # for x in range(10):
    #     print("epoch",x)
    #     print(v)
    #     v=transmit(n,v,v)
    # n0=n[r].process(v)
    # print(n0)
                # print(s[0].dump())