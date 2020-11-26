import requests
import webbrowser

url = "https://www.wikipedia.org"
resp_obj = requests.get(url)

print(resp_obj.url)
webbrowser.open(resp_obj.url)