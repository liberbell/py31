import requests
from pprint import pprint

url1 = "https://gmail.com"
url2 = "https://www.yahoo.co.jp"
url3 = "https://google.com"
url4 = "https://github.com"

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

print(resp1.is_redirect)
print(resp1.is_permanent_redirect)
print(resp1.history[0].is_redirect)

resp2 = requests.get(url3, allow_redirects=False)
print(resp2.status_code)
print(resp2.history)

resp_head = requests.head(url3, allow_redirects=True)
print(resp_head.status_code)
print(resp_head.history)

# resp3 = requests.get(url4, timeout=0.001)
# print(resp3.status_code)
# print(resp3.history)

resp4 = requests.get(url4, timeout=(5, 18))
print(resp4.status_code)
print(resp4.history)