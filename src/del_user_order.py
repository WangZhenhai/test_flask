# Fencoding=utf-8

# function：删除用户名下所有的订单
import pymysql



def del_xs(user_id, xs_db,host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.Connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=xs_db)
	cur = conn.cursor ()
	t_list = ['aut_order_form', 'financeplan_subpoint_orderform ', 'dt_agreement', 'instalment_repayment_order_form',
			  'aut_taste_orderform', 'aut_continuing_invest_plan', 'order_continue_relation',
			  'aut_order_form_plus_rate', 'aut_order_exit_apply', 'act_order_form', 'transfer_apply_wait',
			  'user_point_log', 'sign_agreement', 'sign_join_plan', 'user_virtual_account_log', 'activity_task_event',
			  'user_virtual_account', 'lend_apply_wait', 'user_virtual_account_log', 'aut_order_exit_detail']
	for s in t_list:
		sql = "DELETE FROM " + s + " WHERE user_id = " + str (user_id) + ";"
		cur.execute (sql)
		conn.commit ()
		# print ('共删除了', cur.rowcount, '条数据');

	cur.close ()


def del_legal(user_id, legal_db,host_mysql, user_mysql, passwd_mysql):
	conn = pymysql.Connect (host=host_mysql, port=3306, user=user_mysql, passwd=passwd_mysql, db=legal_db)
	cur = conn.cursor ()
	t_list = ['aut_order_match_apply', 'user_account_log']
	for s in t_list:
		sql = "DELETE FROM " + s + " WHERE user_id = " + str (user_id) + ";"
		# print (sql)
		cur.execute (sql)
		conn.commit ()
		# print ('共删除了', cur.rowcount, '条数据');

	cur.close ()

#
# if __name__ == '__main__':
# 	del_xs ('1', 'xiangshang_test5')
# 	del_legal ('1', 'xiangshang_legal_test5')
