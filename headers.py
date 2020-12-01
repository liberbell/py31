import requests
from pprint import pprint

url = "https://swapi.dev/api/people/3"

header1 = {'user-agent' : 'Google Chrome'}
resp = requests.get(url, headers = header1)

print(resp.status_code)
print(type(resp))
print(resp.headers)