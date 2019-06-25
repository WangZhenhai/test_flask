# encoding=utf-8
# 对开户的账户进行转账，单笔最大默认1万

# 更新向上库user_point
import MySQLdb

from src import host_mysql, user_mysql, passwd_mysql


def update_user_point(user_id, db):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from user_point where user_id='" + str (user_id) + "'"
	cur.execute (sql)
	results = cur.fetchall ()
	if results == ():
		print ("user_point中user_id不存在")
	else:
		for row in results:
			available_points = row[1]
		new_avaliable_points = available_points + 10000
		sql_u = "update user_point set available_points='" + str (new_avaliable_points) + "' where user_id='" + str (
			user_id) + "'"
		cur.execute (sql_u)
		conn.commit ()
		return "转账完成"
	cur.close ()
	conn.close ()


# 更新合规库
def update_user_account(user_id, legal_db):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, legal_db)
	cur = conn.cursor ()
	sql = "select * from user_account where user_id='" + str (user_id) + "'"
	cur.execute (sql)
	results = cur.fetchall ()
	if results == ():
		print ("user_account中user_id不存在")
	else:
		for row in results:
			arrive_amount = row[7]
		new_arrive_amount = arrive_amount + 10000
		sql_u = "update user_account set arrive_amount=" + str (new_arrive_amount) + " where user_id='" + str (
			user_id) + "'"
		cur.execute (sql_u)
		conn.commit ()
		return "转账完成"
	cur.close ()
	conn.close ()

#
# if __name__ == '__main__':
# 	uup = update_user_point ('6525765', 'xiangshang_test5')
# 	uua = update_user_account ('6525765', 'xiangshang_legal_test5')
# 	print (uup)
# 	print (uua)
