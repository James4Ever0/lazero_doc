import os
import subprocess
from parse import *
DEFAULT=5
o = os.listdir(".")
if "dump.rdb" in o:
    s = subprocess.Popen(["./rdb_checker.sh"],stdout=subprocess.PIPE,stderr= subprocess.PIPE)
    s = s.communicate()
    pr = parse("{}",s[0].decode())
    pr = [x for x in pr]
    dec = False
    if len(pr)==1:
        try:
            i = int(pr[0])
            print("the number:",i)
            dec = i<DEFAULT
            # what is wrong?
#            exit(0)
        except:
            print("error")
            pass
#            exit(False)
        exit(dec)
    else:
        print("not qualified")
        exit(False)
# execute some commands.
