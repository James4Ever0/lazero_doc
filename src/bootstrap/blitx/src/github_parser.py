# get the thing.
# from bs4 import BeautifulSoup
import requests
import re
import copy
from storeADill import storeAList
from threading import Thread
import time
import threading
from fuck import shit
import random

def tar(init,s,t):
    i=True
    while i:
        try:                
            r=requests.get("https://github.com"+s,timeout=20)
            req=r.text
            sf=shit(req)
            if (sf==[]):
                time.sleep(random.random()+random.choice(range(5)))
                continue
            else:
                init.append(copy.copy(sf)) 
                i=False
                print("done",t)
        except:
            time.sleep(random.random()+random.choice(range(5)))
            continue

init=[]
listString = ["artificial", "life"]
little = "+".join(listString)
formatString = "https://github.com/search?q={}".format(little)

i=True
res=None
while i:
    try:
        r = requests.get(formatString)
        res = r.text
        sf=shit(res)
        if (sf==[]):
            time.sleep(2)
            continue
        else:
            init.append(copy.copy(sf))
            i=False
    except:
        time.sleep(2)
        continue

def dnf(x):
    if len(x) > 0:
        return x[0]
    else:
        return None
# print(res,type(res))
# get largest number.
# html = BeautifulSoup(res,features='lxml')
# "/search?p=3&amp;q=artificial+life&amp;type=Repositories"
target = list(filter(lambda x: little in x,
                     re.findall(r"/search\?p=\d+[^\"]+", res)))

target = list(
    map(lambda x: dnf(re.findall(r"[0-9]+", x)), target))
target = list(map(lambda x: int(x), list(
    filter(lambda x: x is not None, target))))

# for x in target:
#     print(x)
# target = list(map(lambda x: dnf(re.findall(r"\d+", x)),
#                   list(filter(lambda x: x is not None, target))))
# # # for x in target:
# #     print(x)
max=sorted(target)[-1]

for x in range(max-1):
    y=x+2
    #print(y)
    s="/search?p={}&amp;q={}&amp;type=Repositories".format(y,little)
    Thread(target=tar,args=(init,s,y)).start()

while True:
    time.sleep(2)
    count=threading.active_count()
    print("ACTIVE",count)
    if (count==1):
        break
storeAList(init)
