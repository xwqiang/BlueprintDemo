from flask import Blueprint
from flask import render_template

core = Blueprint('core', __name__,
               template_folder='templates')

@core.route('/timeout')
def timeout():
    return render_template('core/timeout.html')

@core.route('/check_auth')
def check_auth():
    return render_template('core/noauth.html')
