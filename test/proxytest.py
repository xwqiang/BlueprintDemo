import os

from mitmproxy.net.http import Headers
from mitmproxy.test.tutils import tresp

# https://www.wenjuan.in/s/iA7jieu/

def request(flow):
    hostname = flow.request.pretty_host
    uri = flow.request.pretty_url
    # if 'www.wenjuan.in' in hostname and '/iA7jieu/' in uri:
    if 'www.wenjuan.in' in hostname and '/Bj2Efe/' in uri:

        del flow.request.headers['Cookie']
        # flow.response.content = bytes('hello world',encoding='utf8')
    # flow.response.headers["BOOM"] = "boom!boom!boom!"
    # flow.response.headers['Set-Cookie'] = 'JSESSIONID={JSESSIONID}'.format(JSESSIONID=s)
    # flow.response.content = bytes('hello world',encoding='utf8')

# def response(flow):
#     pass
