import requests
from  jsonpath import jsonpath

class TestIndex:
    def test_index_list(self):
        """
            获取列表
        :return:
        """
        url = "http://www.xxx/api/login"
        header = {"token": "jw8d1i903whjcdf0193jfdci8h23989"}
        data = {"type": "test"}
        resp = requests.request(method="post", url=url, json=data, headers=header)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$.msg")[0] == "列表获取成功！"

