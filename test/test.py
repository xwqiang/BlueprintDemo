from flask import Blueprint
from flask import current_app
from flask import make_response
from flask import redirect
from flask import request

test = Blueprint('test', __name__,
                 template_folder='templates')

@test.route('/')
def testtocken():
    tocken = request.args.get('tocken')
    ref = request.headers.get('Referer')
    print(tocken)
    return redirect(ref,302,Response=None)

@test.route('/test')
def ttt():
    print(request.headers)
    resp = make_response()
    return resp

