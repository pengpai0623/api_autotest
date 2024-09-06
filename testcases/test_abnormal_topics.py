import allure
import pytest
import requests
from common import business


class Test_abnormal_topics:
    # id = None

    @allure.feature('cnode接口异常情况测试')
    @allure.story('获取主题首页接口tab参数异常测试')
    @allure.testcase('www.测试用例存放地址.com')
    @allure.issue('www.bug单地址.com')
    @allure.severity('blocker')
    @pytest.mark.parametrize('tab', ['ask1', 'share1'])
    def test_get_abnormal_tab_topics(self, tab):
        """
        用例描述位置：
        1，tab为非指定类型的响应情况
        2，并进行响应内容验证
        """
        url = business.montage_url('topics')
        param = {
            'page': 1,
            'tab': tab,
            'limit': 1,
            'mdrender': "False"
        }
        r = requests.get(url, params=param)
        res = r.json()
        assert r.status_code == 200
        assert 'success' in res, '断言响应存在success字段'
        assert res['success'], '断言响应中success字段值为True'
        assert res['data'] == []

    @allure.feature('cnode接口异常情况测试')
    @allure.story('获取主题首页接口page参数异常测试')
    @allure.testcase('www.测试用例存放地址.com')
    @allure.issue('www.bug单地址.com')
    @allure.severity('blocker')
    @pytest.mark.parametrize('page', ['ask'])
    def test_get_abnormal_page_topics(self, page):
        """
        用例描述位置：
        1，page类型为str异常情况验证
        # 发现一个bug，当page为str类型时，也能访问数据
        2，并进行响应内容验证
        """
        url = business.montage_url('topics')
        param = {
            'page': page,
            'tab': 'ask',
            'limit': 1,
            'mdrender': "False"
        }
        r = requests.get(url, params=param)
        res = r.json()
        assert r.status_code == 200
        assert 'success' in res, '断言响应存在success字段'
        assert res['success'], '断言响应中success字段值为True'


if __name__ == '__main__':
    # pragma:no cover
    pytest.main(['-sv', 'testcases\test_get_topics.py::test_get_topics'])
