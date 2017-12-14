from flask import Blueprint

oa = Blueprint('oa_api', __name__,
                        template_folder='templates')


@oa.route('/index')
def show():
    return "alterpwd"
