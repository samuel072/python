from flask import Flask, render_template, session, url_for
from config import DevConfig
from login import user_blueprint
from db import db

app = Flask(__name__)
db.init_app(app)


# 加载配置文件
app.config.from_object(DevConfig)
app.register_blueprint(blueprint=user_blueprint, url_prefix="/user")


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index_index():
    if "username" in session:
        return render_template("index.html", name="username")
    else:
        return render_template("login.html")


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True, port=9001)
