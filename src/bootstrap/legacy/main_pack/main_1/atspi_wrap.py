import pyatspi
import os
os.system("pydoc3 pyatspi &>/proc/self/fd/0")
for x in dir(pyatspi):
    print(x)
    os.system("pydoc3 pyatspi."+x+" &>/proc/self/fd/0")
    # so the codebase is so goddamn huge and no-one can do the fucking writing anymore.
    # let's just halt.
    # and write C# code to dump the root node?