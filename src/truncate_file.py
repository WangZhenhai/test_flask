# encoding = utf -8
# 测试清空文件内容
import os

basepath = os.path.dirname (__file__)


def truncate_openbank():
	filepath = os.path.join (basepath, '..\\templates\\')
	f = open (filepath + "openbank.html", 'r+')
	f.truncate ()


def truncate_buy():
	filepath = os.path.join (basepath, '..\\templates\\')
	f = open (filepath + "buy.html", 'r+')
	f.truncate ()
