import pytest
from  src.utils.tagfunc import get_user_token


@pytest.fixture(scope='function')
def get_token():
    """
        单个接口获取token
    """
    yield get_user_token()