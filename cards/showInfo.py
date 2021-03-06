import base64

from flask import Blueprint, make_response
from flask import current_app
from flask import request

from config import dev
from manage import User

cards = Blueprint('cards', __name__,
                  template_folder='templates')


@cards.route('/')

def index():
    print(User.query.all())
    print(current_app.config.get("SECRET_KEY"))
    print(current_app.config.get('SETTINGS').PASSWORD)
    print(dev.PASSWORD)
    print(current_app.config.get('USERNAME'))
    return '''
    <form action="/cards/index">
    <input type="text" value="a"/>
        <input type="submit" value="get"/>
    </form>

    <form action="/cards/index" method="post">
    <input type="text" value="a"/>
        <input type="submit" value="post"/>
    </form>
    '''


@cards.route('/index', methods=['POST', 'GET'])
def show():
    # return "cards"
    # return render_template('cards/ok.html')
    respe = make_response()  # 创建响应实例
    # respe.response = render_template('oa/index.html')  #
    respe.headers['Content-type'] = 'text/plain'  # 文档的类型，这里写成了文本类型
    respe.headers['Set-Cookie'] = 'JSESSIONID=from_flask'  # 文档的类型，这里写成了文本类型
    respe.status = '302'
    respe.headers['Location'] = 'https://super.pre.in.kuyun.com'
    return respe


@cards.route('/auth')
# @authentication_required
def auth():
    if checkHeaderAuth():
        return 'logined in'
    else:
        resp = make_response()
        resp.headers['WWW-authenticate'] = 'Basic Realm="test"'
        resp.status = '401'
        return resp;


def checkHeaderAuth():
    authorization = request.headers.get('Authorization')
    if not authorization:
        return False
    user_pwd = authorization[6:]
    inputbytes = base64.decodebytes(bytes(user_pwd, encoding='utf8'))
    if str(inputbytes, encoding='utf-8') == 'a:b':
        return True;
    return False
