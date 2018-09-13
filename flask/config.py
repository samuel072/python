#!/usr/bin/python3.5
# -*- coding utf-8
import os


class Config():
    pass


class ProductConfig():
    pass


class DevConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_ECHO = True
