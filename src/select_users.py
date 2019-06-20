# encoding=utf-8
# Note:查询最新注册的10个用户
import MySQLdb

from src.user_register import host_mysql, user_mysql, passwd_mysql


def select_users(db, count):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from user order by id desc limit %d" % count
	s = cur.execute (sql)
	results = cur.fetchall ()
	list = []
	# list.clear ()
	for row in results:
		user_id = row[0]
		mobile = row[4]
		list.append (user_id)
		list.append (mobile)
	return results
	cur.close ()
	conn.commit ()
	conn.close ()

# if __name__ == '__main__':
# 	su = select_users ("xiangshang_test5",1)
# 	print (str (su))
