# encoding=utf-8
import pymysql
import requests


# 解密
def decrypts(encrypts):
	url = "http://10.200.0.108:18090/decrypt/decrypts"
	headers = {"Content-Type": "application/x-www-form-urlencoded",
			   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
	payload = {}
	payload['encryptDataList'] = encrypts
	# print(payload)
	r = requests.post (url, data=payload, headers=headers)
	# print(r.text)
	d = r.json ()['data'][0]
	return d[payload['encryptDataList']]


# 加密
def encrypts(decrypts_mobile):
	url = "http://10.200.0.108:18090/decrypt/encrypts"
	headers = {"Content-Type": "application/x-www-form-urlencoded",
			   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
	payload = {}
	payload['plainDataList'] = decrypts_mobile
	# print(payload)
	r = requests.post (url, data=payload, headers=headers)
	# print(r.text)
	d = r.json ()['data'][0]
	return d[payload['plainDataList']]


def update_mobile(db, mobile, crypts_mobile, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "update user set mobile='" + mobile + "' where crypt_mobile='" + crypts_mobile + "';"
	# print (sql)
	cur.execute (sql)
	conn.commit ()
	cur.close ()
	conn.close ()
	return sql

#
# if __name__ == '__main__':
# 	crypt_mobile = decrypts ('75211219GnQpbUGHN/Hjcc1/mCeEcg==')
# 	print (crypt_mobile)
# 	mobile = encrypts ('15026509966')
# 	print (mobile)
