# encoding = utf-8

# 查询是否存在该用户
import pymysql


def select_user_id(db, crypt_mobile, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "select id from user where crypt_mobile = '" + crypt_mobile + "'"
	# print (sql)
	s = cur.execute (sql)
	results = cur.fetchall ()
	for id in results:
		return id[0]
	conn.commit ()
	cur.close ()
	conn.close ()


# if __name__ == '__main__':
# 	sui = select_user_id ('xiangshang_test5', '66f9500gp+1E0o0IU75N9/GvUKlXg==', '10.40.0.106', 'test_rw9', 'test_rw9')
# 	print (sui)
