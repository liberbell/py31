import requests
from pprint import pprint

r_post = requests.post("https://en.wikipedia.org/w/index.php", data = {'search' : 'skillsoft'})

# print(r_post.status_code)
# print(type(r_post))

# pprint(r_post.text)
# print(r_post.url)

# with open("skillsoft.html", "wb") as f:
#     for chunk in r_post.iter_content(chunk_size=10000):
#         f.write(chunk)

# r_post = requests.post("https://httpbin.org/post")
# print(r_post.status_code)
# print(type(r_post))

# pprint(r_post.text)
# print(r_post.url)

url = "https://httpbin.org/post"
files = {"files": open("test.txt", "rb")}
value = {"upload_file" : "test.txt", "OUT" : "csv"}