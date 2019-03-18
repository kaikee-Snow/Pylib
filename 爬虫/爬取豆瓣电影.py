# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
url = 'https://movie.douban.com/subject/26942674/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'lxml')
element = soup.select('#content h1 span')
print(element[0].getText())
