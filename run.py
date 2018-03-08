from flask import Flask
from flask import render_template

from SettingManager import SettingManager
from config import setting
from core.session_timeout import core
from oa.ding import ding
from oa.changePwd import oa
from cards.showInfo import cards
from test.test import test
from flask_cors import CORS


app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,dd?'

app.register_blueprint(oa, url_prefix='/oa')
app.register_blueprint(cards, url_prefix='/cards')
app.register_blueprint(ding, url_prefix='/ding')
app.register_blueprint(core, url_prefix='/core')
app.register_blueprint(test, url_prefix='/test')

CORS(app)






@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    print(setting.getvalue("HOST"))


    app.run(host="0.0.0.0", debug=True)
