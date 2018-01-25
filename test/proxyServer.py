import requests
requests.get('http://httpbin.org/ip', proxies={'http': '121.193.143.249:80'}).json()
