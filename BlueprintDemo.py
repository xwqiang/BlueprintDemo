from flask import Flask

from oa.alterPwd import oa
from cards.showInfo import cards

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(oa, url_prefix='/oa')
    app.register_blueprint(cards, url_prefix='/cards')
    app.run(debug=True)
