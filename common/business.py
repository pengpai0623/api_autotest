def montage_url(*args):
    """
    根据不同接口，生成对应的url
    :param args:
    :return: url
    """
    base_url = 'https://cnodejs.org/api/v1'
    for i in args:
        base_url = '/'.join([base_url, i])
    return base_url


def get_token():
    """
    获取token
    :return: token
    """
    return 'cad20bd8-76f1-43f4-a34c-2286d77a4f04'


