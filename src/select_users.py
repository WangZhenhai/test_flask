# encoding=utf-8
# Note:查询最新注册的10个用户
import pymysql

from src import host_mysql, user_mysql, passwd_mysql


# 查询用户信息
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


# 查询bank_user_id
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
	conn.commit ()
	cur.close ()
	conn.close ()


def select_all(xs_db, legal_db, user_id):
	list = []
	conn_xs = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=xs_db)
	cur_xs = conn_xs.cursor ()
	sql_xs = "select user.id,user.mobile,user.bank_user_id,user_point.available_points from user,user_point where user.id=user_point.user_id and user.id = %s" % user_id
	cur_xs.execute (sql_xs)
	conn_xs.commit ()
	results_xs = cur_xs.fetchall ()
	for i in results_xs:
		list.append (i[0])
		list.append (i[1])
		list.append (i[2])
		list.append (i[3])
	cur_xs.close ()
	conn_xs.close ()
	#
	conn_legal = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=legal_db)
	cur_legal = conn_legal.cursor ()
	sql_legal = "select arrive_amount from user_account where user_id = %s" % user_id
	cur_legal.execute (sql_legal)
	conn_legal.commit ()
	results_legal = cur_legal.fetchall ()
	for i in results_legal:
		list.append (i[0])
	cur_legal.close ()
	conn_legal.close ()

	return list


# if __name__ == '__main__':
# 	s = select_all ("xiangshang_test5", "xiangshang_legal_test5", "6525781")
# 	print (s)
