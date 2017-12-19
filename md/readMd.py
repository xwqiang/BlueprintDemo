from flask import Blueprint
from flaskext.markdown import Markdown

md = Blueprint('md', __name__,
               template_folder='templates')




@md.route('/index')
def index():
    return 'md/index.md'
