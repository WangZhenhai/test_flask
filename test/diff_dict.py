# encoding = utf-8

dict1 = {"a": 1, "b": 2, "c": 5}
dict2 = {"a": 1, "c": 5, "b": 2}

if dict1 == dict2:
	print ("Ture")
else:
	print ("False")

differ = set (dict1.items ()) ^ set (dict2.items ())
# print (differ)

print (dict1.keys () & dict2.keys ())  # 共有的keys
print (dict1.keys () ^ dict2.keys ())  # 不共有的keys
print (dict1.items () & dict2.items ())  # 相同的keys，values

diff = dict1.keys () & dict2

diff_vals = [(k, dict1[k], dict2[k]) for k in diff if dict1[k] != dict2[k]]

print (diff_vals)
