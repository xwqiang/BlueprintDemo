from flask import Blueprint
from flask import render_template
from flask import request

from oa.DingRobot import DingRobot

ding = Blueprint('ding', __name__,
                 template_folder='templates')

groups = [
    {
        "name": "小酷测试",
        "tocken": "33714d7a29f4901cf291ef8bddbfaf1356e7a5ecf18f5577e0b0c55c5645b585"
    },
    {
        "name": "酷云",
        "tocken": "fc6b351c3deffe913465e2be9bb84fa23e582ac1a593ede8fd0976b80eafb719"
    }

]


@ding.route('/', methods=['GET'])
def index():
    return render_template('ding/index.html', groups=groups)


@ding.route('/sendMsg', methods=['POST'])
def sendMsg():
    msg = request.form.get('msg')
    access_token = request.form.get('access_token')
    print(msg, access_token)
    if not msg or not access_token:
        return "请输入消息内容"

    ding = DingRobot('https://oapi.dingtalk.com/robot/send?access_token={access_token}'.format(access_token))

    ding.sendText(msg)

    return "<input type='button' onclick='javascript:history.back()' value='返回' />"
