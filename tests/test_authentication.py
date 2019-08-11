import requests
import pytest

# r = requests.get("https://the-internet.herokuapp.com/login")
# print(r.status_code)
# print(r.json)


def test_ping_login():
    r = requests.get("https://the-internet.herokuapp.com/login")
    cookie = r.cookies
    print(cookie)
    assert 200 == r.status_code
