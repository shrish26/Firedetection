import json

from urllib.request import urlopen

url = 'http://ipinfo.io/json'
res = urlopen(url)
data = json.load(res)
print(data)
json_object = json.dumps(data, indent=4)
with open("location.json", "w") as outfile:
    outfile.write(json_object)