import time
from urllib import request
from bs4 import BeautifulSoup
import re

url = r'https://www.zhihu.com/question/22918070'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')

links = soup.find_all(
    'img', "origin_image zh-lightbox-thumb", src=re.compile(r'.jpg$'))

local_path = r'D:\work\pachong\content\pic'

for link in links:
    print(link.attrs['src'])
    request.urlretrieve(link.attrs['src'],
                        local_path + r'\%s.jpg' % time.time())
