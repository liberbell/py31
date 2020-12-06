import requests
from pprint import pprint
from requests import exceptions

url1 = "https://nonexistence.com"

resp1 = requests.get(url1)