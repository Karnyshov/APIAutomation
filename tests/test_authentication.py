import requests
import pytest

# r = requests.get("https://the-internet.herokuapp.com/login")
# print(r.status_code)
# print(r.json)


def test_ping_login():
    r = requests.get("https://the-internet.herokuapp.com/login")
#    cookie = r.cookies
#    print(cookie)
    assert 200 == r.status_code


def test_auth():
    r = requests.post("https://the-internet.herokuapp.com/authenticate",
                      {'username': 'tomsmith', 'password': 'SuperSecretPassword!'})
    cookie = r.cookies
    assert True == ("Welcome to the Secure Area." in r.text)

    d = requests.get('https://the-internet.herokuapp.com/logout', cookies=cookie)
    assert 200 == d.status_code
    print(d.text)
