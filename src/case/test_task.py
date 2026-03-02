from src.utils.requests import http_request
from jsonpath import jsonpath as jp

class TestTask:


    def __get_task_type(self, token):
        """
            获取任务
        """
        url = "http://127.0.0.1:xxxx/task/get/task"
        headers = {"token": token}
        resp = http_request.request("get", url=url, headers=headers)
        assert resp.status_code == 200
        assert len(jp(resp.json(), '$.data')[0]) == 2

        return True

    def __upload_imgs(self, token):
        """
            上传图片
        """
        url = "http://127.0.0.1:xxxx/task/upload/task"
        headers = {"token": token}
        image = [("file", ('IMG_5977.JPG', open(r"data/imgs/IMG_5977.JPG"), 'image/jpeg'))]
        resp = http_request.request("post", url=url, data=image, headers=headers)
        assert resp.status_code == 200
        image_name = jp(resp.json(),'$.data')[0]

        return True, image_name

    def __submit_task(self, token, image_name):
        """
            提交任务
        """
        url = "http://127.0.0.1:xxxx/task/submit/task"
        headers = {"token": token}
        json = {"title": "测试任务", "content": "123123123", "type": 42, "imglist": [image_name],
                "start_time": "2024-07-19 17:12"}
        resp = http_request.request("post", url=url, json=json, headers=headers)
        assert resp.status_code == 200
        assert jp(resp.json(), '$.msg')[0] == "操作成功！"
        psid = jp(resp.json(), '$..id')[0]

        return True, psid

    def __pay_order(self, token="", psid="", payps="123456"):
        """
            支付订单
        """
        url = "http://127.0.0.1:xxxx/task/pay/task"
        json = {"id": psid, "payps": payps}
        headers = {"token": token}
        resp = http_request.request("post", url=url, json=json, headers=headers)
        assert resp.status_code == 200

        return True

    def create_task(self, get_token):
        """
            创建任务业务流用例
            创建任务有两种方式：1.调用接口 2.操作数据库
        """
        self.token = get_token
        assert self.__get_task_type()
        assert self.__upload_imgs()
        assert self.__submit_task()
        assert self.__pay_order()

    def test_reveice_task(self, get_token, create_task):
        """
            测试接受任务成功
        """
        task_id = create_task
        url = "http://127.0.0.1:xxxx/task/receive/task"
        headers = {"token": get_token}
        json = {"id": task_id}
        resp = http_request.request(method="post", url=url, json=json, headers=headers)
        assert resp.status_code == 200
