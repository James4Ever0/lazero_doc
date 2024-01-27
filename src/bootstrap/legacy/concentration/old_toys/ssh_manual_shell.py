import paramiko
import time
from sub2 import timeout
import traceback
#private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')#使用目标的私钥来登录
def getOutput(remote_conn):
    timeall=10
    while timeall>=0:
        try:
            output = timeout(0.1)(remote_conn.recv)
            output = output(1000)
            print(output)
            print(type(output))
        except:
            e=traceback.format_exc()
            print(e)
        # it was stuck. once again. we should use that timer.
# i want to see some web repl.
#result = stdout.read()
#while not stdout.channel.exit_status_ready():
#    # Only print data if there is data to read in the channel
#    if stdout.channel.recv_ready():
#        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
#        if len(rl) > 0:
            # Print data from stdout
#            print(stdout.channel.recv(1024),)
            # this is not good.
#if not result:
# search for possible errors!
# errors are sweet?
# it is all connected.
# does the order matters?
#        print(output.decode())
        #print(output)
        #print(type(output))
    # code is intepretable for shell but no unicode support?
#    print(output)
    # what is the color?
    # check it?
#        time.sleep(0.1)
        timeall-=1
        if timeall<=0:
            break
    print("next_session")
    # there could be things going around.
    # how about writing a shell in python? which will be a lot easier than anything?
    # really? not for me?
        # what the heck?
        

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect(hostname='127.0.0.1',port=22,username='root',pkey=private_key)
# vim should be not working.
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='127.0.0.1', port=22, username='test', password='test')
# it is my system password after all.
# cannot let you do no harm.
# create user on windows as well!
# i do not know things. can these commands being sent to neo4j?
# they are raw data. it might fail.

#cmd = 'yes'
#stdin, stdout, stderr = ssh.exec_command(cmd)
remote_conn = ssh.invoke_shell()
# nothing is like this.
#remote_conn.send("python\n")
# what about errors?
time.sleep(2)
# you even have that shell thing!
#remote_conn.send("yes\n")
# yes! it does matters.
# by the way, I fucking hate shell command typing. It is awful.
# what about networking and GUI clicking?
# same to me! ok?
output=remote_conn.recv(1000)
#remote_conn.send("happybirthday\n")
remote_conn.send("vim\n")
getOutput(remote_conn)
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
#timeall=10
# it is just moving around the shell.
remote_conn.send(":help\n")
getOutput(remote_conn)
# do we really know it is repl?
# never mind. we can do manual debugging from now on.
#    result = stderr.read()
ssh.close()

#print(result.decode())
