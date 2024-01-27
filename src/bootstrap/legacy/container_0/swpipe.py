# -*- coding:utf-8 -*-

import subprocess
import sys
import threading
import platform
import time


class LoopException(Exception):
    """循环异常自定义异常，此异常并不代表循环每一次都是非正常退出的"""

    def __init__(self, msg="LoopException"):
        self._msg = msg

    def __str__(self):
        return self._msg


class SwPipe():
    """
    与任意子进程通信管道类，可以进行管道交互通信
    """

    def __init__(self, commande, func, exitfunc, readyfunc=None,
                 shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, code="UTF-8"):
        # why the fuck you have code inside?
        """
        commande 命令
        func 正确输出反馈函数
        exitfunc 异常反馈函数
        readyfunc 当管道创建完毕时调用
        """
        self._thread = threading.Thread(target=self.__run, args=(
            commande, shell, stdin, stdout, stderr, readyfunc))
        self._code = code
        self._func = func
        self._exitfunc = exitfunc
        self._flag = False
        # do a check.
        if(platform.system == "Windows"):
            self._CRFL = "\r\n"
        # elif(platform.system=="Linux")
        else:
            self._CRFL = "\n"
        # self._FL="\n"

    def __run(self, commande, shell, stdin, stdout, stderr, readyfunc):
        """ 私有函数 """
        # another func?
        try:
            self._process = subprocess.Popen(
                commande,
                shell=shell,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr
            )
        except OSError as e:
            self._exitfunc(e)
        fun = self._process.stdout.readline
        fun0 = self._process.stderr.readline
        # fuck the readline func.

        def stderrFunc(funX):
            while True:
                line = funX()
                if not line:
                    break
                try:
                    tmp = line.decode(self._code)
                except UnicodeDecodeError:
                    tmp =  \
                        self._CRFL + \
                        "[PIPE_CODE_ERROR] <Code ERROR: UnicodeDecodeError>\n" \
                        + "[PIPE_CODE_ERROR] Now code is: " + \
                        self._code + self._CRFL
                self._func(self, "FROM STDERR: "+tmp)
        self._flag = True
        if readyfunc != None:
            threading.Thread(target=readyfunc).start()  # 准备就绪
            # so do another thread?
            # triple thread? what about now?
            # fucking hell.
            # you can listen to a port. -> webshell.
        threading.Thread(target=stderrFunc, args=(fun0,)).start()
        while True:
            line = fun()
            if not line:
                break
            try:
                tmp = line.decode(self._code)
            except UnicodeDecodeError:
                tmp =  \
                    self._CRFL + \
                    "[PIPE_CODE_ERROR] <Code ERROR: UnicodeDecodeError>\n" \
                    + "[PIPE_CODE_ERROR] Now code is: " + \
                    self._code + self._CRFL
            self._func(self, tmp)

        self._flag = False
        self._exitfunc(LoopException("While Loop break"))  # 正常退出

    def write(self, msg):
        if self._flag:
            # 请注意一下这里的换行
            self._process.stdin.write((msg + self._CRFL).encode(self._code))
            self._process.stdin.flush()
            # sys.stdin.write(msg)#怎么说呢，无法直接用代码发送指令，只能默认的stdin
        else:
            raise LoopException(
                "Shell pipe error from '_flag' not True!")  # 还未准备好就退出

    def start(self):
        """ 开始线程 """
        self._thread.start()

    def destroy(self):
        """ 停止并销毁自身 """
        # not working again?
        self._process.stdout.close()
        self._thread.stop()
        del self


if __name__ == '__main__':  # 那么我们来开始使用它吧
    e = None

    # 反馈函数
    def event(cls, line):  # 输出反馈函数
        sys.stdout.write(line)

    def exit(msg):  # 退出反馈函数
        print(msg)

    def ready():  # 线程就绪反馈函数
        ik = 5
        while ik > 0:
            # e.write("echo hello world")
            e.write("blowjob")
            time.sleep(1)
            ik -= 1
        e.destroy()
        # what the heck?
        # e.write("dir")  # 执行
        # e.write("ping www.baidu.com")
        # e.write("echo Hello!World 你好中国！你好世界！")
        # e.write("exit")

    # e = SwPipe("cmd.exe", event, exit, ready)
    e = SwPipe("bash", event, exit, ready)
    e.start()
# somehow working?
# but no reply.
