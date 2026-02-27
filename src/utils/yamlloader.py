import traceback
import yaml

class YamlLoader:

    def load(self, path):
        """
            读取yaml文件
        """
        result = None
        try:
            with open(file=path, mode='r', encoding="utf-8") as f:
                result = yaml.load(stream=f.read(), Loader= yaml.FullLoader)
                return result
        except:
            traceback.print_exc()
            return result


if __name__ == '__main__':
    loader = YamlLoader()
    resp = loader.load(r"data/test_login.yaml")
    print(resp)