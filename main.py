import time
from selenium import webdriver

import common.fileUtil as fileUtil
import task.leetcodeTask as leetcodeTask
import task.JDTask as JDTask

# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
driver = webdriver.Chrome()
if fileUtil.read_yaml("leetcode", "execute"):
    leetcodeTask.loginLeetcode(driver)

mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)


if fileUtil.read_yaml("JD","execute"):
    JDTask.JDLogin(driver)

time.sleep(100)
# # 退出浏览器
# driver.quit()