import requests
from pyquery import PyQuery as pq
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
print(doc('.explore-tab .feed-item'))
