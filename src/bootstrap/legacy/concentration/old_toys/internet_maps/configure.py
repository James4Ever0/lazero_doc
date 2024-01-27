from dbM import createMain, initial
from basepak import getRange

# format is png.
createMain()
for x in range(11):
    g=getRange(x)
    g=[(x,a,b) for a,b in g]
    initial("projects",g)
    print("configured",x)