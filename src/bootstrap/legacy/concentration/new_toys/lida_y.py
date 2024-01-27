from batch_wheel import main
from getFromDill import returnXList
from storeADill import storeXList
import copy
import time
if __name__ == "__main__":
    r = returnXList("rockstars")
    # r = returnXList("rock")
    f = copy.copy(r)
    r0 = [x for x in r.keys() if not r[x]]
    for y in r0:
        main(y,2)
        f.update({y: True})
        storeXList(f, "rockstars")
        time.sleep(5)
# need for failsafe.
