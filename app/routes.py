import logging
import sys
from datetime import datetime

from bs4 import BeautifulSoup
import pysnooper
import requests
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import os, subprocess

from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.forms import RegisterationForm, EditProfileForm
from app import app, db
# 导入表单处理方法
from app.forms import LoginForm
from app.models import User

getcwd = os.getcwd ()
getabspath = os.path.abspath (os.path.join (os.getcwd (), ".."))
session = requests.Session ()


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
		user = User (username=form.username.data)
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
	last_ip = request.remote_addr
	return render_template ('user.html', user=user, last_ip=last_ip)


# 显示最后登录
@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow ()
		current_user.last_ip = request.remote_addr
		db.session.commit ()


# 编辑个人资料
@app.route ('/user/edit_profile', methods=['GET', 'POST'])
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
		form.xs.data = current_user.xs
		form.xs_legal.data = current_user.xs_legal
	return render_template ('edit_profile.html', title='编辑用户IP配置', form=form)


# testAjax
@login_required
@app.route ('/test')
def test():
	return render_template ('test.html')


@login_required
@app.route ('/addnumber')
def add():
	a = request.args.get ('a', 0, type=float)
	b = request.args.get ('b', 0, type=float)
	return jsonify (result=a + b)


# testBAT
@login_required
@app.route ('/test2')
def test2():
	return render_template ('test2.html')


def decode(s):
	try:
		return s.decode ('utf-8')
	except UnicodeDecodeError:
		return s.decode ('gbk')


# 默认执行程序
@login_required
@app.route ('/run', methods=['POST'])
def run():
	exec = sys.executable
	file = "test/test.py"
	return decode (subprocess.check_output ([exec, file], stderr=subprocess.STDOUT, timeout=5))


# 理财用户信息
@login_required
@app.route ('/user/lender_info')
def lender_info():
	return render_template ("leader_info.html")


# 生成理财人注册信息
@login_required
@pysnooper.snoop ()
@app.route ('/user/lender_info', methods=['POST'])
def lender_msg():
	# exec = sys.executable
	filename = request.values.get ("filename")
	if filename == "":
		flash ("文件名称为必填项，不能为空！")
		return redirect (url_for ('lender_info'))
	else:
		url = "http://10.200.0.72:11987/generateData/generateRandomPeopleInfo"
		soup = BeautifulSoup (requests.get (url).text, 'html.parser')
		td_list = soup.find_all ('td')
		f = open (getcwd + '\\uploads\\' + current_user.username + "\\" + filename, 'w', encoding='utf8')
		for i in range (len (td_list)):
			if str (i)[-1] == '1' or str (i)[-1] == '5' or str (i)[-1] == '6':
				f.write (td_list[i].get_text () + ',')
			elif str (i)[-1] == '7':
				f.write (td_list[i].get_text () + '\n')
		f.close ()
		flash ("生成数据完成！")
		return redirect (url_for ('lender_info'))  # return requests.get (url).text


@login_required
@pysnooper.snoop ()
@app.route ('/user/see_lender_msg', methods=['GET', 'POST'])
def see_lender_msg():
	filename = request.values.get ("filename")
	if filename == "":
		errmsg = "文件名称为必填项，不能为空！"
		return render_template ("leader_info.html", errmsg=errmsg)
	else:
		with open (getcwd + '\\uploads\\' + current_user.username + "\\" + filename, encoding='utf8') as rf:
			L = []
			for line in rf.readlines ():
				L.append (line.strip ('\n'))

			return str (L)


# 借款人信息
@login_required
@app.route ('/user/borrowers_info')
def borrowers_info():
	return render_template ("borrowers_info.html")


# 新的理财人信息页面
@login_required
@app.route ('/user/lender')
def lender():
	return render_template ("lender.html")


# 用户一键注册
@login_required
@app.route ('/user/user_register', methods=['POST'])
def user_register():
	# exec = sys.executable
	# file = "src/user_register.py"
	# return decode (subprocess.check_output ([exec, file], stderr=subprocess.STDOUT, timeout=30))
	from src.user_register import mobile, send_message, sub_reg_info, mysql_randomchar, insert_mobile, certification, \
		realName, idCard, user_id, user_login, bankCard
	from src.openbank_v2 import login_web, open_bank_depository, bank_account

	url = "http://" + str (current_user.username) + ".app.xs.sit/app"
	web_url = "http://" + str (current_user.username) + ".www.xs.sit/xweb"
	db = current_user.xs
	m = mobile ()
	name = realName ()
	idcard = idCard ()
	# name = "刘宪鹏"
	# idcard = "130430199312290159"

	# print (m)  # 输出生成手机号
	send_message (url=url, mobile=m)  # 获取注册验证码
	sub_reg_info (url=url, vilidata=mysql_randomchar (m, db=db), mobile=m)  # 注册
	insert_mobile (mobile=m, db=db)  # 更新user表mobile字段
	# print (user_id (mobile=m, db=db))  # 打印user_id
	bankcard = bankCard ()  # 打印银行卡号
	user_login (url=url, mobile=m, password='96e79218965eb72c92a549dd5a330112')  # 登录
	certification (url=url, name=name, id_card=idcard)  # 实名
	login_web (mobile_number=m, password='96e79218965eb72c92a549dd5a330112', web_url=web_url)
	open_bank_depository (web_url)
	bank_account (card_num=bankcard, mobile_number=m)
	info_list = []  # 输出用户信息
	info_list.append (user_id (mobile=m, db=db))
	info_list.append (m)
	info_list.append (name)
	info_list.append (idcard)
	return render_template ("lender.html", register_info=str (info_list))


# 备用银行开户（一键开户）
@login_required
@app.route ('/user/openbank', methods=['POST'])
def openbank():
	from src.openbank_v2 import login_web, open_bank_depository, bank_account
	from src.user_register import bankCard
	web_url = "http://" + str (current_user.username) + ".www.xs.sit/xweb"
	bankcard = bankCard ()
	openbank_mobile = request.values.get ("openbank")
	if openbank_mobile == "":
		msg = "手机号码必填"
		return render_template ("lender.html", msg=msg)
	elif openbank_mobile.isdigit () is False:
		msg = "手机号格式错误"
		return render_template ("lender.html", msg=msg)
	else:
		mobile = openbank_mobile
		login_web (mobile_number=mobile, password='96e79218965eb72c92a549dd5a330112', web_url=web_url)
		open_bank_depository (web_url=web_url)
		bank_account (card_num=bankcard, mobile_number=mobile)
		return render_template ("lender.html")


# 生成银行卡
@login_required
@app.route ('/user/bankcard', methods=['post'])
def bankcard():
	from src.user_register import bankCard
	bankcard = bankCard ()
	return render_template ("lender.html", bankcard=bankcard)


# 一键转账
@login_required
@app.route ('/user/transter_account', methods=['POST'])
def traster_account():
	from src.transfer_account import update_user_account, update_user_point, recharge5425
	from src.select_users import bank_user_id
	db = current_user.xs
	legal_db = current_user.xs_legal
	user_id = request.values.get ('user_id')
	backend_ip = current_user.backend_ip
	if user_id == "" or user_id.isdigit () is False:
		errmsg = "用户user_id输入有误！"
		return render_template ("lender.html", errmsg=errmsg)
	else:
		user_id = str (user_id)
		if update_user_account (user_id=user_id, legal_db=legal_db) != "转账完成":
			errmsg = "user_id在user_account中不存在或该用户未开通银行存管"
			return render_template ("lender.html", errmsg=errmsg)
		elif update_user_point (user_id=user_id, db=db) != "转账完成":
			errmsg = "user_id在user_point中不存在"
			return render_template ("lender.html", errmsg=errmsg)
		else:
			bank_user_id = bank_user_id (legal_db=legal_db, user_id=user_id)
			recharge5425 (backend_ip=backend_ip, bank_user_id=bank_user_id)
			msg = ("转账完成！")
			return render_template ("lender.html", errmsg=msg)


# 通过用户id查询该用户的相关信息
@login_required
@app.route ('/user/user_info', methods=['POST'])
def user_info():
	from src.select_users import select_all
	db = current_user.xs
	legal_db = current_user.xs_legal
	user_id = request.values.get ('user_info')
	if user_id == "" or user_id.isdigit () is False:
		u_msg = "用户user_id输入有误！"
		return render_template ("lender.html", u_msg=u_msg)
	else:
		user_id = str (user_id)
		sa = select_all (xs_db=db, legal_db=legal_db, user_id=user_id)
		return render_template ("user_info.html", sa=sa)


# 用户查询（最新注册的10个用户）
@login_required
@app.route ('/user/select_users', methods=['POST'])
def select_users():
	from src.select_users import select_users
	db = current_user.xs
	count = request.values.get ("count")
	if count == "" or count.isdigit () is False:
		count = 10
	else:
		count = count
	su = select_users (db=db, count=int (count))
	return render_template ("select_users.html", su=su)


# 删除用户订单（还原新用户）
@login_required
@app.route ('/user/del_order', methods=['POST'])
def del_user_order():
	from src.del_user_order import del_xs, del_legal
	xs_db = current_user.xs
	legal_db = current_user.xs_legal
	user_id = request.values.get ("del_user_order")
	if user_id == "" or user_id.isdigit () is False:
		del_msg = "user_id不能为空或输入格式错误"
		return render_template ("lender.html", del_msg=del_msg)
	else:
		del_xs (user_id=user_id, xs_db=xs_db)
		del_legal (user_id=user_id, legal_db=legal_db)
		del_msg = "删除完成"
		return render_template ("lender.html", del_msg=del_msg)


# uploads File
@login_required
@app.route ('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		basepath = os.path.dirname (__file__)
		upload_path = os.path.join (basepath, '..\\uploads\\' + current_user.username, secure_filename (f.filename))
		f.save (upload_path)
		return redirect ('upload')
	return render_template ('upload.html')


# 404错误页面
@login_required
@app.errorhandler (404)
def page_not_found(error):
	return render_template ('404.html'), 404


# 500错误页面
@login_required
@app.errorhandler (500)
def page_not_found(error):
	return render_template ('500.html'), 500
