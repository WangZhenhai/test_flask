# encoding = utf-8

# !/usr/bin/env python3

def find_str_repeat(s):
	d = {}
	for i in range (len (s)):
		if d.get (s[i]):
			return s[i]
		else:
			d[s[i]] = i
	return False


def find_str_repeat1(s):
	list1 = []
	list2 = []
	for i in range (len (s)):
		list1.append (s[i])
	print (list1)

	for i in range (len (list1)):
		if list1[i] not in list2:
			list2.append (list1[i])
	print (list2)


if __name__ == "__main__":
	s = "qweweert22333aadd"
	print (find_str_repeat (s))
	find_str_repeat1 (s)
