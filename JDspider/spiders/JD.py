# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from JDspider.items import JDSpiderItem
import scrapy
import re
import json


class JDSpider(Spider):
    name = "JDSpider"
    # start_urls = ['https://list.jd.com/list.html?cat=1320,5019,12215']
    start_urls = []
    for i in range(1, 10+1):  # 这里需要自己设置页数
        url = 'https://list.jd.com/list.html?cat=1320,5019,12215&page='+ str(i)+'&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        start_urls.append(url)

    def parse_price(self, response):
        item1 = response.meta['item']
        temp1 = str(response.body).split('jQuery712392([')
        s = temp1[1][:-6]  # 获取到需要的json内容
        js = json.loads(str(s))  # js是一个list
        item1['price'] = js['p']
        return item1

    def parse_getCommentnum(self, response):
        item1 = response.meta['item']
        js = json.loads(str(response.body)[2:-1])
        item1['score1count'] = js['CommentsCount'][0]['Score1Count']
        item1['score2count'] = js['CommentsCount'][0]['Score2Count']
        item1['score3count'] = js['CommentsCount'][0]['Score3Count']
        item1['score4count'] = js['CommentsCount'][0]['Score4Count']
        item1['score5count'] = js['CommentsCount'][0]['Score5Count']
        item1['comment_num'] = js['CommentsCount'][0]['CommentCount']
        num = item1['ID']  # 获得商品ID
        s1 = re.findall("\d+",str(num))[0]
        url = "http://p.3.cn/prices/mgets?callback=jQuery712392&type=1&area=1_2800_2849_0.138365810&pdtk=&pduid=15083882680322055841740&pdpin=jd_4fbc182f7d0c0&pin=jd_4fbc182f7d0c0&pdbp=0&skuIds=J_" + s1
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)

    def parse_detail(self, response):
        # pass
        item1 = response.meta['item']
        sel = Selector(response)  # Xpath选择器

        if response.url[:18] == 'https://item.jd.hk':    #判断是否为全球购
            goods = sel.xpath('//div[@class="shopName"]')
            temp = str(goods.xpath('./strong/span/a/text()').extract())[2:-2]
            if temp == '':
                item1['shop_name'] = '全球购：'+ 'JD全球购'  #判断是否JD自营
            else:
                item1['shop_name'] = '全球购：' + temp
            # print('全球购：'+ item1['shop_name'])

        else:
            goods = sel.xpath('//div[@class="J-hove-wrap EDropdown fr"]')
            item1['shop_name'] = str(goods.xpath('./div/div[@class="name"]/a/text()').extract())[2:-2]
            if item1['shop_name'] == '':       #是否JD自营
                item1['shop_name'] = '京东自营'
            # print(item1['shop_name'])

        url = "http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=" + item1['ID'][0]
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_getCommentnum)

    def parse(self, response):  # 解析搜索页
        # print(response.text)
        sel = Selector(response)  # Xpath选择器
        goods = sel.xpath('//li[@class="gl-item"]')
        for good in goods:
            item1 = JDSpiderItem()

            temp1 = str(good.xpath('./div/div[@class="p-name"]/a/em/text()').extract())
            pattern = re.compile("[\u4e00-\u9fa5]+.+\w")   #从第一个汉字起 匹配商品名称
            good_name = re.search(pattern,temp1)

            item1['name'] = good_name.group()
            item1['link'] = "http:" + str(good.xpath('./div/div[@class="p-img"]/a/@href').extract())[2:-2]
            item1['ID'] = good.xpath('./div/@data-sku').extract()

            if good.xpath('./div/div[@class="p-name"]/a/em/span/text()').extract() == ['全球购']:
                item1['link'] = 'https://item.jd.hk/' + item1['ID'][0] +'.html'
            url = item1['link'] + "#comments-list"

            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)
