# encoding=utf-8
# 对开户的账户进行转账，单笔最大默认1万

# 更新向上库user_point
import MySQLdb
import requests



def recharge5425(backend_ip, bank_user_id):
	url = 'http://' + backend_ip + ':19910/fds/trans/request/5425'
	auth = ('admin', 'admin')
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0",
			   "Content-Type": "application/x-www-form-urlencoded"}
	payload = {'qydm': '5425', 'classFullName': 'com.xiangshang.fds.model.request.Request5425', 'paramJson': '[{"name":"qydm","value":"5425"},{"name":"classFullName",\
"value":"com.xiangshang.fds.model.request.Request5425"},{"name":"paramJson","value":""},{"name":"Reserve","value":""},{"name":"FuncFlag","value":"1"},{"name":\
"OutCustAcctId","value":"6034000000000010"},{"name":"OutCustName","value":"\xd7\xd4\xd3\xd0\xd7\xca\xbd\xf0\xd7\xd3\xd5\xcb\xba\xc5"},{"name":\
"InCustAcctId","value":"6034000000112178"},{"name":"InThirdCustId","value":""},{"name":"InCustName","value":"0"},{"name":"TranAmount","value":"10000"},{"name":\
"TranType","value":"0"},{"name":"Note","value":""}]', 'Reserve': '', 'FuncFlag': '1',
			   'OutCustAcctId': '6034000000000010', 'OutCustName': '', 'InCustAcctId': '6034000000112178',
			   'InThirdCustId': '', 'InCustName': '0', 'TranAmount': '10000', 'TranType': '0', 'Note': ''}
	param_json = payload['paramJson']
	param_json = param_json[:338] + bank_user_id + param_json[354:]
	payload['paramJson'] = param_json
	payload['InCustAcctId'] = bank_user_id
	# print (payload)
	r = requests.post (url, data=payload, auth=auth, headers=headers)
	# print (r.text)


def update_user_point(user_id, db,host_mysql, user_mysql, passwd_mysql):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, db)
	cur = conn.cursor ()
	sql = "select * from user_point where user_id='" + str (user_id) + "'"
	cur.execute (sql)
	results = cur.fetchall ()
	if results == ():
		return "user_point中user_id不存在"
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
def update_user_account(user_id, legal_db,host_mysql, user_mysql, passwd_mysql):
	conn = MySQLdb.connect (host_mysql, user_mysql, passwd_mysql, legal_db)
	cur = conn.cursor ()
	sql = "select * from user_account where user_id='" + str (user_id) + "'"
	cur.execute (sql)
	results = cur.fetchall ()
	if results == ():
		return "user_account中user_id不存在"
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
# 	backend_ip = '10.40.1.150'
# 	bank_user_id = '6034000000126627'
# 	rc = recharge5425 (backend_ip, bank_user_id)
# 	print (rc)
