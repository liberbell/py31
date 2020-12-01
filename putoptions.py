import requests
from pprint import pprint
import json

URL = "https://httpbin.org/put"
URL2 = "https://httpbin.org/get"
URL3 = "https://httpbin.org/delete"
r_put = requests.put(URL, data={'key': 'value'})

# print(r_put.status_code)
# # print(r_put.text)

# r_option = requests.options(URL2)
# print(type(r_option))
# print(r_option.text)

# pprint(r_option.headers)

r_delete = requests.delete(URL3)
print(r_delete.status_code)
print(type(r_delete))

print(r_delete.text)