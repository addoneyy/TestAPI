from src.utils.requests import http_request
from  jsonpath import jsonpath as  jp
from src.utils.yamlloader import YamlLoader


def get_user_token(loader=None, node=None):
    """
        获取token的pyyaml自定义标签
    """
    #解决循环导入
    from src.utils.yamlloader import YamlLoader
    INIT_DATA = YamlLoader().load(r"data/init_data.yaml")["get_user_token"]
    url = "http://www.xxx/api/login"
    resp = http_request.request(url=url, method="post", json=INIT_DATA)
    assert resp.status_code == 200

    return jp(resp.json(), '$..token')[0]