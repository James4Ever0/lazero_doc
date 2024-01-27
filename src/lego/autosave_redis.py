import time,os,sys
sv = sys.argv
#print(sv)
tm = 2
if len(sv) == 2:
    tm = int(sv[1])
while True:
    time.sleep(tm)
    os.system("redis-cli bgsave")
