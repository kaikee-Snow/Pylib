import requests
response = requests.get('http://www.baidu.com')
print(response.text)
print(response.cookies)
print(response.status_code)
print(response.content)
response.headers
response.url
response.history
response.raise_for_status()
response.json()
