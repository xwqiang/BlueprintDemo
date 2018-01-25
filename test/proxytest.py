import os
def response(flow):
    # flow.response.headers["BOOM"] = "boom!boom!boom!"
    # flow.response.headers['Set-Cookie'] = 'JSESSIONID={JSESSIONID}'.format(JSESSIONID=s)
    flow.response.content = bytes('hello world',encoding='utf8')

