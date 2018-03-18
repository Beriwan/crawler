# -*- coding: utf-8 -*-
import scrapy
from firstDemo.items import FirstdemoItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item = FirstdemoItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        yield item
