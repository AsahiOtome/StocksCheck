import json
import random
import time
import requests
from config import global_config
import os
import pickle


def parse_json(string: str) -> dict:
    """
    将获取到的字符串转译为json串
    :param string: 获取到的jsonQuery字符串
    :return:
    """
    begin = string.find('{')
    end = string.find('}') + 1
    return json.loads(string[begin:end])


"""
json.loads()对字符串的读取必须严格按照单引号'包裹双引号"的形式。eg. '{"name": "Demo"}'
"""


def get_random_users() -> str:
    """
    生成随机的用户代理
    :return:
    """
    user_agents = list(json.loads(global_config.get('connect_config', 'user_agents').replace('\n', '')).values())
    return random.choice(user_agents)


def wait_some_time():
    time.sleep(random.randint(100, 300) / 100)


"""
session.headers 将会添加一个预先的header字典，在get时自动应用。在get(headers=headers)时会将两个headers整合到一起，
如果存在重复的key则会用后者的value覆盖前者。
pickle.dump() 函数能一个接着一个地将几个对象转储到同一个文件。随后调用 pickle.load() 来以同样的顺序检索这些对象
"""


class SpiderSession(object):
    """
    用于对session进行初始化，并提供cookies的存储与调用功能
    """
    def __init__(self):
        self._cookies_path = './cookies/' + global_config.get('settings', 'project_name') + '.cookies'
        self._accept = global_config.get('connect_config', 'accept')
        self._connection = global_config.get('connect_config', 'connection')
        self._user_agent = get_random_users()

        self.session = self._init_session()

    def _init_session(self):
        session = requests.session()
        session.headers = self.get_headers()
        return session

    def get_headers(self):
        headers = {
            'Accept': self._accept,
            'User - Agent': self._user_agent,
            'Connection': self._connection
        }
        return headers

    def get_user_agent(self):
        return self._user_agent

    def get_session(self):
        """
        获取当前session信息
        :return:
        """
        return self.session

    def get_cookies(self):
        """
        获取当前cookies
        :return:
        """
        return self.get_session().cookies

    def save_cookies_to_local(self):
        """
        将当前cookies保存至本地文件
        :return:
        """
        directory = os.path.dirname(self._cookies_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(self._cookies_path, 'wb') as fp:
            pickle.dump(self.get_cookies(), fp)

    def load_cookies_from_local(self):
        """
        从本地文件读取上一次的cookies
        :return:
        """
        if not os.path.exists(self._cookies_path):
            return False
        with open(self._cookies_path, 'rb') as fp:
            cookies = pickle.load(fp)
        self.get_session().cookies.update(cookies)


