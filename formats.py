import requests
from pprint import pprint
import json

url1 = "https://swapi.dev/api/vehicles/4/"
resp_obj = requests.get(url1)
print(resp_obj.status_code)
print(type(resp_obj))

pprint(resp_obj.json())
print(resp_obj.headers["content-type"])

url2 = "https://www.yahoo.com"
resp = requests.get(url2)
print(resp.status_code)
print(resp.headers["content-type"])

url3 = "https://maps.googleapis.com/maps/api/geocode/json"
resp_obj = requests.get(url3)
print(resp_obj.status_code)
print(resp_obj.headers["content-type"])
print(resp_obj.json())

url4 = "https://swapi.dev/api/vehicles/4/"
resp_obj = requests.get(url4, stream=True)
print(resp_obj.status_code)
print(resp_obj.raw)
print(resp_obj.raw.read(10))