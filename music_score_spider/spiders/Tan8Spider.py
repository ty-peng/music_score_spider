# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector, Request

from music_score_spider.items import ScoreItem


class Tan8spiderSpider(scrapy.Spider):
    name = 'Tan8Spider'
    allowed_domains = ['tan8.com']
    start_urls = ['http://www.tan8.com/piano-119-0-collects-1-0.html']
    page = 0

    def parse(self, response):
        self.page += 1
        selector = Selector(response)
        score_urls = selector.xpath("//div[@class='p-single-content']//ul/a/@href").extract()
        # 解析详情
        for score_url in score_urls:
            yield Request(score_url, callback=self.parse_detail)
        # 翻页
        if self.page <= 1961:
            per_page = self.page * 20
            detail_url = self.start_urls[0] + '&per_page=%s' % per_page
            yield Request(detail_url, callback=self.parse)

    def parse_detail(self, response):
        score_item = ScoreItem()
        selector = Selector(response)
        score_item['title'] = selector.xpath("//div//h1[@class='title_color']/text()").extract_first()
        score_item['sourceId'] = int(selector.xpath("//div//a[@id='img_heart']/@onclick").extract_first()[13:-1])
        score_item['source'] = 'http://www.tan8.com/yuepu-%s.html' % score_item['sourceId']
        score_item['img'] = selector.xpath("//div[@class='yuepu_img_0421']/img/@src").extract_first()
        score_item['artist'] = selector.xpath("//div[@class='yuepu_name_0421']//span//a//text()").extract_first()
        score_item['desc'] = selector.xpath("//p[@class='brief_0421 content_color']/text()").extract_first()
        # score_item['content'] = selector.xpath("").extract_first()
        score_item['play_url'] = 'http://www.77music.com/flash/%s.swf' % score_item['sourceId']
        score_item['views'] = int(selector.xpath("//div[@class='yuepu_name_0421']//span[2]/text()").extract_first()[:-1])
        score_item['collects'] = int(selector.xpath("//div[@class='yuepu_name_0421']//span[3]/text()").extract_first()[:-1])
        score_item['type'] = 1
        score_item['level'] = int(selector.xpath("//div[@class='yuepu_name_0421']//span[4]/text()").extract_first()[3:-1])
        score_item['uploader'] = selector.xpath("//div[@class='author_img']//h3[@class='title_color']/text()").extract_first()
        score_item['uploadDatetime'] = selector.xpath("//div[@class='author_img']//p[2]/text()").extract_first()
        score_item['updateDatetime'] = selector.xpath("//div[@class='author_img']//p[2]/text()").extract_first()
        # score_item['sounds'] = selector.xpath("").extract_first()
        # score_item['videos'] = selector.xpath("").extract_first()
        yield score_item

