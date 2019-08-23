from utils.api import Api
from utils.template import Template


class TestFlow(Template):

    def test_ping_login(self):
        api = Api()
        response = api.get(api.LOGIN_URL)
        assert 200 == response.status_code
        print(response.text)
        assert True == ("This is where you can log into the secure area." in response.text)

    def test_auth_new(self):
        api = Api()
        response = api.login()

        print('-->', api.getCookies())
        print(response.text)
        print(response.status_code)
        assert True == ("Welcome to the Secure Area." in response.text)

    def test_logout(self):
        api = Api()
        api.login()
        response = api.get(api.LOGOUT_URL)

        assert 200 == response.status_code
        assert True == ("This is where you can log into the secure area." in response.text)
        print(response.text)

    def test_logout_new(self, authentication):
        response = self.api.get(self.api.LOGOUT_URL)

        assert 200 == response.status_code
        assert True == ("This is where you can log into the secure area." in response.text)
        print(response.text)
