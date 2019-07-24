# encoding = utf-8

# 查询产品id 是否可购买
import pymysql


def select_goods_id(db, goods_id, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "SELECT id from xiangshang_test5.aut_product WHERE id='" + goods_id + "'"
	s = cur.execute (sql)
	results = cur.fetchall ()
	for id in results:
		return id[0]
	cur.close ()
	conn.commit ()
	conn.close ()


# if __name__ == '__main__':
# 	sgi = select_goods_id ('xiangshang_test5', '3003', '10.40.0.106', 'test_rw9', 'test_rw9')
# 	print (sgi)
