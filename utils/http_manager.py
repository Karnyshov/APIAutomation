import requests


class HttpManager:
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    cookie = {}

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpManager.header, cookies=HttpManager.cookie)

        return result

    @staticmethod
    def post(url, data):
        result = requests.post(url, data=data, headers=HttpManager.header, cookies=HttpManager.cookie)

        return result
