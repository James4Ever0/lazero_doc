# say it is possible?
# done several times to see if it is working?
imp=0
while imp<3:
    try:
        int(str)
        print("possible")
        break
    except:
        imp+=1
        print("not working")
        pass
# print()