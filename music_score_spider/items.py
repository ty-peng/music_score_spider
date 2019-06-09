# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScoreItem(scrapy.Item):
    title = scrapy.Field()
    # 源网页链接
    source = scrapy.Field()
    # 源id
    sourceId = scrapy.Field()
    # 封面头图
    img = scrapy.Field()
    artist = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()
    play_url = scrapy.Field()
    views = scrapy.Field()
    collects = scrapy.Field()
    # 乐器类别
    type = scrapy.Field()
    # 难度
    level = scrapy.Field()
    uploader = scrapy.Field()
    uploadDatetime = scrapy.Field()
    updateDatetime = scrapy.Field()
    sounds = scrapy.Field()
    videos = scrapy.Field()
