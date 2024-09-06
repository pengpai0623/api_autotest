import pytest


@pytest.fixture(scope='module')
def fixture1():
    base_url = 'https://cnodejs.org/api/v1/'
    return base_url
