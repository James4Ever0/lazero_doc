import sys
import uuid
uid = str(uuid.uuid4())
print("init",uid)
for x in sys.stdin:
    print([x],uid)
