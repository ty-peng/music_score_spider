# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicScoreSpiderItem(scrapy.Item):
    title = scrapy.Field()
    source = scrapy.Field()
    sourceId = scrapy.Field()
    img = scrapy.Field()
    artist = scrapy.Field()
    desc = scrapy.Field()
    views = scrapy.Field()
    collects = scrapy.Field()
    type = scrapy.Field()
    level = scrapy.Field()
    uploader = scrapy.Field()
    uploadDatetime = scrapy.Field()
    sounds = scrapy.Field()
    videos = scrapy.Field()
    pass
