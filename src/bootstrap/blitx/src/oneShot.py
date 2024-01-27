import sys
sys.path.append("../")
import dbM
dbM.setter("../Monitor.db")
a=dbM.show("projects")
for x in a:
    print(x)
