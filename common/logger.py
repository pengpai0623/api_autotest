import logging
from common import utils

logger = logging.getLogger(name='api_Test')
logger.setLevel(logging.DEBUG)
# 依次对应时间 级别 函数名
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')
# 打开一个文件用于追加
fl = logging.FileHandler(filename=utils.get_path()[2], mode='a', encoding='utf8')
fl.setFormatter(formatter)
# 在命令行运行时输出
sl = logging.StreamHandler()
sl.setFormatter(formatter)

logger.addHandler(fl)
logger.addHandler(sl)

fl.close()
