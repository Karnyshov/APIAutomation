import requests


class HttpManager:
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
