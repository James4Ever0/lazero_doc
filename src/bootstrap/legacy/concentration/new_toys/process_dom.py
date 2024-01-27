from bs4 import BeautifulSoup
#import traceback
def proc1(z):
    f=list(z.select("a"))[0]["href"]
    g=z.text
    return (f,g)

def proc2(z):
    return z.text

def proc0(x):
    r=[]
    for y in x:
        try:
            rg=(proc1(y[0]),proc2(y[1]))
            # use negative numbers instead.
            # really?
            r.append({"link":rg[0][0],"title":rg[0][1],"brief":rg[1]})
        except:
            pass
    return r

def bing_dom(a0):
    global_x=0
    entry=[]
    # with a0 as ecological_pyramid:
    soup = BeautifulSoup(a0, features="lxml")
    producer_entries = soup.find_all('li')
    # print(producer_entries)
#print(type(producer_entries))
    for x in producer_entries:
#        print(">>>entry<<<")
        try:
            e=int(x["data-bm"])
            #print(e,type(e))
            f=x["class"]
#            print(f)
            assert "b_algo" in f
            assert e>global_x
            global_x=e
#            g=list(x.find_all("h2"))
            try:
                g=x.select("h2")
#                print(g)
                g=list(g)
                assert len(g)==1
                h=x.select("div")
                yh=None
                for y in h:
                    try:
                        assert "b_caption" in y["class"]
                        yh=list(y.select("p"))
#                        print(yh)
                        assert len(yh)==1
                    except:
                        pass
                if yh is not None:
                    entry.append((g[0],yh[0]))
            except:
#                print(traceback.format_exc())
                pass
        except:
            pass
    # print(entry)
    ef=proc0(entry)
    return ef

    #for z in ef:
    #    print(z)
# string.
# with open('brim.html', 'r') as f:
#     f0=f.read()
#     s=bing_dom(f0)
#     print(s)