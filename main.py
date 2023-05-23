import time
from selenium import webdriver

import common.fileUtil as FileUtil
import task.LeetcodeTask as LeetcodeTask
import task.JDTask as JDTask
import task.Taobao as Taobao

# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
driver = webdriver.Chrome()
#cdp破解反爬虫
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
　　    Object.defineProperty(navigator, 'webdriver', {
　　      get: () => undefined
　　    })
　　  """
})

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")

if FileUtil.read_yaml("leetcode", "execute"):
    LeetcodeTask.loginLeetcode(driver)

mobileEmulation = {'deviceName': 'iPhone X'}
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_experimental_option('excludeSwitches',['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
　　    Object.defineProperty(navigator, 'webdriver', {
　　      get: () => undefined
　　    })
　　  """
})
#
#
# if FileUtil.read_yaml("JD","execute"):
#     JDTask.JDLogin(driver)
#
if FileUtil.read_yaml("Taobao", "execute"):
    Taobao.TaobaoLogin(driver)

time.sleep(100)
# # 退出浏览器
# driver.quit()
