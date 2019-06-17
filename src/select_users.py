# encoding=utf-8
# Note:查询最新注册的10个用户
import MySQLdb

from src.user_register import host_mysql, user_mysql, passwd_mysql, db_mysql


def select_users():
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db_mysql)
	cur = conn.cursor ()
	sql = "select * from user order by id desc limit 10"
	s = cur.execute (sql)
	results = cur.fetchall ()
	list = []
	# list.clear ()
	for row in results:
		mobile = row[4]
		list.append (mobile)
	cur.close ()
	conn.commit ()
	conn.close ()
	return list
