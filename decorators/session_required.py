from functools import wraps

import functools
from flask import flash, redirect, url_for, app, jsonify
from flask import request
from flask import session
from flask import current_app as app


def session_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get('name'):
            flash("session timeout!")
            return redirect(url_for('core.check_auth'))
        return func(*args, **kwargs)

    return decorated_function


def requires_authorization(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


def ok_user_and_password(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']


def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'
    return resp
