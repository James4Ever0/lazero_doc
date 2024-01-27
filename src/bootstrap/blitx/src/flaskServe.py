from flask import Flask, request
import threading
import pytesseract
import time
import copy
import io
from PIL import Image

def scanner(mainfile,filerefresh):
    while True:
        if (filerefresh[0]):
            try:
                data=copy.copy(mainfile[0])
                #print(type(data),len(data))
                image = Image.open(io.BytesIO(data))
                text = pytesseract.image_to_string(image,lang='eng') #使用简体中文解析图片
                # so goddamn slow.
                # but it is because without direct access.
                print(text)
                filerefresh[0]=False
            except:
                #print("MISSED")
        else:
            time.sleep(1)
mainfile=[None]
filerefresh=[False]
app = Flask(__name__)
@app.route('/sample', methods=['POST'])
# use a separate thread to process this saving thing.
def result():
    # get all things.
    #print(request.data)
    files=request.files
    form=request.form
    pr=[files[x] for x in list(files)]
    pr0=[form[x] for x in list(form)]
    if len(pr0)==1:
        if pr0[0]=="screenshot":
            mainfile[0]=pr[0].read()
            filerefresh[0]=True
            #print(pr[0])
    #print(request.form['foo']) # should display 'bar'
    return 'Received !' # response to your request.

p=threading.Thread(target=scanner,args=(mainfile,filerefresh))
p.setDaemon(True)
p.start()
app.run(port=4999)
