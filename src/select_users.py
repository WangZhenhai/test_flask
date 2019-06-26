# encoding=utf-8
# Note:查询最新注册的10个用户
import pymysql

from src import host_mysql, user_mysql, passwd_mysql


def select_users(db, count):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "select * from user order by id desc limit %d" % count
	s = cur.execute (sql)
	results = cur.fetchall ()
	return results
	cur.close ()
	conn.commit ()
	conn.close ()


def bank_user_id(legal_db, user_id):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=legal_db)
	cur = conn.cursor ()
	sql = "select * from user_account where user_id= %s" % user_id
	s = cur.execute (sql)
	results = cur.fetchall ()
	# return results
	for i in results:
		bank_user_id = i[2]
	return bank_user_id
	cur.close ()
	conn.commit ()
	conn.close ()


# if __name__ == '__main__':
# 	b = bank_user_id ("xiangshang_legal_test5", "6525768")
# 	print (b)
