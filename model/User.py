# 导入:
from sqlalchemy import Column, String, Integer

from init import db


class User(db.Model):
    # 表的名字:
    __tablename__ = 'oa_system_user'

    # 表的结构:
    id = Column(Integer(20), primary_key=True)
    name = Column(String(20))


