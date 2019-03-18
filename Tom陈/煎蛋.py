from bs4 import BeautifulSoup
import requests
import time
import os
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    try:
        r = requests.get(url, headers=headers)
    except:
        r = 
#comment-3906546 > div > div > div.text > p > img
http://jandan.net/ooxx/page-1