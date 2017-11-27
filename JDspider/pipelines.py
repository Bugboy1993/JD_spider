# -*- coding: utf-8 -*-
from Sql import Sql
from JDspider.items import JDSpiderItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdspiderPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, JDSpiderItem):
            good_id = item['ID']
            good_name = item['name']
            shop_name = item['shop_name']
            price = item['price']
            link = item['link']
            comment_num = item['comment_num']
            score1count = item['score1count']
            score2count = item['score2count']
            score3count = item['score3count']
            score4count = item['score4count']
            score5count = item['score5count']
            Sql.insert_JD_name(good_id, good_name, shop_name, price, link,
                               comment_num ,score1count, score2count, score3count, score4count, score5count)
            # print('存储一条信息完毕了哦')
        return item
