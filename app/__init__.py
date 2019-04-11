from flask import Flask
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask (__name__, static_folder='../static', template_folder='../templates')
# 添加配置信息
app.config.from_object (Config)
# 建立数据库关系
db = SQLAlchemy (app)
# 绑定APP和数据库
migrate = Migrate (app, db)
# flask-login
login = LoginManager (app)
from app import routes, models
