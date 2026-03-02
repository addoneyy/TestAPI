import os
import sys
sys.path.append(os.getcwd())

import pytest
import time
from src.utils.tagfunc import get_user_token
from src.utils.mysql import MysqlClient


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