import requests
from pprint import pprint
import json

URL = "https://httpbin.org/put"
r_put = requests.put(URL, data={'key': 'value'})