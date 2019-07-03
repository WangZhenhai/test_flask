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
# 	mobile = decrypts ('df198591FVc03LYMAhCJ2LlEXPOFzA')
# 	print (mobile)
# 	update_mobile (db="xiangshang_test11", mobile="13550043155", crypts_mobile="df198591FVc03LYMAhCJ2LlEXPOFzA",
# 				   host_mysql="172.25.1.45", user_mysql="test_rw", passwd_mysql="test_rw")
