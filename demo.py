from urllib import request
from bs4 import BeautifulSoup

url = r'http://www.jianshu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')

soup = BeautifulSoup(page_info, 'html.parser')

# print(soup.prettify())
titles = soup.find_all('a', 'title')

#将爬到的文章写入txt
with open(r'D:\work\pachong\content\titles.txt', 'w') as file:
    for title in titles:
        file.write(title.string + '\n')
