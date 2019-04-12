from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import User


class LoginForm (FlaskForm):
	# DataRequired，当你在当前表格没有输入而直接到下一个表格时会提示你输入
	username = StringField ('用户名', validators=[DataRequired (message='请输入用户名')])
	password = PasswordField ('密码', validators=[DataRequired (message='请输入密码')])
	remember_me = BooleanField ('记住我')
	submit = SubmitField ('登录')


class RegisterationForm (FlaskForm):
	username = StringField ('用户名', validators=[DataRequired (message='请输入注册用户名')])
	email = StringField ('邮箱', validators=[DataRequired (message='请输入注册邮箱地址'), Email ()])
	password = PasswordField ('密码', validators=[DataRequired (message='请输入注册密码')])
	password2 = PasswordField ('重复密码', validators=[DataRequired (message='请再次输入注册密码'), EqualTo ('password')])
	submit = SubmitField ('注册')

	# 校验用户名是否重复
	def validate_username(self, username):
		user = User.query.filter_by (username=username.data).first ()
		if user is not None:
			raise ValidationError ('用户名重复了，请您重新输入!')

	# 校验邮箱是否重复
	def validate_email(self, email):
		user = User.query.filter_by (email=email.data).first ()
		if user is not None:
			raise ValidationError ('邮箱重复了，请您重新输入!')
