# -*- coding: utf-8 -*-
import scrapy


class Tan8spiderSpider(scrapy.Spider):
    name = 'Tan8Spider'
    allowed_domains = ['tan8.com']
    start_urls = ['http://tan8.com/']

    def parse(self, response):
        pass
