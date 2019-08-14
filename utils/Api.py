import requests
from utils.http_manager import HttpManager


class Api:
    BASE_URL = "https://the-internet.herokuapp.com/"
    LOGIN_URL = BASE_URL + "authenticate"
    LOGOUT_URL = BASE_URL + "logout"

    @staticmethod
    def auth():
        url = Api.LOGIN_URL
        username = "tomsmith"
        password = "SuperSecretPassword!"
        data = {'username': username, 'password': password}

        result = requests.post(url, data)
        # print(result.cookies)
        # TODO: save cookie in Api.py or http_manager.py
        HttpManager.cookie = {'rack.session': result.cookies.get('rack.session')}
        print("API Cookie")
        print(HttpManager.cookie)

        return result
