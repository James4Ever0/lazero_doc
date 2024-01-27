import pyadb
import numpy as np
import cv2
import random

# define picture shot every --- moments.
# crop the image as needed?
# shot before doing the thing?
# i do not want to think about these shits.
# stop that entirely. just get me the xml dump.
def getImage(a):
    s2 = np.frombuffer(a.replace(b'\r\n',b'\n'), np.uint8)
    # print(s2)
    # finally!
    s2 = cv2.imdecode(s2, 1)
    return s2
d=pyadb.adb.ADB('/usr/bin/adb')
# not the same name. will introduce error if written in different scripts.
# without path?
d0=d.get_devices()
# print("show",d0)
# just consider your raw output from database.
assert len(d0)==2
e=d0[1]
# print(e)
# k=" input tap 500 500"
# k= "input swipe 500 500 700 700"
# f=d.run_cmd(k)
# simp
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
# visual difference, and always, beware of skimage.
f=d.shell_command("screencap -p") # wtf?
# f=d.shell_command("cat /sdcard/screen.png")
# print(dir(f))
# not working well.
# very bad.
# shit.
# no reign.
# shit!
# print(f[:100])
# not working?
g=getImage(f)
# nothing!
print(g.shape)
cv2.imshow(" ",g)
cv2.waitKey(0)
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