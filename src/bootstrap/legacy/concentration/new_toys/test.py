from process_dom import bing_dom

with open("strange.html","r") as f:
    f0=bing_dom(f.read())
    print("spliter_____________________-")
    print(f0)
