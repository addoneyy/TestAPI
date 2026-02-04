import  requests
from jsonpath import jsonpath

class TestLogin:
    def test_login_success_01(self):
        """"
            用户登录成功
        """
        url = "http://www.xxx/api/login"
        data = {"phone": "18212341234", "code": "123456"}
        resp = requests.request(method="post", url=url, json=data)
        assert resp.status_code == 200
        assert jsonpath(resp.json(),"$..msg")[0] == "登录成功"