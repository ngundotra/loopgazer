import pickle
from urllib.parse import urlencode
from urllib.request import Request, urlopen

base_url = 'http://127.0.0.1:5000'

def create_user(usr, pwd):
    """
    Returns an HTTPResponse object from attempting to create a user
    """
    ext = '/create-acct'
    url = base_url + ext
    usrcred = {
        'username': usr,
        'password': pwd
    }

    request = Request(url, urlencode(usrcred).encode())
    return urlopen(request)

def post_progress(usr, pwd, prog):
    """
    Given a float(prog), will post to server
    """
    form = {'username': usr,
            'password': pwd,
            'progress': prog}
    ext = '/progress'
    url = base_url + ext
    request = Request(url, urlencode(form).encode())
    return urlopen(request)


def get_progress(usr, pwd):
    """
    Attempts to retrieve loop progress
    """
    form = {'username': usr,
            'password': pwd}
    request = Request(base_url, urlencode(form).encode())
    return urlopen(request)


def change_pwd(usr, pwd, new_pwd):
    """
    Attempts to change the user's password
    """
    ext = '/change-acct'
    url = base_url + ext
    form = {'username': usr,
            'password': pwd,
            'new_password': new_pwd}
    request = Request(url, urlencode(form).encode())
    return urlopen(request)


def validate_usr(usr, pwd):
    """
    Returns True if user is valid, otherwise False
    """
    ext = '/validate'
    url = base_url + ext
    form = {'username': usr,
            'password': pwd}
    request = Request(url, urlencode(form).encode())
    return urlopen(request)