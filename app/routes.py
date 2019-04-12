from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import RegisterationForm
from app import app, db
# 导入表单处理方法
from app.forms import LoginForm
from app.models import User


@app.route ('/')
@app.route ('/index')
@login_required
def index():
	user = {'username': 'duke'}
	posts = [{'author': {'username': '刘'}, 'body': '这是模板模块中的循环例子～1'},
			 {'author': {'username': '忠强'}, 'body': '这是模板模块中的循环例子～2'}]
	return render_template ('index.html', title='我的', user=user, posts=posts)


# 登录
@app.route ('/login', methods=['GET', 'POST'])
def login():
	# 判断当前用户是否进行验证
	if current_user.is_authenticated:
		return redirect (url_for ('index'))
	form = LoginForm ()
	# 对表单进行验证
	if form.validate_on_submit ():
		# 查询表用户
		user = User.query.filter_by (username=form.username.data).first ()
		if user is None or not user.check_password (form.password.data):
			flash ('用户名或密码错误！')
			return redirect (url_for ('login'))
		login_user (user, remember=form.remember_me.data)
		next_page = request.args.get ('next')
		if not next_page or url_parse (next_page).netloc != '':
			next_page = url_for ('index')
		return redirect (next_page)
	return render_template ('login.html', title='登录', form=form)


# 注销
@app.route ('/logout')
def logout():
	logout_user ()
	return redirect (url_for ('index'))


# 注册
@app.route ('/register')
def register():
	# 判断当前用户是否验证，如果通过的话返回首页
	if current_user.is_authenticated:
		return redirect (url_for ('index'))
	form = RegisterationForm ()
	if form.validate_on_submit ():
		user = User (username=form.username.data, email=form.email.data)
		user.set_password (form.password.data)
		db.session.add (user)
		db.session.commit ()
		flash ('恭喜你成为我们网站的新用户!')
		return redirect (url_for ('login'))
	return render_template ('register.html', title='注册', form=form)


# 用户中心
@app.route ('/user/<username>')
def user(username):
	user = User.query.filter_by (username=username).first_or_404 ()
	posts = [{'author': user, 'body': 'Test Post #1号'}, {'author': user, 'body': 'Test Post #1号'}]
	return render_template ('user.html', user=username, posts=posts)
