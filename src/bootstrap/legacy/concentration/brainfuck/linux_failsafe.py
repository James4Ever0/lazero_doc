def commandFuse(a, f=1):
    assert type(f) in [float, int] and f > 0
    assert type(a) == str and len(a) > 0
    return "timeout {} {}".format(f, a)
# now, time to check if you can read shit?