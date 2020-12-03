import requests
from pprint import pprint

url1 = "https://gmail.com"

resp1 = requests.get(url1)
print(resp1.status_code)
print(resp1.history)
print(resp1.url)

if resp1.history:
    print("Redirect history:")
    for resp in resp1.history:
        print(resp.status_code, resp.url)
    
    print("\nFinal destination:")
    print(resp1.status_code, resp1.url)

else:
    print("Request was not redirected:")
    print(resp1.status_code, resp1.url)