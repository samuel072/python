#!/usr/bin/python3.5
# -*- coding utf-8
from flask import request, Blueprint, render_template, jsonify, session
from User import User


user_blueprint = Blueprint(name="user", import_name=__name__)


@user_blueprint.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        session['username'] = username
        user = User.query.filter_by(user_name=username).first()
        if user is not None:
            return jsonify({"status": "0", "errmsg": "登录成功!"})
        else:
            return jsonify({"status": "-1", "errmsg": "登录失败, 用户不存在!"})
    else:
        return render_template("login.html")
