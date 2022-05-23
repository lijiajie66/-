from flask import Flask
from config import Config

from resources.user import user_bp

from util.middlewares import jwt_authentication
app = Flask(__name__)
app.register_blueprint(user_bp)  # 注册蓝图

app.config.from_object(Config)  # 添加配置文件

app.before_request(jwt_authentication)  # 添加请求钩子  在每次请求接口时  都会先走到这里



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
