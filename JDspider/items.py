# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    ID = scrapy.Field()  # 商品ID
    name = scrapy.Field()  # 商品名字
    comment = scrapy.Field()  # 评论人数
    shop_name = scrapy.Field()  # 店家名字
    price = scrapy.Field()  # 价钱
    link = scrapy.Field()
    # commentVersion = scrapy.Field()
    comment_num = scrapy.Field()
    score1count = scrapy.Field()  # 评分为1星的人数
    score2count = scrapy.Field()  # 评分为2星的人数
    score3count = scrapy.Field()  # 评分为3星的人数
    score4count = scrapy.Field()  # 评分为4星的人数
    score5count = scrapy.Field()
