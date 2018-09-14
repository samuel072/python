from flask import Flask, render_template, session
from config import DevConfig
from com.kaiji.flask.controller.ApiController import api
from com.kaiji.flask.controller.login import user_blueprint
from com.kaiji.flask.model.db import db

app = Flask(__name__)
db.init_app(app)


# 加载配置文件
app.config.from_object(DevConfig)
app.register_blueprint(blueprint=user_blueprint, url_prefix="/user")
app.register_blueprint(blueprint=api, url_prefix="/api")


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
