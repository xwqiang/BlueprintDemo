import requests
import webbrowser
import os
def getHeader(JSESSIONID):
    HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Cookie': 'JSESSIONID='+JSESSIONID,
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }

login_url = 'http://172.21.62.101:7777/uia/login'

# editthiscookie插件可以修改浏览器的cookie

def openWeb():
    session = requests.session()

    resp = session.post(login_url, {'username': 'xuwuqiang', 'password': 'kuyun123' })
    JSESSIONID = session.cookies.get('JSESSIONID')
    os.system("echo '{JSESSIONID}' > ~/.uia.session".format(JSESSIONID=JSESSIONID))
    print(str(resp.content,encoding='utf-8'))
    print('get from cookie',JSESSIONID)
    open_url = 'http://172.21.62.101:7777/uia/index.jsp'.format(
        JSESSIONID=JSESSIONID)

    os.system("cd /Users/xuwuqiang/PycharmProjects/BlueprintDemo/test;mitmproxy -s proxytest.py -p 19999")

    webbrowser.open(open_url)


if __name__ == '__main__':
    os.system('tell application "Finder" ')
    os.system('set dialog to display dialog "切换代理. 请选择:" buttons {"Home", "Office", "Cancel"} default button "Home" with title "切换代理" ')
    # openWeb()
