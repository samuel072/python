#!/usr/bin/python3.5
# -*- coding utf-8
from flask_login import UserMixin
from db import db


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
