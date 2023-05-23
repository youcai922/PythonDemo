import time
import common.fileUtil as fileUtil

def loginLeetcode(driver):
    driver.get("https://leetcode.cn/")
    time.sleep(1)
    # 右上角的登录按钮(力扣会自动弹出登录弹窗，所以这行注释了)
    # driver.find_element("xpath",'//*[@id="lc-header"]/nav/div/div[2]/a[2]').click()
    # 账号密码登录
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/div[6]/div').click()
    # 输入用户名
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/div[3]/div/label/input').send_keys(
        fileUtil.read_yaml("leetcode", "username"))
    # 输入密码
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/div[4]/div/label/input').send_keys(
        fileUtil.read_yaml("leetcode", "password"))
    # 勾选用户协议
    driver.find_element("css selector",
                        'body > div.modal-container.css-1w5zeo3-RootContainer.e117yaqi0 > div > div > div.css-mbfawm-Container.eyzdego1 > div > div > div.css-spjj8d-Container.e1end7df0 > div > span.css-4a562t-BaseCheckbox-w16.e18ulegg0 > svg').click()
    time.sleep(3)
    # 登录
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/button/span').click()