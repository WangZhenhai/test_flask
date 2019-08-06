# encoding=utf-8

# 查询产品期限
import pymysql


def select_period(db, goods_id, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "SELECT period from xiangshang_test5.aut_product WHERE id='" + str (goods_id) + "'"
	s = cur.execute (sql)
	results = cur.fetchall ()
	for period in results:
		return period[0]
	cur.close ()
	conn.commit ()
	conn.close ()

#
# if __name__ == '__main__':
# 	sp = select_period ('xiangshang_test5', '3003', '10.40.0.106', 'test_rw9', 'test_rw9')
# 	print (sp)
