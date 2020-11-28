import requests
from pprint import pprint

r_post = requests.post("https://en.wikipedia.org/w/index.php", data= {'search' : 'skillsoft'})

print(r_post.status_code)
print(type(r_post))

pprint(r_post.txt)