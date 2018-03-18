# -*- coding: utf-8 -*-
import scrapy


class Pic169bbSpider(scrapy.Spider):
    name = 'pic_169bb'
    allowed_domains = ['169bb.com']
    start_urls = ['http://169bb.com/']

    def parse(self, response):
        pass
