# -*- coding: utf-8 -*-
from module.config.crawler import CrawlerConfigReader
from module.request.test import HTTPProxiesTest
from module.request.http import HTTPListRequest


class Do(object):

    @staticmethod
    def test(self):
        '''test
        Request IP test URL to ensure the proxies is enabled.
        '''
        HTTPProxiesTest.test()

    def __init__(self, crawler_name):
        '''Do object
            You may get much info from appointed crawler files.
            It may include request's type, parser's type and
            so on.
        params:
            crawler_name: Crawler's name, which turns to config
            files in ./config folders.
        '''
        # var
        self.crawler_name = crawler_name
        self.req_order    = list()
        self.crawler_conf = dict()
        
        # init
        self.__load__

        self.do()       # debug code

    def do(self):
        '''do
        Start Process from here.
        '''
        self.list_res_iter = self.__req_list__

    @property
    def __load__(self):
        '''__load__
        Load crawler config detail info from config files.
        '''
        self.crawler_conf = CrawlerConfigReader.crawler_config(self.crawler_name)
        # Here is a log about read crawler config info succeed.

    @property
    def __req_list__(self):
        '''__req_list__
        Start a request to get list info from list websites/APIs.
        '''
        # You are supposed to create a child process to do this.
        # Crawler config info.

        req = HTTPListRequest(self.crawler_conf["list_crawler"])
        yield from req.list_res_iter

    @property
    def __parser_list__(self):
        pass