# encoding=utf-8
# 用户实名接口开户

# session登录
import json

import requests

from src.user_register import url, auth, headers, mobile

session = requests.Session ()


def login(mobile, password):
	url_login = url + '/user/login'
	params = {'userName': mobile, 'password': password}

	r = session.post (url_login, data=json.dumps (params), auth=auth, headers=headers)
	code = r.json ()['code']
	message = r.json ()['message']
	if code == 200 and message == u'操作成功':
		print (u'登录成功，测试通过')
	else:
		print (u'登录失败,测试不通过')
		print (r.text)


if __name__ == '__main__':
	print (mobile ())
	login (mobile=mobile (), password='96e79218965eb72c92a549dd5a330112')
