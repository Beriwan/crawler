# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'woshiren12',
    'db': 'info2',
    'charset': 'utf8'
}


class LgspiderPipeline(object):
    # 获取数据库连接和游标
    def __init__(self):
        self.connection = connection = pymysql.connect(**db_config)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = 'insert into info01(title, salary, position, time, grade, company) values(%s, %s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (item['title'].encode('utf-8'),
                                      item['salary'],
                                      item['position'].encode('utf-8'),
                                      item['time'].encode('utf-8'),
                                      item['grade'].encode('utf-8'),
                                      item['company'].encode('utf-8'),
                                      )
                                )
            self.connection.commit()
        except pymysql.Error as e:
            print(e.args)
        return item
