import requests
from pprint import pprint
import webbrowser

post_link = "https://pastebin.com/api/api_post.php"
payload = "{'username' :'john', 'email' : 'john@example.com'}"

API_key = "068ef8c5332427952bd43af129886ca0"

parameters = {
    'api_dev_key': API_key,
    'api_option': 'paste',
    'api_paste_code': payload,
    'api_paste_format': 'python'
}

r_post = requests.post(post_link, data=parameters)

if (r_post.status_code == 200):
    print("The request to the URL was successful.")
    print("You can find the code pasted on this link: {}".format(r_post.text))