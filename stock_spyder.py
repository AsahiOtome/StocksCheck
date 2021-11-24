from logger import logger
from util import parse_json, wait_some_time, get_random_users
from config import global_config
from util import SpiderSession


class StockSpyder(object):
    def __init__(self):
        self._spider_session = SpiderSession()
        self._spider_session.load_cookies_from_local()

        self.session = self._spider_session.get_session()

    def visit_homepage(self):
        url = 'http://quote.eastmoney.com/newstatic/js/libs/quotemoneyflowchart0715.js'
        headers = {
            'Host': 'quote.eastmoney.com',
            'Referer': 'http://quote.eastmoney.com/sh601208.html',
            'User-Agent': get_random_users()
        }
        resp = self.session.get(url=url, headers=headers)
        return resp


