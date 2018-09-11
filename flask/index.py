from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash, make_response, jsonify
import flask_login
from flask_login import UserMixin, LoginManager, login_required, login_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'
login_manager.login_message = 'please login!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_db'
#该配置为True,则每次请求结束都会自动commit数据库的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = "f_user"
    id = db.Column(db.String, primary_key=True)
    user_name = db.Column("user_name", db.String)
    password = db.Column("password", db.String)
    phone = db.Column(db.String)
    ip = db.Column(db.String)
    login_error_num = db.Column(db.INT)
    create_date = db.Column(db.DATETIME)
    last_login_date = db.Column(db.DATETIME)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    if "username" in session:
        return render_template("index.html", name=flask_login.current_user.user_name)
    else:
        return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(user_name=username).first()
        if user is not None and user.password == password:
            session["username"] = user.user_name
            login_user(user, True)
            return jsonify({"status": "0", "errmsg": "登录成功!"})
        else:
            return jsonify({"status": "-1", "errmsg": "登录失败!"})

    return render_template("login.html")


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9001)