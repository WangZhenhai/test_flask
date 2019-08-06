# encoding=utf-8
# 比较两个字典函数是否一致
import json
import operator


def get_cmp_dict(src_dict, dst_dict):
	if isinstance (src_dict, str):
		src_dict = json.dumps (src_dict)
	if isinstance (dst_dict, str):
		dst_dict = json.dumps (dst_dict)
	if len (src_dict) != len (dst_dict):
		return False
	else:
		src_keys = list (src_dict.keys ())
		dst_keys = list (dst_dict.keys ())
		if operator.eq (src_keys, dst_keys):
			src_value = list (src_dict.values ())
			dst_value = list (dst_dict.values ())
			if operator.eq (src_value, dst_value):
				for key in src_dict.keys ():
					if src_dict[key] != dst_dict[key]:
						return False
				return True
			else:
				return False
		else:
			return False


if __name__ == '__main__':
	dict1 = {"a": 1, "b": 2, "c": 5}
	dict2 = {"a": 1, "b": 2, "c": 5}
	print (get_cmp_dict (dict1, dict2))
