# encoding=utf-8
# 对开户的账户进行转账，单笔最大默认1万

# 更新向上库user_point
import MySQLdb

from src import host_mysql, user_mysql, passwd_mysql


def update_user_point(user_id, db):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from user_point where user_id='" + str(user_id)+"'"
	s = cur.execute (sql)
	results = cur.fetchall ()
	for row in results:
		available_points = row[1]
	new_avaliable_points = available_points + 10000
	sql = "update user_point set available_points='" + str(new_avaliable_points) + "' where user_id='" + str(user_id)+"'"
	print(sql)
	s = cur.execute (sql)
	cur.close ()
	conn.commit ()
	conn.close ()
	return available_points


if __name__ == '__main__':
	update_user_point (user_id='6525745', db='xiangshang_test5')
