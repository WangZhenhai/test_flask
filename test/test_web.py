# encoding = utf-8
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote (command_executor='10.200.1.65:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
# path_dir = str (os.path.abspath (os.path.join (os.path.dirname (__file__), os.pardir)))
# url = 'file://' + path_dir + '/src/r.html'
driver.get ("https://www.baidu.com")
# driver.get (url)
execcutor_url = driver.command_executor._url

seesion_id = driver.session_id

print (execcutor_url)
print (seesion_id)
