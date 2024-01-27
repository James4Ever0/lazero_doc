from bs4 import BeautifulSoup
def soup(a):
    return BeautifulSoup(a,features="html.parser")

def openShit(b):
    return b

def shit(x):
    try:
        s=soup(openShit(x)).find_all(name="ul",attrs={"class":"repo-list"})[0].find_all(name="a",attrs={"class":"v-align-middle"},recursive=True)
        return [s0.get_text() for s0 in s]
    except:
        return []

# fuck you.

#e=[[shit(c) for c ]]
#print(len(d))
