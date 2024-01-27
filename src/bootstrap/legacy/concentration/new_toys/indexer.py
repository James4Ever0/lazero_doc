from getFromDill import returnXList


def getlower(a, b):
    return [x for x in a if b.lower() in x.lower()]


def juicy(a, b):
    return [x for x in a if set(b.lower()).issubset(set(x.lower()))]


def positive(a, x, c):
    if c:
        return getlower(a, x)
    else:
        return juicy(a, x)


r = returnXList("shredded_realcode")
while True:
    try:
        c = input("mode: N/S - normal/set\n")
        assert type(c) == str and c in ["N", "S"]
        if c == "N":
            c = False
            break
        c = True
        break
    except Exception as err:
        print("wrong mode!")
        continue
a = input("query:\n")
for x in r.keys():
    i = positive(r[x], a, c)
    if i != []:
        print("lazero_playground/"+x)
        # print(str(r)[:100])  # still working.
