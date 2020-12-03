import requests
from pprint import pprint

url1 = "https://gmail.com"

resp1 = requests.get(url1)
print(resp1.status_code)