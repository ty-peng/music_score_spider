# -*- coding: utf-8 -*-
import pymongo
from music_score_spider.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MusicScoreSpiderPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        table_name = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[table_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
