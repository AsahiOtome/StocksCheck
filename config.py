import configparser
import os

"""
conf.ini:
[setting]
url = https://%(host)s/%(id)s.html
host = www.jd.com
id = 10869467

ConfigParser.get() 能够进行%(value)s格式数据的自动填充, 但如果没有对应的key = value对, 将会报错
    print:  https://www.jd.com/10869467.html
RawConfigParser.get() 则不会进行自动的配对, 会把原本的数据内容读入
"""


class GlobalConfig(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError('未能在目录下找到\'{}\'配置文件！请检查！'.format(os.getcwd()))
        self._conf = configparser.ConfigParser()
        self._conf.read(self._path, encoding='utf-8-sig')

    def get(self, section: str, option: str) -> str:
        return self._conf.get(section, option)


global_config = GlobalConfig()
