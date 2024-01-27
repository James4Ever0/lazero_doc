import redis   # 导入redis 模块
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)   
r.set('name', 'runoob',ex=3)  # 设置 name 对应的值
while True:
    try:
        print(r['name'])
        print(r.get('name'))  # 取出键 name 对应的值
        print(type(r.get('name')))
    except:
        print("expired")
    time.sleep(1)
