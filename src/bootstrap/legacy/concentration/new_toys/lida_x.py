from been_well import main
from getFromDill import returnXList
from storeADill import storeXList
import copy
if __name__ == "__main__":
    r = returnXList("rockstar")
    # r = returnXList("rock")
    f = copy.copy(r)
    r0 = [x for x in r.keys() if not r[x]]
    for y in r0:
        main(y)
        f.update({y: True})
        storeXList(f, "rockstar")
# need for failsafe.
