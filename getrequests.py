import requests
from pprint import pprint
import json

print(requests.__version__)
print(requests.__copyright__)

url1 = "https://www.metaweather.com/api/location/2487956/2020/11/24" 
r_get = requests.get(url1)