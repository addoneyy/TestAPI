import  pytest
from src.utils.requests import http_request
from src.utils.yamlloader import YamlLoader
from src.utils.validator import Validator

class TestLogin:

    @pytest.mark.parametrize("data", YamlLoader().load(r"data/test_login.yaml")["login"])
    def test_login(self, data):
        resp = http_request.request(**data["request"])
        assert Validator().validate(data, resp)
        print(f"测试用例[{data['name']}]执行成功")