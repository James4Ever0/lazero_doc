import re,sys
for x in sys.stdin:
    rf = re.findall(r"\d+",x)
    if len(rf)>0:
        print(rf[0])
