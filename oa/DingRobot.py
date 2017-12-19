import requests


class DingRobot():
    def __init__(self, url):
        self.url = url;

    def sendText(self, message, atMobiles=None, isAtAll=False):
        data = {
            "msgtype": "text",
            "text": {
                "content": message
            },
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": isAtAll
            }
        }
        requests.post(self.url, json=data)
