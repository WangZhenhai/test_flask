# encoding = utf-8
import os
import platform

print ("run test script for python")
getcwd = os.getcwd ()

if platform.system () == "Windows":
	slash = '\\'
else:
	platform.system () == "Linux"
	slash = '/'

with open (getcwd + slash + 'pyweb.txt', 'r', encoding='utf8') as rf:
	str = rf.read ()
	# print (str.splitlines ())
	print (str)
