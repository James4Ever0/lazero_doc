def checkFuzzy(a, b, sigma=0.4):
    c = abs(len(a)-len(b))
    r = a.intersection(b)
    d = int((len(a)+len(b))/2)
    return len(r) >= (d-c*sigma)


# already useful.
if __name__ == "__main__":
    a = set("remainder")
    b = set("reminder")
    # c = set("remin")  # what the fuck?
    c = set("s")
    print(checkFuzzy(a, b), checkFuzzy(a, c), checkFuzzy(b, c))
