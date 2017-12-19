import pymysql
from flask import Blueprint
from flask import render_template
from flask import request

from decorators.session_required import session_required

oa = Blueprint('oa_api', __name__,
               template_folder='templates')


@oa.route('/')
@session_required
def sendOk():
    return render_template('oa/index.html')


@oa.route('/changePwd', methods=['POST'])
def newPage():
    password = request.form.get('password')
    username = request.form.get('username')
    if not password or not password:
        return "请输入新密码/用户名"

    try:
        conn = pymysql.connect(host='192.168.200.22', user='kuyun_oa', passwd='MSbiJU52w3e', db='kuyun_oa', port=3306,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        with conn.cursor() as cur:  # 获取一个游标
            sql = "update oa_system_user set password = '{password}' where deleted =  0 and name = '{username}'".format(
                password=password, username=username)
            cur.execute(sql)
        conn.commit()
    except Exception as e:
        return "设置失败"
    finally:
        conn.close()
    return "ok,设置成功"
