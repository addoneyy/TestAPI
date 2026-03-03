import traceback
import yaml
from copy import deepcopy
import  re
from src.utils.tagfunc import get_user_token

class YamlLoader:

    TAGS = [
        {"!get_token": get_user_token},
    ]

    def __init__(self, tags= TAGS):
        for tag in tags:
            for k, v in tag.items():
                yaml.add_constructor(k, v)


    def load(self, path):
        """
            读取yaml文件
        """
        result = None
        try:
            with open(file=path, mode='r', encoding="utf-8") as f:
                result = yaml.load(stream=f.read(), Loader= yaml.FullLoader)
                result =result if r"conf" in path and r"data" not in path else self.__replace_vars(result)
                return result
        except:
            traceback.print_exc()
            return result

    def __replace_vars(self, datas, replace = False):
        """
            替换variable的所有变量值
        """
        datas_copy = {}

        for k, v in datas.items():
            datas_copy[k] = []
            if isinstance(v, list):
                for case in v:
                    case_copy = str(deepcopy(case))
                    if isinstance(case, dict) and case.get("variables"):
                        for k1 ,v1 in case["variables"].items():
                            find_result = re.findall("\${"+k1+"}", case_copy)
                            for res in find_result:
                                case_copy = case_copy.replace(res,v1)

                    datas_copy[k].append(eval(case_copy))
            else:
                datas_copy[k] = deepcopy(v)
        return  datas_copy



if __name__ == '__main__':
    loader = YamlLoader()
    resp = loader.load(r"data/test_login.yaml")
    print(resp)
