from core4 import merge_node
from getFromDill import returnXList
r=returnXList("all_commands")
for x in r:
    merge_node(x)