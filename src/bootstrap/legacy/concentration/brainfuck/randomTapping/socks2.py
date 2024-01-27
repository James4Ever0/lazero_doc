# coding: utf-8
import pyadb
# import numpy as np
from multiprocessing import Process, freeze_support
from dbM_2 import initial
# import cv2
# this is fucking python2 script.
# just can you repeat my input?
import random
import time
# just how to get the human input?
def wrapper(x):
    p=Process(target=initial, args=("projects",[x]))
    p.start()
    # p.join()
    return
# you know, that their fucking brain architecture is fried.
# define picture shot every --- moments.
# crop the image as needed?
# shot before doing the thing?
# i do not want to think about these shits.
# stop that entirely. just get me the xml dump.
# do you want to calculate the overall success rate over different acts?
# gui is just a beginning, but remember, only something that is attacable to human can receive human critic and training.
# low level language, must be associated with books and resources.
SCALE=(1080,1920)

def getRandomCode(a):
    x0,y0=a
    return random.choice(range(x0)),random.choice(range(y0))
# shit. only for python3.
def getTap(a):
    return "input tap {} {}".format(*getRandomCode(a))

def getSwipe(a):
    k=[]
    for x in range(2):
        x0,y0=getRandomCode(a)
        k.append(x0)
        k.append(y0)
    return "input swipe {} {} {} {}".format(*k)
# not printing shit?
# def getImage(a):
#     s2 = np.frombuffer(a.replace(b'\r\n',b'\n'), np.uint8)
#     # print(s2)
#     # finally!
#     s2 = cv2.imdecode(s2, 1)
#     return s2

def getDump(d):
    d.shell_command("uiautomator dump")
    f=d.shell_command("cat /sdcard/window_dump.xml")
    return f

def getRandomAct(a,d):
    p=random.choice([getTap,getSwipe])
    p0=p(a)
    d.shell_command(p0)
    return p0
# will introduce error if with human manipulation.
def getTime():
    return time.time()
# it will be too huge, all xml dumps, and more.
def getLoop(a,d):
    xv=["xml_dump","screen_command"]
    buffer=getDump(d)
    wrapper((getTime(),xv[0],buffer))
    while True:
        e0=getRandomAct(SCALE,d)
        time.sleep(.5)
        g0=getDump(d)
        if buffer!=g0:
            buffer=g0
            print("different act!")
            print(e0)
            wrapper((getTime(),xv[1],e0))
            wrapper((getTime(),xv[0],buffer))
        # else:
        # get human input is important.
        # better use logcat? monitor its output?
        # well, that verbosity you cannot stand.
        #     print("no difference!")
        #     print(e0)
            # you can increase the registry, for input and output.
# do not care about the growth of your fucking breast, cause it is flat and everything is shit.
if __name__ == "__main__":
    freeze_support()
    d=pyadb.adb.ADB('/usr/bin/adb')
    # not the same name. will introduce error if written in different scripts.
    # without path?
    # we need wireless?
    # using screen command? share output?
    # you can try it, if you really want to give it a try.
    # want to store in neo4j or something else?
    # this is a remarkable story. just what about human input? will my input counts?
    # can it repeat my acts and therefore reinforce the learning?
    # maybe the time will change. does that count?
    # what about these things?
    # just think about something equivalent to the overall shit.
    # you need something that has overall control.
    # never mind. you can manually override this.
    d0=d.get_devices()
    # print("show",d0)
    # just consider your raw output from database.
    assert len(d0)==2
    e=d0[1]
    # print(e)
    # check if it is the same?
    # i do not know if this works the same for py2.
    getLoop(SCALE,d)
# print(g0)
# print(e0)
# fucking hell.
# why don't you swipe?
# k=" input tap 1080 1920"
# k="input tap 1000 1900" #- ok.
# # k= "input swipe 500 500 700 700"
# f=d.shell_command(k)
# simple.
# fuck. but can we do the image?
# will it be large?
# d.shell_command("uiautomator dump")
# how to record the events?
# is it a good idea to create xml dumps along the way?
# f=d.shell_command("cat /sdcard/window_dump.xml")
# d.shell_command("")
# print("this is not from the console")
# print(f)
# it is working, but we need the timeout.
# something, huh?
# what about other buttons?
# just fucking tap it!
# finally did I realized the limitation of python, and so many other operating systems.
# shall we use logcat?
# i don't even know what the fuck it is talking about.
# yes, does this mean anything?
# f=d.get_logcat()
# d.shell_command("")
# using local python?
# numpy or something.
# record it or not, just follow the schema.
# visual difference, and always, beware of skimage.
# f=d.shell_command("screencap -p") # wtf?
# # f=d.shell_command("cat /sdcard/screen.png")
# # print(dir(f))
# # not working well.
# # very bad.
# # shit.
# # no reign.
# # shit!
# # print(f[:100])
# # not working?
# g=getImage(f)
# # nothing!
# print(g.shape)
# cv2.imshow(" ",g)
# cv2.waitKey(0)
# 1920*1080?
# it is so fucking fragile.
# print(f)
# print(type(f))
# print("logcat")
# print(f)
# not working?
# this is crazy.
# not working at all.
# it doesn't differentiate!