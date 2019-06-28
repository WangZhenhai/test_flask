# encoding=utf-8
import requests

#解密
def decrypts(encrypts):
	url = "http://10.200.0.108:18090/decrypt/decrypts"
	headers = {"Content-Type": "application/x-www-form-urlencoded",
			   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
	payload = {}
	payload['encryptDataList'] = encrypts
	# print(payload)
	r = requests.post (url, data=payload, headers=headers)
	# print(r.text)
	d = r.json ()['data'][0]
	return d[payload['encryptDataList']]


# if __name__ == '__main__':
# 	mobile = decrypts ('a178d08ekQXDbh3JKR2vCTBvQr1x/Q==')
# 	print (mobile)
