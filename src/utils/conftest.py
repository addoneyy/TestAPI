import pytest
import requests
from jsonpath import jsonpath


@pytest.fixture(scope='function', params=[{"phone": "18212341234", "code": "123456"},], ids=['login_success'])
def get_token(request):
    """
        获取token
    """
    url = "http://www.xxx/api/login"
    resp = requests.request(method="post", url=url, json= request.params)
    assert resp.status_code == 200

    yield  jsonpath(resp.json(), '$..token')[0]
