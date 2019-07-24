# encoding = utf-8

# 通过用户id查询该用户的银行卡号
import pymysql


def bank_card_by_userid(db, user_id, host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=db)
	cur = conn.cursor ()
	sql = "SELECT bank_card_no from xiangshang_test5.bank_open_account_record WHERE user_id='" + user_id + "'"
	# print (sql)
	s = cur.execute (sql)
	results = cur.fetchall ()
	for bank_card in results:
		return bank_card[0]
	cur.close ()
	conn.commit ()
	conn.close ()

#
# if __name__ == '__main__':
# 	bank_card = bank_card_by_userid ('xiangshang_test5', '6525806', '10.40.0.106', 'test_rw9', 'test_rw9')
# 	print (bank_card)
