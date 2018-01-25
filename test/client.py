import requests

resp = requests.get("http://uia.in.kuyun.com/uia/",proxies={'http':'127.0.0.1:19999'})
print(resp.content)