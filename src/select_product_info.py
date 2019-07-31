# encoding = utf-8

# 查询是否存在该用户
import pymysql


def select_product_info(db, product_name, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db, charset='utf8')
	cur = conn.cursor ()
	sql = "select id,period,lower_limit,allow_auto_exit,expire_withdrawal_way from aut_product where name = \'" + str (product_name) + "\' and status=2 and joined_total_amount < raise_amount;"
	# print (sql)
	s = cur.execute (sql)
	results = cur.fetchall ()
	list = []
	for i in results:
		list.append (i[0])
		list.append (i[1])
		list.append (i[2])
		list.append(i[3])
		list.append (i[4])
	return list
	conn.commit ()
	cur.close ()
	conn.close ()


if __name__ == '__main__':
	spi = select_product_info ('xiangshang_test5', '再加息测试', '10.40.0.106', 'test_rw9', 'test_rw9')
	print (spi)
