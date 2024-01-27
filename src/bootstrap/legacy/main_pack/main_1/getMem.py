from dogtail import *
import os
g=globals()
f=[x for x in g]
g=list(map(lambda x:"dogtail."+x,f))
for x in g:
    os.system("pydoc3 "+x+" >> sample_diag.log")
    os.system("echo '___________spliter___________' >> sample_diag.log")
    # cd /proc/self.
    # it does not make sense. there is no fucking text over the place.
    # do you want to trace along the place?
    # do you want to change the way we configure the text?
    # whatever you mean, it is always the same shit.
    # you want to get the text. yes I know it exactly.
    # you want it. always.
    # do it for whatever reason?
    # have not done for that shit. you have not get the core of it.
    # here we go from firefox-esr to gnome-shell
    # whatever it takes.