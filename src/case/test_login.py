import  pytest
import  requests
from jsonpath import jsonpath
from src.utils.yamlloader import YamlLoader
from src.utils.validator import Validator

class TestLogin:

    datas = YamlLoader().load(r"data/test_login.yaml")["login"]
    @pytest.mark.parametrize("data", datas)
    def test_login(self, data):
        resp = requests.request(**data["request"])
        assert Validator().validate(data, resp)
        print(f"测试用例[{data['name']}]执行成功")