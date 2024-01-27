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
 
# when using wifi, it is damn easy to get yourself blocked. static ip. so use browser to get fresh cookies, in case of nasty shits. 
@sockets.route('/',defaults={'path': ''})  # 指定路由
@sockets.route('/<path:path>')
def echo_socket(ws,path):
    while not ws.closed:
        print("WS: ",path)
        ws.send(str("message test!"))  # 回传给clicent
        # this is just a heartbeat package. check the content first.
        """ 服务端必须接收到客户端发的消息才能保持该服务运行，如果ws.receive()没有接收到客户端发送的
         消息，那么它会关闭与客户端建立的链接
         底层解释：Read and return a message from the stream. If `None` is returned, then
        the socket is considered closed/errored.
        所以客户端只建立连接，不与服务端交互通信，则无法实现自由通信状态，之后在客户端代码处会有详细内容。
         """
        message = ws.receive()  # 接收到消息
        if message is not None:
            print("%s receive msg==> " % now, str(json.dumps(message)))
            """ 如果客户端未发送消息给服务端，就调用接收消息方法，则会导致receive()接收消息为空，关闭此次连接 """
#            ws.send(str(json.dumps(message)))  # 回传给clicent
# this connection is not async. check async websocket.
            time.sleep(1)
# wait for a while. shall we?
            ws.send("https://www.baidu.com/s?wd=how+to+kill+your+father%0A")
            # to disable the protocol, you might need another background script.
            # sending string. check data type.
            # natural clustering.
        else:
            print(now, "no receive")
 
 
@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    print("HTTP: ",path)
    return 'Hello World! server start！'
 
 
if __name__ == "__main__":
    server = pywsgi.WSGIServer(('localhost', 7777), app, handler_class=WebSocketHandler,keyfile="certs/server.key",certfile="certs/server.crt")
    #server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler,keyfile="certs/ca/ca.key",certfile="certs/ca/ca.crt")
    print('server start')
    server.serve_forever()
