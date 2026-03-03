import os
import sys

from src.utils.mail import Mail

sys.path.append(os.getcwd())
from datetime import datetime
sys.path.append(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

import pytest
import time
from src.utils.tagfunc import get_user_token
from src.utils.mysql import MysqlClient
from src.utils.report import Report
from src.utils.dingtalk import DingTalk
from src.utils.result import record_result



@pytest.fixture(scope='function')
def get_token():
    """
        单个接口获取token
    """
    yield get_user_token()


@pytest.fixture
def create_task():
    """
        创建自定义的任务
    """
    sql = f"""
            INSERT INTO tb_tasks
                VALUES
                    (
                        NULL,
                        '{int(time.time())}', 
                        '测试任务{int(time.time())}', 
                        '测试任务{int(time.time())}',
                        '42',
                        '["dl1EffqrqpiJsqN.jpg"]',
                        '2024-07-19 17:12:00',
                        '-8.99',
                        '100',
                        '0',
                        '100.0',
                        '999',
                        '10923',
                        '0',
                        '2023-07-20 16:44:07',
                        '2023-07-20 16:44:07'
                    );

            """
    assert MysqlClient().commit(sql)
    sql = "select max(id) as id from tb_tasks where xxx"
    res = MysqlClient().query(sql)
    yield res[0][0]


def pytest_config(config):
    """
        产生全局变量的配置函数
    """
    item = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    sys.path.append(item)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
        获取所有的测试用例结果
    """
    passed, failed, skipped = Report().get_report_summary(terminalreporter)
    subject = f"自动化测试报告{sys.path[-1]}"
    content = f"测试结果如下:\n测试通过用例：\n    {len(passed)}个用例通过\n"
    content = content + f"\n测试跳过用例：\n    {len(skipped)}个用例跳过\n"
    content = content + f"\n测试失败用例：\n    {len(failed)}个用例执行失败\n"
    record_result(passed, failed, skipped)
    Mail().send_mail(subject, content)
    DingTalk().send_message(msg= content)

