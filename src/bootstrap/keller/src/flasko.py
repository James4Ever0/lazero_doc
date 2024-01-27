# encoding: utf-8
"""
@version: v1.0
@author: W_H_J
@license: Apache Licence
@contact: 415900617@qq.com
@software: PyCharm
@file: flaskWebSocket.py
@time: 2019/2/19 10:20
@describe: flask_sockets 实现websocket
"""
import json
import sys
import os
from flask_sockets import Sockets
import time
#from threading import Thread
from gevent import monkey
from flask import Flask, request
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
monkey.patch_all()
 
app = Flask(__name__)
sockets = Sockets(app)
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
 
 
@sockets.route('/',defaults={'path': ''})  # 指定路由
@sockets.route('/<path:path>')
def echo_socket(ws,path):
    while not ws.closed:
        print("WS: ",path)
        ws.send("1+250")  # 回传给clicent
        """ 服务端必须接收到客户端发的消息才能保持该服务运行，如果ws.receive()没有接收到客户端发送的
         消息，那么它会关闭与客户端建立的链接
         底层解释：Read and return a message from the stream. If `None` is returned, then
        the socket is considered closed/errored.
        所以客户端只建立连接，不与服务端交互通信，则无法实现自由通信状态，之后在客户端代码处会有详细内容。
         """
        message = ws.receive()  # 接收到消息
        if message is not None:
            print("%s receive msg==> " % now, str(json.dumps(message)))
            def sendmsg():
                time.sleep(0.5)
                ws.send(str(json.dumps(message)))  # 回传给clicent
            sendmsg()
            #Thread(target=sendmsg,args=()).start()
            """ 如果客户端未发送消息给服务端，就调用接收消息方法，则会导致receive()接收消息为空，关闭此次连接 """
        else:
            print(now, "no receive")
 
 
@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    print("HTTP: ",path)
    return 'Hello World! server start！'
 
 
if __name__ == "__main__":
    server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
