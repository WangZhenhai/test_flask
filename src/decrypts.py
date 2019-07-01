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


# if __name__ == '__main__':
# 	# mobile = decrypts ('a178d08ekQXDbh3JKR2vCTBvQr1x/Q==')
# 	# 	 print (mobile)
# 	update_mobile (db="xiangshang_test7", mobile="15199600413", crypts_mobile="e77ef94fB6e0/hOMQ9LSgsDn1uuhVg==",
# 				   host_mysql="10.40.0.106", user_mysql="test_rw9", passwd_mysql="test_rw9")
