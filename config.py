# 配置文件
import os

BASE_DIR = os.path.abspath (os.path.dirname (__file__))


class Config (object):
	# 设置安全秘钥
	SECRET_KEY = 'YGj7^0vyA^!OBdAOwqqF'
	# 配置数据库连接
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flask_blog?charset=utf8'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
