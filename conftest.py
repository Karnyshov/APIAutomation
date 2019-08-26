import pytest
from utils.api import Api


@pytest.fixture()
def authentication():
    api = Api()
    response = api.login()

    assert 200 == response.status_code
    assert True == ("Welcome to the Secure Area." in response.text)

    print("\n")
    print(response.status_code)
    print("\n")
    print(response.text)
