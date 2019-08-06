from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, InputRequired

from app.models import User


class LoginForm (FlaskForm):
	# DataRequired，当你在当前表格没有输入而直接到下一个表格时会提示你输入
	username = StringField ('用户名', validators=[DataRequired (message='请输入用户名')])
	password = PasswordField ('密码', validators=[DataRequired (message='请输入密码')])
	remember_me = BooleanField ('记住我')
	submit = SubmitField ('登录')


class RegisterationForm (FlaskForm):
	username = StringField ('用户名', validators=[DataRequired (message='请输入注册用户名')])
	# email = StringField ('邮箱', validators=[DataRequired (message='请输入注册邮箱地址'), Email ()])
	password = PasswordField ('密码', validators=[DataRequired (message='请输入注册密码')])
	password2 = PasswordField ('重复密码', validators=[DataRequired (message='请再次输入注册密码'), EqualTo ('password')])
	submit = SubmitField ('注册')

	# 校验用户名是否重复
	def validate_username(self, username):
		user = User.query.filter_by (username=username.data).first ()
		if user is not None:
			raise ValidationError ('用户名重复了，请您重新输入!')

	# 校验邮箱是否重复
	# def validate_email(self, email):
	# 	user = User.query.filter_by (email=email.data).first ()
	# 	if user is not None:
	# 		raise ValidationError ('邮箱重复了，请您重新输入!')


class EditProfileForm (FlaskForm):
	backend_ip = StringField ('后端IP地址', validators=[DataRequired (message='请输入后端IP地址!')])
	front_ip = StringField ('前端IP地址', validators=[DataRequired (message='请输入前端IP地址!')])
	db_ip = StringField ('数据库连接地址', validators=[DataRequired (message='请输入数据库连接地址!')])
	db_user = StringField ('数据库连接用户名/密码', validators=[DataRequired (message='请输入数据库用户名!')])
	xs = StringField ('向上库test连接名称(不可更改)')
	xs_legal = StringField ('数据库合规legal名称(不可更改)')
	submit = SubmitField ('提交')


class UploadForm (Form):
	avatar = FileField (validators=[FileRequired (),  # FileRequired必须上传
									FileAllowed (['txt', 'png', 'gif'])  # FileAllowed:必须为指定的格式的文件
									])
	desc = StringField (validators=[InputRequired ()])
