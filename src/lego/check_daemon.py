# there supposed to be something big here.
# but nothing.
# do you know the relationship?
import sys
import re
x0 = []
PID = sys.argv[1]
#print("PID",PID)
for x in sys.stdin:
    x0.append(x)
if len(x0)==1:
#    print(x0)
    x = x0[0]
    x = re.findall(r'\(\d+\)',x)
    # old problem prevails.
#    print(x)
    if len(x) == 2 and x[0] == "(1)":
        print(PID,"is a daemon")
        exit(1)
    else:
#        print("shall be killed")
        exit(0)
        # shall be killed. consider relaunching.
        # or return something?
    # start working.
else:
    exit(0)
#    print("going wrong")
    # going wrong. kill that pid.
