# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : woodenrobot
from scrapy import cmdline
name = 'JDSpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

#用于在IDE里进行Debug
