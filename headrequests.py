import requests
from pprint import pprint
import json

r_head = requests.head("https://example.com")
print(r_head.status_code)
print(r_head.text)
print(r_head.content)

pprint(r_head.headers)