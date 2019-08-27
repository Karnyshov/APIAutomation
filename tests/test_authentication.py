from utils.template import Template


class TestFlow(Template):

    def test_ping_login(self):
        response = self.api.get(self.api.LOGIN_URL)
        assert 200 == response.status_code
        assert True == ("This is where you can log into the secure area." in response.text)

    def test_auth_new(self):
        response = self.api.login()
        assert 200 == response.status_code
        assert True == ("Welcome to the Secure Area." in response.text)

    def test_logout_new(self, authentication):
        response = self.api.get(self.api.LOGOUT_URL)
        assert 200 == response.status_code
        assert True == ("This is where you can log into the secure area." in response.text)
