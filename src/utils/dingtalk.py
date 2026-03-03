import time
import hmac
import hashlib
import base64
import urllib.parse
from src.utils.logger import logger
import requests
from jsonpath import jsonpath
import traceback
import jenkins


class JenkinReader:

    @staticmethod
    def get_msg():

        job_name = "咱羊自动化测试"
        url = "http://127.0.0.1:8080/"
        username = "username"
        password = "28374r9348593248r5902349r92"
        server = jenkins.Jenkins(url, username, password, timeout=60)
        job_info = server.get_job_info(job_name, fetch_all_builds=True)

        last_build_url = urllib.parse.unquote(job_info["builds"][0]["url"])
        last_build_report_url = last_build_url + "allure/"

        with open(file=r"results\results.txt", mode="r",encoding="utf-8") as f:
            count, passed, failed, skipped = f.read().split(":")

        msg = f"""{job_name}测试结果:
执行总数：{count}
通过数量：{passed}
失败数量：{failed}
跳过执行：{skipped}
构建地址：\n{last_build_url}
测试报告：\n{last_build_report_url}"""
        return msg



class DingTalk:
    def __init__(self):
        from src.utils.yamlloader import YamlLoader
        self.ding_conf = YamlLoader().load(r"conf/dingtalk.yaml")
        self.__url = self.__get_url(secret = self.ding_conf["robot"]["secret"], \
                                    access_token = self.ding_conf["robot"]["access_token"])

    def __get_url(self, secret, access_token):
        """
            获取请求地址
        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return  f"this is webhook/access_token={access_token}&timestamp={timestamp}&sign={sign}"


    def send_message(self, msg):
        """
            发送文字消息
        """
        if self.ding_conf["active"]:
            logger.info("开始给钉钉群测试报告！")
            try:
                data = {"msgtype": "text", "text": {"content": msg}}
                resp = requests.post(self.__url, json=data)
                if jsonpath(resp.json(), "$.errcode")[0] == 0:
                    logger.success("钉钉消息发送成功！")
                else:
                    logger.success("钉钉消息发送失败！", resp.text)
            except:
                traceback.print_exc()
                logger.warning("钉钉消息发送异常！")
        else:
            logger.warning("未启用钉钉推送，停止发送消息！")


if __name__ == "__main__":
    msg = JenkinReader.get_msg()
    DingTalk().send_message(msg=msg)