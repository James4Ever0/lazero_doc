#import urllib.parse
import sys
# binary inside.
for x in sys.stdin.buffer:
    print(type(x),len(x))
    # too slow. maybe using multi rgs?
