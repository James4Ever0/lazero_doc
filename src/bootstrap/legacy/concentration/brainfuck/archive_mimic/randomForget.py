import random
def r(a):
    l= len(a)
    b=list(a)
    b[random.choice(range(l))]=""
    return "".join(b)

if __name__ == '__main__':
    k="torch is the besh shit ever"
    while True:
        print(k)
        k=r(k)