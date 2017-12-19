from functools import wraps

from flask import flash, redirect, url_for
from flask import session


def session_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        print('wrapper')
        if not session.get('name'):
            flash("session timeout!")
            print('timeout.')
            return redirect(url_for('core.check_auth'))
        return func(*args, **kwargs)

    return decorated_function