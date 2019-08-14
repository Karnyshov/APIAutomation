import requests
import pytest
from utils import http_manager
from utils.Api import Api
# from utils import

# r = requests.get("https://the-internet.herokuapp.com/login")
# print(r.status_code)
# print(r.json)


def test_ping_login():
    r = requests.get("https://the-internet.herokuapp.com/login")
    cookie = r.cookies
    print(cookie)
    cookie_new = cookie.get("rack.session")
    print(cookie_new)
    assert 200 == r.status_code


def test_auth():
    r = requests.post("https://the-internet.herokuapp.com/authenticate",
                      {'username': 'tomsmith', 'password': 'SuperSecretPassword!'})
    cookie = r.cookies
    cookie_2 = cookie.get
    header = r.headers
    print(header)
    print(r.text)
    print(cookie)
    assert True == ("Welcome to the Secure Area." in r.text)

#    d = requests.get('https://the-internet.herokuapp.com/logout', cookies=cookie)
#    assert 200 == d.status_code
#    print(d.text)


def test_auth_new():
    result = Api.auth()
#    Cookie cannot be saved here

#    print(result.text)
#    print(result.status_code)
#    assert True == ("Welcome to the Secure Area." in result.text)
