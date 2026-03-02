import  pytest
import requests
from src.utils.yamlloader import YamlLoader
from src.utils.validator import Validator

class TestIndex:



    @pytest.mark.parametrize("data", YamlLoader().load(r"data/test_index.yaml")["index"])
    def test_index_list(self, data):
        resp = requests.request(**data["request"])
        assert Validator().validate(data, resp)
        print(f"测试用例[{data['name']}]执行成功")
