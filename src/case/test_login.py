import  pytest
import  requests
from jsonpath import jsonpath

class TestLogin:

    @pytest.mark.skip(reason = "skip")
    def test_login_success(self):
        """"
            用户登录成功
        """
        url = "http://www.xxx/api/login"
        data = {"phone": "18212341234", "code": "123456"}
        resp = requests.request(method="post", url=url, json=data)
        assert resp.status_code == 200
        assert jsonpath(resp.json(),"$..msg")[0] == "登录成功"

    def test_login_fail_phone_error(self):
        """"
            用户手机号错误登录失败
        """
        url = "http://www.xxx/api/login"
        data = {"phone": "182123412345", "code": "123456"}
        resp = requests.request(method="post", url=url, json=data)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$..msg")[0] == "登录失败"

    def test_login_fail_code_error(self):
        """"
            用户验证码错误登录失败
        """
        url = "http://www.xxx/api/login"
        data = {"phone": "18212341234", "code": "111222"}
        resp = requests.request(method="post", url=url, json=data)
        assert resp.status_code == 200
        assert jsonpath(resp.json(), "$..msg")[0] == "验证码不正确"