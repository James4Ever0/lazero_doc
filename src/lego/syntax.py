a = open("shit.sh","r").read()
#print(a)
# ready to learn shit or be shit.
# you know that. python is just another unsafe implementation of CMD.
s = [x for x in a]
print(s)
# so let's conclude. how many syntaxs are there?
import os
import subprocess
# for safe evaluation.
# the execution cannot be done too fast.
# os.system("".join(s))
# executed without problem.
# check this out.
for x in range(len(s)):
    print(x,len(s[x:]))
    # map things here.
#   print(s[x:])
# tell me, that I can imagine the scenario a bit.
    with open("fuck.sh","w+") as f:
        f.write("".join(s[x:]))
    os.system("chmod +x fuck.sh")
    # do other stuff.
    sx = subprocess.Popen(["./libjudger.so","--exe_path=fuck.sh","--max_cpu_time=500","--max_real_time=500"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdoe = sx.communicate()
    # so we are creating a civilization.
    # we need to time it. so in order to time, either do it in libjudger or in here.
    print(stdoe)
    # so how you're gonna execute the thing?
    # we're gonna pretend the thing to happen.
    # do emulate the process first?
    # so this is a no-go. must check the things first?
#    os.system("".join(s[x:]))
# so what the fuss? extract some function structure so we can manipulate it again?
