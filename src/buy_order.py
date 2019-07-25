# encoding = utf-8
# 封装用户购买接口
import os
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from src.select_period import select_period

basepath = os.path.dirname (__file__)
s = requests.session ()


def login_web(mobile_number, password, web_url):
	url = web_url + "/login/check"
	payload = {'username': '', 'validateCode': '', 'messageCodeRegister': False, 'password': password}
	payload['username'] = str (mobile_number)
	headers = {'Content-Type': 'application/x-www-form-urlencoded',
			   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	r = s.post (url, data=payload, headers=headers)


def ordermoney(web_url, goodsId, amount):
	url = web_url + "/buy/ordermoney"
	payload = {"goodsId": goodsId, "goodsType": "AUTHORIZE", "amount": amount}
	headers = {'Content-Type': 'application/x-www-form-urlencoded',
			   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	r = s.post (url, data=payload, headers=headers)
	# print(r.text)
	html = r.text
	soup = BeautifulSoup (html, 'lxml')
	token = soup.find_all (id='token')[0].get ('value')
	return token


def authBalancepay(web_url, amount, goodsId, cardNumber, token):
	url = web_url + "/buy/authBalancepay"
	payload = {"buyerAmount": amount, "bankPayAmount": "0", "planId": goodsId, "goodsId": goodsId,
			   "goodsType": "AUTHORIZE", "bankCode": "$item.bankCode", "cardNumber": cardNumber, "jxId": "", "dcId": "",
			   "zkjId": "", "lcjId": "", "couponAmount": "", "token": token, "channelCode": "", "isSafe": False,
			   "joinFee": "0.0", "safeAmount": "", "payPassword": "", "autOrderId": "", "continueBuyType": "",
			   "payType": "0"}
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	r = s.get (url, params=payload, headers=headers)
	# print (r.text)
	bus_order_no = r.json ()['data']['busOrderNo']
	print (bus_order_no)
	return bus_order_no


def authindex(web_url, bus_order_no, period, amount):
	url = web_url + "/OpenBankDepository/authindex"
	payload = {"url": "", "period": period, "amt": amount, "busOrderNo": bus_order_no, "goodsType": "AUTHORIZE"}
	payload['url'] = web_url + "/static/autSuc?busOrderNo=" + bus_order_no
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	r = s.get (url, params=payload, headers=headers)
	data = r.json ()['data']
	bankServiceUrl = data['bankServiceUrl']
	bank_request_vo = data['bankRequestVo']
	orig = bank_request_vo['orig']
	sign = bank_request_vo['sign']
	returnurl = bank_request_vo['returnurl']
	NOTIFYURL = bank_request_vo['NOTIFYURL']
	userType = bank_request_vo['userType']
	# filepath = os.path.join (basepath, '..\\templates\\')
	filepath = os.path.join (basepath, '..\\src\\')
	f = open (filepath + "buy.html", 'w')
	f.write ('<!doctype html>')
	f.write ('\n')
	f.write ('<html>')
	f.write ('\n')
	f.write ('<head>')
	f.write ('\n')
	f.write ('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
	f.write ('\n')
	f.write ('</head>')
	f.write ('\n')
	f.write ('<body>')
	bank_service_url = '''<form id="PayForm" name="PayForm" action=''' + bankServiceUrl + ''' autocomplete="off" method="post">'''
	f.write (bank_service_url)
	f.write ('\n')
	f.write ('\n')
	orig = '''    <input type="hidden" name="orig" value="''' + orig + '''">'''
	f.write (orig)
	f.write ('\n')
	sign = '''    <input type="hidden" name= "sign" value="''' + sign + '''">'''
	f.write (sign)
	f.write ('\n')
	returnurl = '''    <input type="hidden" name= "returnurl" value="''' + returnurl + '''">'''
	f.write (returnurl)
	f.write ('\n')

	f.write ('''    <input type="hidden" name= "NOTIFYURL" value="http://118.244.227.120:12403/callback/notify">''')
	f.write ('\n')

	f.write ('''    <input type="hidden" name= "userType" value="0">''')
	f.write ('\n')
	f.write (''' <input type="submit" value="submit" style="position:absolute;top:20%;left:20%">''')
	f.write ('\n')
	f.write ('''</form>''')
	f.write ('\n')
	f.write ('</body>')
	f.write ('\n')
	f.write ('</html>')


def buy(local_ip):
	driver = webdriver.Remote (command_executor=local_ip + ':4444/wd/hub',
							   desired_capabilities=DesiredCapabilities.CHROME)
	driver.maximize_window ()

	path_dir = str (os.path.abspath (os.path.join (os.path.dirname (__file__), os.pardir)))
	print (path_dir)
	url = 'file://' + path_dir + '/src/buy.html'
	# url = 'http://' + local_ip + ':81/buy'
	# url = 'http://' + local_ip + '/buy'
	driver.get (url)
	driver.find_element_by_xpath ("//input[@type='submit']").click ()
	driver.find_element_by_xpath ("//*[@id='queryButton']").click ()
	driver.find_element_by_xpath ("//*[@id='mobilePwd']").send_keys ('111111')
	js1 = "$('#keyboards').val('xs111111');"
	driver.execute_script (js1)
	driver.find_element_by_xpath ("//*[@id='submitButton']").click ()
	time.sleep (10)
	driver.quit ()

#
# if __name__ == '__main__':
# 	web_url = 'http://test5.www.xs.sit/xweb/'
# 	amount = '1000'
# 	goodsId = '3680'
# 	cardno = '622588****3358'
# 	login = login_web ('15316563887', '96e79218965eb72c92a549dd5a330112', web_url)
# 	token = ordermoney (web_url, '3680', '1000')
# 	period = select_period ('xiangshang_test5', goodsId, '10.40.0.106', 'test_rw9', 'test_rw9')
# 	bus_order_no = authBalancepay (web_url, amount, goodsId, cardno, token)
# 	authindex = authindex (web_url, bus_order_no, period, amount)
# 	time.sleep (5)
# 	b = buy ('10.200.1.59')
# 	print (token)
# 	print (bus_order_no)
