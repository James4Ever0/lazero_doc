import paramiko
import time
from core4 import createLinks
from sub2 import timeout
import traceback


def autoreturn(a):
    return a.replace("\n", "")+"\n"


private_key = paramiko.RSAKey.from_private_key_file(
    '/root/.ssh/id_rsa')  # 使用目标的私钥来登录
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect(hostname='127.0.0.1',port=22,username='root',pkey=private_key)
# we will do recording later.
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='127.0.0.1', port=22, username='test', password='test')
# it is my system password after all.

#cmd = 'yes'
#stdin, stdout, stderr = ssh.exec_command(cmd)
timestamp = time.time()
# accept float?
remote_conn = ssh.invoke_shell()
# nothing is like this.
# remote_conn.send("python\n")
# what about errors?
time.sleep(2)
# you even have that shell thing!
# remote_conn.send("yes\n")
# yes! it does matters.
# by the way, I fucking hate shell command typing. It is awful.
# what about networking and GUI clicking?
# same to me! ok?
output = remote_conn.recv(1000)
# remote_conn.send("happybirthday\n")
a = "msfconsole"
remote_conn.send(autoreturn(a))
command_init = [a, 0]
output_init = []
# time.sleep(20)
# what is going on?
# just to check.
# it is working, after all.
# may miss a bit?
# you should get that thing!
# no error! strange thing!
# there should be error.
# no respond! how about python?
# why you have to wait
# sleep for a while?
timeall = 50
counter = 0
patience = 5
# is it too much?
while timeall >= 0 and patience > 0:
    # i want to see some web repl.
    #result = stdout.read()
    # while not stdout.channel.exit_status_ready():
    #    # Only print data if there is data to read in the channel
    #    if stdout.channel.recv_ready():
    #        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
    #        if len(rl) > 0:
    # Print data from stdout
    #            print(stdout.channel.recv(1024),)
    # this is not good.
    # if not result:
    # search for possible errors!
    # errors are sweet?
    # it is all connected.
    # does the order matters?
    # print(output.decode())
    try:
        # p = timeout(0.1)(output.decode)
        p = timeout(1)(remote_conn.recv)
        # we are missing things.
        x = p(1000).decode()
        output_init.append([x, counter, time.time()])
        print(x)
        counter += 1
        # it is shit.
        # but then we get stuck.
    except:
        # print(traceback.format_exc())
        patience -= 1
        # there is no error.
        pass
    # well, for those non-ending.
    # code is intepretable for shell but no unicode support?
#    print(output)
    # what is the color?
    # check it?
    # time.sleep(0.1)
    # print(timeall, time.time()-timestamp)
    # it is likely to fail.
    timeall -= 1
# do we really know it is repl?
# never mind. we can do manual debugging from now on.
#    result = stderr.read()
ssh.close()
for x in output_init:
    row = x[2]-timestamp
    createLinks(timestamp, row, command_init[0], command_init[1], x[0], x[1])
# print(result.decode())
# let's check.
