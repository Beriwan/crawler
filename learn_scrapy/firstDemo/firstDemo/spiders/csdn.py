# -*- coding: utf-8 -*-
import scrapy
from firstDemo.items import FirstdemoItem 


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        item = FirstdemoItem()
        item['title'] = response.xpath("//h2[@class='csdn-tracking-statistics']/a/text()").extract()
        item['detail'] = response.xpath("//dd[@class='tag']/a/text()").extract()
        item['link'] = response.xpath("//h2[@class='csdn-tracking-statistics']/a/@href").extract()
        yield item
