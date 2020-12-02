import requests
from pprint import pprint

resp_obj = requests.get("https://httpbin.org")
print(resp_obj.status_code)
print(resp_obj.encoding)

resp_obj.encoding = "ISO 8859-1"
print(resp_obj.encoding)

resp_obj = requests.get("https://github.com/timeline.json")
print(resp_obj.status_code)
print(resp_obj.encoding)

pprint(resp_obj.text)
resp_obj.encoding = "ISO-8859-1"
pprint(resp_obj.text)

from PIL import Image
from io import BytesIO

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Moon_and_Aurora.jpg/320px-Moon_and_Aurora.jpg"
url2 = "https://upload.wikimedia.org/wikipedia/commons/4/4c/Moon_and_Aurora.jpg"

resp = requests.get(url)
print(resp.status_code)
print(type(resp.content))