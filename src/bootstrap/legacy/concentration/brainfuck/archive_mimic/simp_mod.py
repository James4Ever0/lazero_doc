def test(a, b):
    return a in b


a = [(12+x) % 24 for x in range(24)]
b = [(12+9++x) % 24 for x in range(24)]
c = list(range(10, 24))
d = zip(a, b)
e = list(filter(lambda x: test(x[0], c) and test(x[1], c), d))
for x in e:
    print(x)
    # this ain't funny.