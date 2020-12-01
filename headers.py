import requests
from pprint import pprint

url = "https://swapi.dev/api/people/3"

header1 = {'user-agent' : 'Google Chrome'}
resp = requests.get(url, headers = header1)

# print(resp.status_code)
# print(type(resp))
# print(resp.headers)
# print(resp.headers['content-type'])

url2 = "https://en.wikipedia.org/wiki/Monty_Python"
# resp_obj = requests.get(url2)

# print(resp_obj.headers)
# print(resp_obj.request.headers)

url3 = "https://httpbin.org/user-agent"
header2 = {'user-agent' : 'Internet Explorer/2.0'}

r = requests.get(url3, headers=header2)
data = r.json()
print(data)