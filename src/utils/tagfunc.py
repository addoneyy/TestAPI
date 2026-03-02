from src.utils.requests import http_request
from  jsonpath import jsonpath as  jp
from src.utils.yamlloader import YamlLoader


def get_user_token(loader=None, node=None):
    """
        获取token的pyyaml自定义标签
    """
    INIT_DATA = YamlLoader().load(r"data/test_login.yaml")["login"]["variables"]
    url = "http://www.xxx/api/login"
    resp = http_request.request(url=url, method="post", json=INIT_DATA)
    assert resp.status_code == 200

    return jp(resp.json(), '$..token')[0]