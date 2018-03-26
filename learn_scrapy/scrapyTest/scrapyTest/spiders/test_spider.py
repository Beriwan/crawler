import scrapy
from bs4 import BeautifulSoup


class tsSpride(scrapy.Spider):
    name = 'test'         # 爬虫的唯一名字，在项目中爬虫名字一定不能重复

    # start_requests() 必须返回一个迭代的Request
    def start_requests(self):
        urls = ['http://www.jianshu.com/', ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        titles = soup.find_all('a', 'title')
        for title in titles:
            print(title.string)
