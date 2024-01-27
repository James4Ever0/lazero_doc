import pickle,sys,os
import signal

PWD = os.environ["PWD"]
#print("pwd",PWD)
x = pickle.load(sys.stdin.buffer)
#print(x)
# so how to get the kill?
px = []
for y in x.keys():
    yx = x[y]
    if yx != PWD:
        print("will be killed",y)
        os.kill(int(y),signal.SIGKILL)
    else:
        px.append(int(y))
if len(px)==0:
    # not running.
    print("relaunching program")
    os.system("./main_redis_server.sh")
    # must daemonize the thing.
elif len(px)==1:
    print("normal running.")
else:
    # error here. must kill excessive ones.
    for x in px[1:]:
        print("killing excessive redis",x)
        os.kill(x,signal.SIGKILL)
        # must keep at least one running.
        # so what?
