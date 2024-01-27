from dogtail import *
# for x in dir(util):
#     print(x)
# x,y w,h.
# import dogtail
import pyautogui
import numpy as np
import cv2

def getXray(t, s):
    f = t.extents
    print(t, type(t), f)
    if f != None:
        s.append(f)
    # this is the core thing. pass something to here?


def getExam(t, s):
    y = t.children
    print(y)
    for x in y:
        getXray(x, s)
    return y


def getBuff(a, s, sample=[]):
    def l(x): return [z for y in x for z in y]
    if a != None:
        return getBuff(None, s, getExam(a, s))
    elif a == None and sample != []:
        return getBuff(None, s, l(list(map(lambda a: getExam(a, s), sample))))
    elif sample == []:
        print("_______end___of____conv_______")
        return s


# f=util.isA11yEnabled()
# print(f)
# # get the node first??
# how was the dump func enabled?
# how does it work?
t = tree.root
s = []
getBuff(t, s)
k = pyautogui.screenshot()
print(k, type(k))
ky = np.array(k)
# finally?
# always fake shit.
# but what is the deal? how to get deep?
ky=cv2.cvtColor(ky,cv2.COLOR_RGB2BGR)
print(ky, type(ky))
# still, the tree and nothing else.
for x in s:
    print(x)
    x1, y1, x2, y2 = x
    x2, y2 = x1+x2, y2+y1
    cv2.rectangle(ky, (x1, y1), (x2, y2), (255, 0, 0), 2)
    print("______RECTANGLE-SPILTER______")
cv2.imshow("sample",ky)
# the color is really strange.
# and I cannot debug this thing.
# it is weird stuff.
# all javascript, HTML and so on.
# we have all the stuff here.
cv2.waitKey(0)
# you are gonna draw rectangles?
# you need to find duplicates?
# write till this computer bricks?
# i think we have a tempfile here.
# you can make it outside the directory.
# such as /etc/lazero or /tmp/lazero, /dev/shm/lazero
# make some FIFO?
# not really the root node?
# does not have position????
# it is not great at all.
# whatever.

# x.point(mouseDelay=1)
# not implemented.
# what is this pyatspi?
# for x in dir(t):
#     print(x)
