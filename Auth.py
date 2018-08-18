import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def config(username, password):

    url = 'http://127.0.0.1:5000/'
    post_fields = {
        'username': username,
        'password': password
    }
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
