import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
data = urllib.request.urlopen(address).read()
info = json.loads(data)
y = 0
for x in info["comments"]:
    y = y + int((x["count"]))
print(y)
