from flask import render_template, flash, redirect, url_for
from app import app
# 导入表单处理方法
from app.forms import LoginForm


@app.route ('/')
@app.route ('/index')
def index():
	user = {'username': 'duke'}
	posts = [{'author': {'username': '刘'}, 'body': '这是模板模块中的循环例子～1'},
			 {'author': {'username': '忠强'}, 'body': '这是模板模块中的循环例子～2'}]
	return render_template ('index.html', title='我的', user=user, posts=posts)


@app.route ('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm ()
	if form.validate_on_submit ():
		flash ('用户登录的用户名是：{},是否记住我:{}'.format (form.username.data, form.remember_me.data))
		return redirect (url_for ('/index'))
	return render_template ('login.html', title='登录', form=form)
