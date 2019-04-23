# encoding=utf-8
from identity import *
import random as r
import sys
# 需要生成的数量
count = int(sys.argv[1])

a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '拓跋', '西门', '南宫', '公仪', '太史', '贺', '独孤', '陈', '魏']
a2 = ['玉', '明', '龙', '芳', '军', '玲', '珠', '翠', '雅', '芝', '玉', '萍', '红', '娥', '玲', '芬', '芳', '燕', '彩', '春', '菊', '兰', '凤',
	  '洁', '梅', '琳', '素', '云', '莲', '真', '环', '雪', '荣', '爱', '妹', '霞', '香']
a3 = ['立', '玲', '国', '', '伟', '刚', '勇', '毅', '俊', '峰', '强', '军', '平', '保', '东', '文', '辉', '力', '明', '永', '健', '世', '广',
	  '志', '义', '兴', '良', '海', '山']

# 手机号前三位
m1 = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157', '158', '159', '187', '188', '130', '131',
	  '132', '155', '156', '185', '186', '133', '153', '180', '189']
# 剩余手机号位数（随机取值）
m2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 身份证号组成
id1 = ['110101', '130626', '131122', '150524', '220622', '150925', '230707', '340223', '410404', '520425', '640202',
	   '632723']  # 地区省份
y = '19'
year = ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
		'68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85',
		'86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

id2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']  # 月份
id3 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
	   '20', '21', '22', '23', '24']  # 日期
id4 = ['1', '2', '3', '4', '5', '6']
id5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
id6 = ['1', '2', '3', '4']
id7 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']

# 银行信息
bank = '622588'
bank_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# 生成姓名
def random_name():
    name = r.choice (a1) + r.choice (a2) + r.choice (a3)
    return name


# 生成手机号
def random_mobile():
    mobile = r.choice (m1) + r.choice (m2) + r.choice (m2) + r.choice (m2) + r.choice (m2) + r.choice (m2) + r.choice (m2) + r.choice (m2) + r.choice (m2)
    return mobile


# 生成身份证号(废弃)
#def random_idcard():
#    idcard = r.choice (id1) + y + r.choice (year) + r.choice (id2) + r.choice (id3) + r.choice (id4) + r.choice (id5) + r.choice (id6) + r.choice (id7)
#    return idcard


def random_bankNum():
    bankNum = bank + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num) + r.choice (bank_num)
    return bankNum


if __name__ == "__main__":
    random_sex = r.randint (0, 1)
    for i in range (count):
        if int(sys.argv[3])==1:
            print (random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==2:
            print (random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," + random_bankNum () + "," +"招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==3:
            print (random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==4:
            print (random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
        if int(sys.argv[3])==5:
            print (random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB")
            with open(sys.argv[2],"a+") as f:
                f.write(random_name () + "," + random_mobile () + "," + (IdNumber.generate_id (random_sex)) + "," + random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," +random_bankNum () + "," + "招商银行|CMB\n")
                f.close()
