from urllib import request
from bs4 import BeautifulSoup
import pymysql

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'woshiren12',
    'db': 'pytest',
    'charset': 'utf8'
}

connection = pymysql.connect(**db_config)

url = r'http://www.jianshu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')
urls = soup.find_all('a', 'title')

try:
    with connection.cursor() as cursor:
        sql = 'insert into titles(title, url) values(%s, %s)'
        for u in urls:
            cursor.execute(
                sql, (u.string, r'http://www.jianshu.com'+u.attrs['href']))

    connection.commit()
finally:
    connection.close()
