from flask import Flask, request
import random
from curl_baidu import get_url
#from flask import Flask, render_template
# use monkey patch
from gevent import monkey
from stackMe import queue
import threading
import difflib
import copy

monkey.patch_all()
app = Flask(__name__)
buff=None
#mainq=queue(3)
def diff(a,b):
    return difflib.Differ().compare(a,b)
"""
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
def catch_all(path):
    print("path",path)
    return render_template('index.html')
"""
rng=random.SystemRandom()
lst=["how to kill your father","how to kill your mother"]
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
@app.route('/<path:path>',methods=['POST','GET'])
def catch_all(path):
    global buff
    print("path",path)
    if path=="keller":
#        pass
#        print(request.data)
# do not patch.
        #print(type(request.data)) bytes. but can be string
        dec=request.data.decode()
        """
        if buff==None:
            pass
        else:
            df=diff(buff,copy.copy(dec))
            # too slow?
            for gk in df:
                print(gk)
        buff=copy.copy(dec)"""
        dec=dec.split()
        # shit then. we cannot get quick diff.
        # too slow.
        for x in dec:
            print(x)
    elif path=="url":
        return get_url(rng.choice(lst))
# should you be dynamic?
# create a heart-beat package. choose from avaliable candidates.
# use redis.
# so captcha over there.
        # cannot get data here.
    return "PATH "+path
    #return render_template('index.html')
    # are you sure it is utf-8? not concerned.

# do not use browser. use code like js or curl to test connection.
"""
@app.route('/')
def homepage():
    return "Hello world!"
"""
app.run(port=7777)
