# encoding
# 用户注册
import json

import MySQLdb
import requests
from faker import Faker
import random as r

from src import host_mysql, user_mysql, passwd_mysql

f = Faker (locale='zh_CN')

auth = ('xiangshang', 'dx3vf~yDt6s57Dbfoo')
headers = {'Content-Type': 'application/json', 'AppVersionCode': '105', 'deviceBrand': 'Xiaomi',
		   'device': '02093A41-181E-40A3-A006-9E2D1AFD5664', 'appchannel': '1', 'platform_type': '2'}


# 发送短信验证码接口
def send_message(url, mobile):
	# print mobile_number
	url_reg = url + "/user/register/sendCode/" + mobile
	r = requests.get (url_reg, auth=auth)


# print (r.status_code)
# print (r.text)

# 查询验证码
def mysql_randomchar(mobile, db):
	# conn= MySQLdb.connect('10.40.1.25','zhangmeijia','Q84mFosl5P','xiangshang_test7')
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from mobile_validate where mobile='" + mobile + "' order by create_time desc limit 1"
	s = cur.execute (sql)
	results = cur.fetchall ()
	for row in results:
		vilidata = row[5]
	cur.close ()
	conn.commit ()
	conn.close ()
	return vilidata


# 把生成的手机号更新到user表
def insert_mobile(mobile, db):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "update user set mobile='" + mobile + "' order by id desc limit 1"
	s = cur.execute (sql)
	cur.close ()
	conn.commit ()
	conn.close ()


def user_id(mobile, db):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from user where mobile='" + mobile + "'"
	s = cur.execute (sql)
	results = cur.fetchall ()
	for row in results:
		user_id = row[0]
	cur.close ()
	conn.commit ()
	conn.close ()
	return user_id


# 提交注册信息接口
def sub_reg_info(url, mobile, vilidata):
	url_r = url + "/user/register/submit"
	params = {'mobile': mobile, 'mcode': vilidata, 'password': '96e79218965eb72c92a549dd5a330112',
			  'utmSource': 'XIANGSHANG_ANDROID_REGISTER_USER'}
	r = requests.post (url_r, data=json.dumps (params), auth=auth, headers=headers)


# print (r.status_code)
# print (r.text)

# 生成手机号码
def mobile():
	mobile = f.phone_number ()
	return mobile


# 生成实名信息
def realName():
	name = f.name ()
	return name


# 生成随机身份信息
def idCard():
	idCard = f.ssn ()
	return idCard


# 生成随机卡号（招商银行）
def bankCard():
	bank_front = '622588'  # 招商
	num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	bankCard = bank_front + r.choice (num_list) + r.choice (num_list) + r.choice (num_list) + r.choice (
		num_list) + r.choice (num_list) + r.choice (num_list) + r.choice (num_list) + r.choice (num_list) + r.choice (
		num_list) + r.choice (num_list)
	return bankCard


# 验证登录
session = requests.Session ()


def user_login(url, mobile, password):
	url_login = url + '/user/login'
	params = {'userName': mobile, 'password': password}

	r = session.post (url_login, data=json.dumps (params), auth=auth, headers=headers)
	code = r.json ()['code']
	message = r.json ()['message']
	if code == 200 and message == u'操作成功':
		# print (u'登录成功，测试通过')
		pass
	else:
		print (u'登录失败,测试不通过')
		print (r.text)


# 实名认证
def certification(url, name, id_card):
	# print real_name
	# print id_card
	url_cert = url + '/user/setting//authIdCard'
	params = {'realName': name, 'idCard': id_card}
	r = session.post (url_cert, data=json.dumps (params), auth=auth, headers=headers)
