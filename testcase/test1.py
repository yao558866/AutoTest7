import requests

r=requests.get("http://www.baidu.com")
print(r)
print(r.status_code)
print(r.content)
print(r.headers)
# print(r.json())
print(r.url)
print(r.encoding)
print(r.raw)
print(r.text)#响应体
# print(r.raise_for_status())