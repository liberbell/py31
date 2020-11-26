import requests
import webbrowser

url = "https://www.wikipedia.org"
resp_obj = requests.get(url)

print(resp_obj.url)