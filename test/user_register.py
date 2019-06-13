# encoding
# 用户注册
import json

import MySQLdb
import requests
from faker import Faker

f = Faker (locale='zh_CN')

host_mysql = '10.40.0.106'
user_mysql = 'test_rw9'
passwd_mysql = 'test_rw9'
db_mysql = 'xiangshang_test5'

url = "http://test5.app.xs.sit/app"
auth = ('xiangshang', 'dx3vf~yDt6s57Dbfoo')
headers = {'Content-Type': 'application/json', 'AppVersionCode': '73', 'deviceBrand': 'Xiaomi',
		   'device': '02093A41-181E-40A3-A006-9E2D1AFD5664', 'appchannel': '1', 'platform_type': '2'}


# 发送短信验证码接口
def send_message(mobile):
	# print mobile_number
	url_reg = url + "/user/register/sendCode/" + mobile
	r = requests.get (url_reg, auth=auth)


# print (r.status_code)
# print (r.text)

# 查询验证码
def mysql_randomchar(mobile):
	# conn= MySQLdb.connect('10.40.1.25','zhangmeijia','Q84mFosl5P','xiangshang_test7')
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db_mysql)
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


def insert_mobile(mobile):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db_mysql)
	cur = conn.cursor ()
	sql = "update user set mobile='" + mobile + "' order by id desc limit 1"
	s = cur.execute (sql)
	cur.close ()
	conn.commit ()
	conn.close ()


# 提交注册信息接口
def sub_reg_info(vilidata, mobile):
	url_r = url + "/user/register/submit"
	params = {'mobile': mobile, 'mcode': vilidata, 'password': '96e79218965eb72c92a549dd5a330112',
			  'utmSource': 'XIANGSHANG_ANDROID_REGISTER_USER'}
	r = requests.post (url_r, data=json.dumps (params), auth=auth, headers=headers)
	# print (r.status_code)
	# print (r.text)


if __name__ == '__main__':
	mobile = f.phone_number ()
	print (mobile)
	send_message (mobile=mobile)
	sub_reg_info (vilidata=mysql_randomchar (mobile), mobile=mobile)
	insert_mobile (mobile=mobile)
