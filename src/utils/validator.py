from jsonpath import jsonpath as jp
import traceback

class Validator:

    @staticmethod
    def eq(r1, r2):
        return r1 == r2

    @staticmethod
    def nq(r1, r2):
        return r1 != r2

    @staticmethod
    def iin(r1, r2):
        return r1 in r2

    @staticmethod
    def nin(r1, r2):
        return r1 not in r2

    def validate(self, data, resp):
        """
            结果校验函数
        """
        try:
            for check_items in data["validate"]:
                for k, v in check_items.items():
                    if v[0] == "status_code":
                        assert getattr(Validator, k)(resp.status_code, v[1])
                    elif "$." in v[0]:
                        assert getattr(Validator, k)(jp(resp.json(), v[0])[0], v[1])
        except:
            traceback.print_exc()
            return False

        return True