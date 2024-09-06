import allure
import pytest
import requests
from common import business, utils
from common.logger import logger


class Test_topics:
    id = None

    @allure.feature('cnode接口测试')
    @allure.story('获取主题首页接口测试')
    @allure.testcase('www.测试用例存放地址.com')
    @allure.issue('www.bug单地址.com')
    @allure.severity('blocker')
    #  从json文件读取数据
    # @pytest.mark.parametrize('topic_basic_info', utils.get_json_data('test_get_topics'))
    # 从excel格式读取数据
    @pytest.mark.parametrize('topic_basic_info', utils.get_csv_data())
    def test_get_topics(self, topic_basic_info):
        """
        用例描述位置：
        1，获取page == 1、tab == ask/share/job、limit == 1、mdrender == false的信息
        2，并进行响应内容验证
        """
        url = business.montage_url('topics')
        r = requests.get(url, params=topic_basic_info)
        res = r.json()
        logger.critical(f'断言topic_basic_info类型为字典:{isinstance(topic_basic_info, dict)}')
        assert isinstance(topic_basic_info, dict)
        for i in res['data']:
            logger.critical(f'断言tab类型是否符合预期:{i["tab"] == topic_basic_info["tab"]}')
            assert i['tab'] == topic_basic_info['tab']
        logger.critical(f'断言状态码为200:{r.status_code == 200}')
        assert r.status_code == 200
        logger.critical(f'断言响应存在success字段:{"success" in res}')
        assert 'success' in res, '断言响应存在success字段'
        logger.critical(f'断言响应中success字段值为True:{res["success"] == True}')
        assert res['success'], '断言响应中success字段值为True'

    @allure.feature('cnode接口测试')
    @pytest.mark.xfail('True', '新增话题接口暂未实现')
    @allure.story('新增话题接口测试')
    @pytest.mark.parametrize('url', [business.montage_url('topics')])
    # add这个接口就不太适合使用json来存储data了，因为accesstoken需要手动获取
    # 或者可以把accesstoken直接更新在json，但这样失去了自动化的意义
    # 这个案例只是特殊情况，正常来说，token不会当做params或者data里的一个参数的
    # 所以新增仍可以通过json来存储数据
    # 最重要的是灵活使用
    # 至于token 我们可以使用headers去传递
    def test_add_topic(self, url):
        data = {
            "accesstoken": business.get_token(),
            "title": "简单验证一下",
            "tab": "dev",
            "content": "验证"
        }
        r = requests.post(url=url, data=data)
        res = r.json()
        assert 'success' in res, '断言响应存在success字段'
        assert 'topic_id' in res, '断言响应存在success字段'
        assert res['success'], '断言响应中success字段值为True'

    @allure.feature('cnode接口测试')
    @allure.story('查询话题接口测试')
    def test_get_topic(self):
        topic_id = '66a1e980fc5c3b4f1cee9d1b'
        url = business.montage_url('topic', topic_id)
        r = requests.get(url)
        res = r.json()
        assert r.status_code == 200
        assert 'success' in res, '断言响应存在success字段'
        assert res['success'] is True, '断言响应中success字段值为True'

    @allure.feature('cnode接口测试')
    @pytest.mark.xfail('True', '更新话题接口暂未实现')
    @allure.story('更新话题接口测试')
    def test_update_topic(self):
        url = business.montage_url('topics/update')
        update_data = {
            "accesstoken": business.get_token(),
            "topic_id": '66a1e980fc5c3b4f1cee9d1b',
            "title": "new简单验证一下",
            "tab": "dev",
            "content": "new验证"
        }
        r = requests.post(url=url, data=update_data)
        assert r.status_code == 200
        res = r.json()
        print(res)
        # 注意，当断言content时，应使用assert xxx in xxx的形式，具体打印出来看一下
        assert 'success' in res
        assert res['success']
        assert res['topic_id'] == update_data['topic_id']
