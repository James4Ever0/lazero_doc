import requests
import traceback
import copy


def getPic(a, b, c):
    try:
        assert type(a) == int and a >= 0 and a <= 10
        assert type(b) == int and b >= 0 and b <= 1024
        assert type(c) == int and c >= 0 and c <= 1024
        # d=(a,b,c)
        # d=list(map(str,d))
        r = "https://d2h9tsxwphc7ip.cloudfront.net/{}/{}%20{}.png".format(
            a, b, c)
        r = requests.get(r)
        r = r.content
        return r
    except:
        e = traceback.format_exc()
        print(e)
        return None


def getRange(a):
    a = 2**a
    return [(x, y) for x in range(a) for y in range(a)]
    # it should be preconfigured.


def getShift(a, s, c):
    # a is a pair.
    # remove candidate?
    b = copy.deepcopy((a[0], a[1]))
    assert type(s) == int and s in [0, 1, 2, 3]
    # must include themselves.
    # length == 0 -> do not check.
    if s == 0:
        return []
    elif s == 1:
        return [(c, b[0]+1, b[1])]
    elif s == 2:
        return [(c, b[0], b[1]+1)]
    else:
        return [(c, b[0], b[1]+1), (c, b[0]+1, b[1]), (c, b[0]+1, b[1]+1)]
        # domain problem. just observe this.
# talk about arrangement.
