import requests
from pprint import pprint
from requests import exceptions

url1 = "https://nonexistent.com"

resp1 = requests.get(url1)