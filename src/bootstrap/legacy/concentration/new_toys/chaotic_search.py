# randomly browsing the websites. like I do.
# but with initial values.
# with a global forbidden list?
# examine if it is the same.
# you can set time of getting bored.
import random
import re
import time
import traceback
import jieba
from dbM import initial, up
from the_real_wheel import parse_page, get_url

b_page = 2
recur = 20


def check_duplicate(a, b):
    # a for query.
    y = set(re.findall('r[^ ]+', a))
    return sum([int(set(y).issubset(set(x))) for x in b]) != 0


while True:
    try:
        s = int(input("enter depth of recursions:\n"))
        a = input("enter initial keyword phrase.\n")
        i = [re.findall(r'[^ ]+', x[0]) for x in set(initial("projects"))]
        assert s >= 5 and type(a) == str
        assert not check_duplicate(a, i)
        break
    except:
        e = traceback.format_exc()
        print(e)
        continue
while True:
    # print(i)
    # what about query?
    p = [x for x in parse_page(get_url(a), b_page)]
    y = [jieba.lcut_for_search(x['title']) for x in p]
    z = [jieba.lcut_for_search(x['abstract']) for x in p]
    # for x in p:
    file = 0
    t = int(time.time())
    for result in p:
        up(t, file, a, result)
        file += 1
        # waht if we want to use the result?
        print(result)
    halt = 0
    while True:
        try:
            r = random.choice(random.choice(y))
            f = random.choice(random.choice(z))
            if len(r) > 10 or len(f) > 10:
                continue
            k = " ".join([r, f])
            if check_duplicate(k, i):
                continue
        except:
            e = traceback.format_exc()
            print(e)
            continue
        halt += 1
        if halt > recur:
            raise Exception("RECURSION ERROR")
        a = k
        print(">>>Next chaotic approach<<<", a)
        break
    # a=k
    s -= 1
    i = [re.findall(r'[^ ]+', x[0]) for x in set(initial("projects"))]
    if s <= 0:
        break
print("chaotic search complete!")
# finally:
