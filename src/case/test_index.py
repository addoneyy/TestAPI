import  pytest
import requests
from  jsonpath import jsonpath

class TestIndex:

    @pytest.mark.skip(reason = "skip")
    def test_index_list(self, get_token):
        """
            获取列表
        :return:
        """
        url = "http://www.xxx/api/tasklist"
        header = {"token": get_token}
        data = {"type": "test"}
        resp = requests.request(method="post", url=url, json=data, headers=header)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$..msg")[0] == "列表获取成功！"

    def test_index_list_token_error(self):
        """
            错误token获取列表失败
        :return:
        """
        url = "http://www.xxx/api/tasklist"
        header = {"token": "1234567"}
        data = {"type": "test"}
        resp = requests.request(method="post", url=url, json=data, headers=header)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$..msg")[0] == "列表获取失败！"