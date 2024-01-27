#import dogtail
from dogtail import *
# actually you can find out what is in here by looking into the globals.
# can you do anonymous shits? adding prefix will do the trick.
# finally get it right?
f="________________________________________________________________"
# # distribution?
# # fuck the code?
# print(f)
# for x in dir(utils):
#dogtail.config.childrenLimit=1000
#     print(x)
# where is the config?
def walker(a,f):
    a.childrenLimit=1000
# not setting it?
#    config.childrenLimit=1000
    for x in a.children:
        print(x.path.split("/")[-1])
        # get the extent.
        print(x.extents)
        # get the name somehow.
        # somewhat we don't need the name?
        # the last digits.
#        for j in f:
#            try:
#                eval("""print(">>>>>{}",x.{})""".format(j,j))
#            except:
#                pass
        walker(x,f)
# Only returning 100 children. You may change config.childrenLimit if you wish. This message will only be printed once.
# so change it?
r=tree.root
#print(r.id)
f=dir(r)
walker(r,f)
#for x in r.children:
#    print(x.id)
# get a walker for this.
#print(r,type(r))
#print(f)
#for x in dir(r):
#    print(x)
#print(f)
#print(r.dump())
# this is fucking awesome.
# what is this class??
    # always the fucking cron job!
    # it is hard to tell. check that shit first?
    # this is gnome compatible. but remember, there's some tinycore linux over the spot.
    # well, we don't use it.
    # there is a sniff util.
# f=utils.isA11yEnabled()
# f=utils.screenshot()
# print(f)
# returning a path.
# it can be done with a little script.
# whatever. this is not the main focus.
# print the tree of all shits? what about windows?
# shit man.
