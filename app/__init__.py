from flask import Flask
from config import Config

app = Flask (__name__, static_folder='../static', template_folder='../templates')

# 添加配置信息
app.config.from_object (Config)
from app import routes
