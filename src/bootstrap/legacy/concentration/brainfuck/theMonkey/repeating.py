def al(a):
    return set(a)


def ak(a):
    # print(a)
    return [a[x]-a[x+1] for x in range(len(a)-1)]
# all kind of things?


def akII(a, s=2):
    assert type(s) == int and s >= 0
    if s > 0:
        return akII(ak(a), s-1)
    else:
        return a
# double derivative.


def am(a):
    i = al(a)
    return {x: akII([y for y in range(len(a)) if a[y] == x], 2) for x in i}


def ajam(a, b, c, d, e):
    j = am(a)
    # test_val: continuously getting zero for longer than b:
    # print(j)
    # you should sort it.
    s = list(sorted([(x, sum(j[x])) for x in j.keys()], key=lambda x: x[1]))
    s = list(map(lambda x: x[0], s))
    for x in s:
        xj = j[x]
        xy = 0
        xd = 0
        # buf=xj[0]
        for y in xj:
            if y != 0:
                if xy < b*c:
                    xy = 0
                    if xy > b*e:
                        xd += xy**c
            else:
                xy += 1
            if xy >= b or xd >= d:
                return True
            # buf = y
        if xy >= b:
            return True
    return False
