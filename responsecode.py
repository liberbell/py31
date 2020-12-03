import requests
from pprint import pprint

url1 = "https://example.com"
ok_resp = requests.get(url1)

print(ok_resp.status_code)
print(ok_resp.ok)

url2 = "https://www.yahoo.com/alf2adfd5"
bad_resp = requests.get(url2)

print(bad_resp.status_code)
print(bad_resp.ok)