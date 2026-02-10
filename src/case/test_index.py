import requests
from  jsonpath import jsonpath

class TestIndex:
    def test_index_list(self, get_token):
        """
            获取列表
        :return:
        """
        url = "http://www.xxx/api/login"
        header = {"token": get_token}
        data = {"type": "test"}
        resp = requests.request(method="post", url=url, json=data, headers=header)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$.msg")[0] == "列表获取成功！"

