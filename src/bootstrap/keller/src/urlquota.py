import requests
quota=5
for x in range(quota):
    r=requests.get(input("url:\n"))
    print(r.text)
