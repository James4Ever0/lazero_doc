import pickle,sys,os
import signal

argx = sys.argv
limit = 1
if len(argx) == 2:
    try:
        limit = int(argx[1])
        print("limit process number",limit)
    except:
        print("error limit argument",argx[1])
else:
    print("use default limit",limit)
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
if len(px)<limit:
    # not running.
    for x in range(limit-len(px)):
        print("relaunching program",x)
        os.system("./daemon_server.sh")
    # how many times?
    # must daemonize the thing.
elif len(px)==limit:
    print("normal running.")
else:
    # error here. must kill excessive ones.
    for x in px[limit:]:
        print("killing excessive webpaste",x)
        os.kill(x,signal.SIGKILL)
        # must keep at least one running.
        # so what?
