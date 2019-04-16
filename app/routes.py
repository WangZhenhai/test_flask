import time
from datetime import datetime
import os
from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.forms import RegisterationForm, EditProfileForm, UploadForm
from app import app, db
# 导入表单处理方法
from app.forms import LoginForm
from app.models import User


@app.route ('/')
@app.route ('/index')
@login_required
def index():
	return render_template ('index.html')


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
			flash ("用户名或密码错误！")
			return redirect (url_for ('login'))
		login_user (user, remember=form.remember_me.data)
		next_page = request.args.get ('next')
		if not next_page or url_parse (next_page).netloc != '':
			next_page = url_for ('index')
		return redirect (next_page)
	return render_template ('login.html', form=form)


# 注销
@app.route ('/logout')
def logout():
	logout_user ()
	return redirect (url_for ('index'))


# 注册
@app.route ('/register', methods=['GET', 'POST'])
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
		flash ("恭喜你成为我们网站的新用户!")
		return redirect (url_for ('login'))
	return render_template ('register.html', form=form)


# 用户中心
@login_required
@app.route ('/user/<username>')
def user(username):
	user = User.query.filter_by (username=username).first_or_404 ()
	posts = [{'author': user, 'body': 'Test Post #1号'}, {'author': user, 'body': 'Test Post #2号'}]
	last_ip = request.remote_addr
	return render_template ('user.html', user=user, posts=posts, last_ip=last_ip)


# 显示最后登录
@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow ()
		current_user.last_ip = request.remote_addr
		db.session.commit ()


# 编辑个人资料
@app.route ('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm ()
	if form.validate_on_submit ():
		current_user.backend_ip = form.backend_ip.data
		current_user.front_ip = form.front_ip.data
		current_user.db_ip = form.db_ip.data
		db.session.commit ()
		flash ('你的提交已变更.')
		return redirect (url_for ('edit_profile'))
	elif request.method == 'GET':
		form.backend_ip.data = current_user.backend_ip
		form.front_ip.data = current_user.front_ip
		form.db_ip.data = current_user.db_ip
	return render_template ('edit_profile.html', title='编辑用户IP配置', form=form)


# 上传文件页面
@login_required
@app.route ('/upload', methods=['GET'], strict_slashes=False)
def upload():
	return render_template ('upload.html')


# 上传操作
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath (os.path.dirname (__file__))
ALLOWED_EXTENSIONS = set (['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF', 'zip'])


# 用于判断文件后缀
def allowed_file(filename):
	return '.' in filename and filename.rsplit ('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传文件
UPLOAD_PATH = os.path.join (os.path.dirname (__file__), '../static/images')


@app.route ('/upload/', methods=['GET', 'POST'])
def settings():
	if request.method == 'GET':
		return render_template ('upload.html')
	else:
		# 文件是从request,files里面获取，这里使用CombinedMultiDict把form和file的数据组合起来，一起验证
		form = UploadForm (CombinedMultiDict ([request.form, request.files]))
		if form.validate ():
			desc = request.form.get ('desc')
			avatar = request.files.get ('avatar')
			# 对文件名进行包装，为了安全,不过对中文的文件名显示有问题
			filename = secure_filename (avatar.filename)
			avatar.save (os.path.join (UPLOAD_PATH, filename))
			print (desc)
			return '文件上传成功'
		else:
			print (form.errors)
			return "fail"

#查看文件
@app.route ('/images/<filename>/', methods=['GET', 'POST'])
def get_image(filename):
	return send_from_directory (UPLOAD_PATH, filename)
