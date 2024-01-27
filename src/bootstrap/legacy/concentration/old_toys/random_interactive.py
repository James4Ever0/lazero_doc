import paramiko
import time
from core4 import createLinks
from sub2 import timeout
# import traceback
from getFromDill import returnXList
from storeADill import storeXList
import copy
from endmark import windowEndMarkEx
from multiprocessing import Pool, freeze_support
from repeating import ajam
# we need a record.
# try that thing! the jediterm.
# we are reusing the database! it is cool!
# there might be some detaching issues. launching firefox or something.
# it needs for display. unlike windows.
# if that happens, it is windows to blame.
# but xdm is a different thing, it always pops up to me.
# without my fucking keyboard, i'm feeling shit.

def autoreturn(a):
    return a.replace("\n", "")+"\n"
# there seems to some problems inside.
# repetitive patterns.
# set some total buffer size.
# charlen: 10000


def the_loop(a):
    # private_key = paramiko.RSAKey.from_private_key_file(
    #     '/root/.ssh/id_rsa')  # 使用目标的私钥来登录
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh.connect(hostname='127.0.0.1',port=22,username='root',pkey=private_key)
    # we will do recording later.
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='127.0.0.1', port=22,
                username='test', password='test')
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
    # but where the fuck is stderr?
    # remote_conn.send("happybirthday\n")
    # a = "msfconsole"
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
    timeall = 1000
    charlen_buff = 40000
    time_limit = 10
    # will be problem.
    # computer is gonna blow.
    # this will be incredible.
    # time precision.
    # we are gonna count.
    counter = 0
    patience = 5
    # is it too much?
    # self-related?
    jam_warn = False
    global_buff = ""
    while timeall >= 0 and patience > 0 and charlen_buff > 0 and time.time()-timestamp < time_limit and not jam_warn:
        # i want to see some web repl.
        # always logic mistakes. so there should be alternative?
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
            if len(x) > 135:
                if ajam(x, 75, 0.7, 500, 0.3):
                    jam_warn = True
                    break
            global_buff += x
            # total counts?
            # anyway, hope this works.
            # there could be limit.
            # dynamic things?
            if ajam(global_buff, 75, 0.7, 500, 0.3):
                jam_warn = True
                break
            # if highly repetitive, break.
            # decode?
            output_init.append([x, counter, time.time()])
            # print(x)
            charlen_buff -= len(x)
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
    # timestamp?
    # a highighter will be useful.
    ssh.close()
    for x in output_init:
        row = x[2]-timestamp
        createLinks(timestamp, row,
                    command_init[0], command_init[1], x[0], x[1])
    # print(result.decode())
    # it takes a long time.
    # let's check.
# def metaloop(a):
# /usr/share/neo4j/data/databases/graph.db/


def parallel(v, z):
    with Pool(processes=len(z)) as pool:
        return pool.map(v, z)


if __name__ == "__main__":
    freeze_support()
    r = returnXList("rock")
    f = copy.copy(r)
    r0 = [x for x in r.keys() if not r[x]]
    r1 = windowEndMarkEx(r0, 10)
    # very strange.
    # not too damn much.
    # you want this.
    rx = len(r0)
    for x in r1:
        # p=Pool(the_loop,x)
        print(rx, "items left")
        p = "".join(str(parallel(the_loop, x)))
        # what the heck.
        for y in x:
            f.update({y: True})
        storeXList(f, "rock")
        rx -= len(x)
# rebuild the thing.
# maybe it is deleted.
