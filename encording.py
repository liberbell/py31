import requests
from pprint import pprint

resp_obj = requests.get("https://httpbin.org")
print(resp_obj.status_code)