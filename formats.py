import requests
from pprint import pprint
import json

url1 = "https://swapi.dev/api/vehicles/4/"
resp_obj = requests.get(url1)
print(resp_obj.status_code)
print(type(resp_obj))

pprint(resp_obj.json())