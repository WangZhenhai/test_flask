# encoding=utf-8
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

local_ip = '10.200.1.59'

driver = webdriver.Remote (command_executor=local_ip + ':4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

# driver.get ('https://my-st1.orangebank.com.cn/corporbank/netLoanIn.do')

# 获取cookie全部内容
cookie = driver.get_cookies ()

driver.delete_all_cookies ()
# 打印全部cookile信息
print (cookie)
# 打印cookie第一组信息
print (cookie[0])

driver.delete_all_cookies ()
