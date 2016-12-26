#!/usr/bin/env
# by sfzhang 2016.11.22

import requests
from urllib.request import urlopen
with urlopen("http://www.apple.com") as urlfile:
    for i in urlfile:
        print(i)
    urlfile.close()
request_obj = requests.request("GET", "http://www.apple.com")
print("#" * 100)
print(request_obj.content)
print("status code:", request_obj.status_code)
print(request_obj.text)



