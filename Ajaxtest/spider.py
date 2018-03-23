import json
import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/64.0.3282.186 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('title')[0].get_text()
    print(title)


def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        print(url)
        html = get_page_detail(url)
        if html:
            #print(html)
            parse_page_detail(html)


if __name__ == '__main__':
    main()
