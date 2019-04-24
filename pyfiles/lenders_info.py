# -*-coding:utf-8-*-

import os
import requests
from bs4 import BeautifulSoup

getcwd = os.getcwd()
def generate_lenders_info():
	url = "http://10.200.0.72:11987/generateData/generateRandomPeopleInfo"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"}
	r = requests.get (url, headers=headers)
	print(r.text)
	return r.text


def html_parser(r_text):
	html_doc = r_text
	soup = BeautifulSoup (html_doc, 'html.parser')
	td_list = soup.find_all ('td')
	f = open (getcwd + '\\uploads\\lender_msg.txt', 'w', encoding='utf8')
	for i in range (len (td_list)):
		if str (i)[-1] == '1' or str (i)[-1] == '5' or str (i)[-1] == '6':
			f.write (td_list[i].get_text () + ',')
		elif str (i)[-1] == '7':
			f.write (td_list[i].get_text () + '\n')
	f = open ('../uploads/lender_msg.txt', 'r', encoding='utf8')
	lines = f.readlines ()
	for line in lines:
		print (line)
	f.close()

html_parser (generate_lenders_info ())
