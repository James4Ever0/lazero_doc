import redis   # 导入redis 模块
from itertools import zip_longest as izip_longest
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def rset(a,b,c=3):
    r.set(a,b,ex=c)  # 设置 name 对应的值
"""while True:
    try:
        print(r['name'])
        print(r.get('name'))  # 取出键 name 对应的值
        print(type(r.get('name')))
    except:
        print("expired")
    time.sleep(1)"""
def rget(a):
    try:
        return r.get(a)
    except:
        return None

def rbset(a,b,c=3):
    pipe = r.pipeline()
    for x in a:
        #pipe.lpush(b,x)
        pipe.setex(x,c,b)
    pipe.execute()
    print("done: ",len(a))

def batcher(iterable, n):
    args = [iter(iterable)] * n
    return izip_longest(*args)

# in batches of 500 delete keys matching user:*
# do you know when things going to shit?
def rka():
    return batcher(r.scan_iter('*'),500)

def pka():
    for keybatch in rka():
        print(*keybatch)

