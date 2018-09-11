#!/usr/bin/python3.5
# -*- coding utf-8
from flask_login import UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_db'
#该配置为True,则每次请求结束都会自动commit数据库的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = "f_user"
    id = db.Column(db.String, primary_key=True)
    user_name = db.Column("user_name", db.String)
    password = db.Column("password", db.String)
    phone = db.Column(db.String)
    ip = db.Column(db.String)
    login_error_num = db.Column(db.Integer)
    create_date = db.Column(db.DATETIME)
    last_login_date = db.Column(db.DateTime)
