from bs4 import BeautifulSoup
import requests
url = 'http://jandan.net/ooxx/page-1'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
# print(soup.select('div.p12'))
# print(soup.select('tr.item'))
print(soup.select('div.text > p > img')[0]['src'])
# content > div > div.article > div > table:nth-child(18) > tbody > tr
