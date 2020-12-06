import requests
from pprint import pprint
from requests import exceptions

url1 = "https://nonexistent.com"
url2 = "https://github.com"

# resp1 = requests.get(url1)

try:
    requests.get(url1)
except exceptions.ConnectionError:
    print("Error: Connection error")

resp2 = requests.get(url2, timeout=0.001)