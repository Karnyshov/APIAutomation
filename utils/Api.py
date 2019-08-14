from utils.http_manager import HttpManager


class Api:
    BASE_URL = "https://the-internet.herokuapp.com/"
    LOGIN_URL = BASE_URL + "authenticate"
    LOGOUT_URL = BASE_URL + "logout"

    def __init__(self):
        self._httpManager = HttpManager()

    def getHttpManager(self):
        return self._httpManager

    def login(self):
        url = Api.LOGIN_URL
        username = "tomsmith"
        password = "SuperSecretPassword!"
        data = {'username': username, 'password': password}

        response = self._httpManager.post(url, data)
        # TODO: save cookie in Api.py or http_manager.py
        self._httpManager.setCookies('rack.session', response.cookies.get('rack.session'))

        return response
