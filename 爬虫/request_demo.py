import requests
r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
