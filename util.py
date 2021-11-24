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


def get_random_users() -> str:
    """
    生成随机的用户代理
    :return:
    """
    return random.choice(json.loads(global_config.get('connect_config', 'user_agents')))


def wait_some_time():
    time.sleep(random.randint(100, 300) / 100)


"""
session.headers 将会添加一个预先的header字典，在get时自动应用。在get(headers=headers)时会将两个headers整合到一起，
如果存在重复的key则会用后者的value覆盖前者。
"""


class SpiderSession(object):
    """
    用于对session进行初始化，并提供cookies的存储与调用功能
    """
    def __init__(self):
        self._cookies_name = './cookies/'
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
        return self.session

    def save_cookies_to_local(self):
        if not os.path.exists(self._cookies_save_path):
            os.makedirs(self._cookies_save_path)


