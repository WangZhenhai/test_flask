# encoding = utf-8
# 银行开户 v2.0
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

basepath = os.path.dirname (__file__)
session = requests.Session ()


def login_web(mobile_number, password, web_url):
	url = web_url + "/login/check"
	payload = {'username': '', 'validateCode': '', 'messageCodeRegister': False, 'password': password}
	payload['username'] = str (mobile_number)
	headers = {'Content-Type': 'application/x-www-form-urlencoded',
			   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	r = session.post (url, data=payload, headers=headers)
	# return r.text


def open_bank_depository(web_url):
	url = web_url + "/OpenBankDepository/openBankDepositoryInit"
	payload = {}
	payload['url'] = web_url + '/OpenBankDepository/bankReturnBack'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
	# print (url)
	# print (payload)
	r = session.get (url, params=payload, headers=headers)
	# print(r.url)
	# print(r.text)
	data = r.json ()['data']
	# print (data)
	bankServiceUrl = data['bankServiceUrl']
	bank_request_vo = data['bankRequestVo']
	orig = bank_request_vo['orig']
	sign = bank_request_vo['sign']
	returnurl = bank_request_vo['returnurl']
	NOTIFYURL = bank_request_vo['NOTIFYURL']
	userType = bank_request_vo['userType']
	# f = open ('D:\\我的工作空间\\Flask_blog\\src\\r.html', 'w')
	filepath = os.path.join (basepath, '..\\templates\\')
	f = open (filepath + "r.html", 'w')
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
	bank_service_url = '''<form id="PayForm" name="PayForm"
      action=''' + bankServiceUrl + ''' autocomplete="off" method="post">'''
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

	f.write ('''    <input type="hidden" name= "NOTIFYURL" value="''' + NOTIFYURL + '''">''')
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


# 银行开户
def bank_account(card_num, mobile_number, local_ip):
	# driver = webdriver.Chrome ()
	driver = webdriver.Remote (command_executor=local_ip + ':4444/wd/hub',
							   desired_capabilities=DesiredCapabilities.CHROME)
	driver.maximize_window ()
	# path_dir = str (os.path.abspath (os.path.join (os.path.dirname (__file__), os.pardir)))
	# print(path_dir)
	# url = 'file://' + path_dir + '/src/r.html'
	url = 'http://10.200.1.59:81/r'
	# url = 'http://172.25.1.111/r'
	# print (url)
	driver.get (url)
	# 点击下一步
	driver.find_element_by_xpath ("//input[@type='submit']").click ()
	driver.find_element_by_id ('accountNo').send_keys (card_num)
	driver.find_element_by_id ('phone').send_keys (mobile_number)
	js1 = "$('#keyboards').val('xs111111');"
	driver.execute_script (js1)
	js2 = "$('#keyboards2').val('xs111111');"
	driver.execute_script (js2)
	driver.find_element_by_id ('isRead').click ()
	for j in range (10):
		driver.find_element_by_id ('checkCodeText').click ()
		# time.sleep(10)
		for i in range (10):
			time.sleep (3)
			checkCodeText = driver.find_element_by_id ('checkCodeText').get_attribute ('value')
			# print(checkCodeText)
			if len (checkCodeText) == 4:
				break

		driver.find_element_by_id ('queryButton').click ()
		# print (driver.find_element_by_id ('showError').text)
		time.sleep (1)
		# print(driver.find_element_by_id('msgId').text)
		if driver.find_element_by_id ('showError').text == u'请输入正确的图形验证码':
			# time.sleep(1)
			# driver.find_element_by_xpath("//a[text()='确定']").click()
			driver.find_element_by_id ('checkCodeText').clear ()
		else:
			break

	otp_code = '111111'

	driver.find_element_by_id ('mobilePwd').send_keys (otp_code)

	url = driver.current_url
	# https://my-st1.orangebank.com.cn/corporbank/netLoanIn.do
	# print (url)

	driver.find_element_by_id ('SubmitButton').click ()
	time.sleep (10)

	driver.close ()

# if __name__ == '__main__':
# 	print (getcwd)
# 	print(getabspath)
# 	list = ['test5', '13586693795']
# 	web_url = "http://" + list[0] + ".www.xs.sit/xweb"
# 	mobile = list[1]
# 	passwd = '96e79218965eb72c92a549dd5a330112'
# 	banknum = '6225888809585750'
# 	login_web (mobile_number=mobile, password=passwd, web_url=web_url)
# 	open_bank_depository (web_url=web_url)
# 	bank_account (card_num=banknum, mobile_number=mobile)
