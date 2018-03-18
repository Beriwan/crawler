import scrapy
from bs4 import BeautifulSoup


class lg_spider(scrapy.Spider):
    name = 'lg'

    def start_requests(self):
        urls = ['https://www.lagou.com/zhaopin/Python/1/?filterOption=1',
                'https://www.lagou.com/zhaopin/Python/2/?filterOption=2',
                'https://www.lagou.com/zhaopin/Python/3/?filterOption=3',
                'https://www.lagou.com/zhaopin/Python/4/?filterOption=4',
                'https://www.lagou.com/zhaopin/Python/5/?filterOption=5',
                ]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for info in soup.find_all('li', 'con_list_item default_list'):
            salary = info.attrs['data-salary'].split('k')[0]
            salary = int(salary) * 1000

            yield {
                'title': info.attrs['data-positionname'],  # 职位
                'position': info.find('em').get_text().split('·')[0],  # 工作地点
                'salary': salary,  # 最低工资
                'time': (info.find('span', 'format-time')).string,  # 发布时间
                # 学历要求
                'grade': info.find('div', 'li_b_l').get_text().split('/')[-1],
                'company': info.attrs['data-company'],  # 公司名称
            }

		
