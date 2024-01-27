from getFromDill import returnAList
r=returnAList()
r=[x for y in r for x in y]
for x in r:
    print(x)
