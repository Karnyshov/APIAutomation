import requests


class Api:
    BASE_URL = "https://the-internet.herokuapp.com/"
    LOGIN_URL = BASE_URL + "login"
    AUTH_URL = BASE_URL + "authenticate"
    LOGOUT_URL = BASE_URL + "logout"

    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"

    def __init__(self):
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self._cookies = {}

    def setCookies(self, key, value):
        self._cookies[key] = value

    def getCookies(self):
        return self._cookies

    def setHeader(self, key, value):
        self._headers[key] = value

    def getHeaders(self):
        return self._headers

    def get(self, url):
        return requests.get(url, headers=self.getHeaders(), cookies=self.getCookies())

    def post(self, url, data):
        return requests.post(url, data=data, headers=self.getHeaders(), cookies=self.getCookies())

    def login(self, username=USERNAME, password=PASSWORD):
        url = Api.AUTH_URL
        data = {'username': username, 'password': password}

        response = self.post(url, data)
        self.setCookies('rack.session', response.cookies.get('rack.session'))

        assert 200 == response.status_code
        assert True == ("Welcome to the Secure Area." in response.text)

        return response
