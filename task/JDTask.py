import common.fileUtil as fileUtil
def JDLogin(driver):
    driver.get('https://m.jd.com/')
    driver.find_element("id", 'msShortcutLogin').click()
    driver.find_element("xpath", '//*[@id="app"]/div/p[1]/span[1]').click()
    # 输入用户名
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/div[3]/div/label/input').send_keys(
        fileUtil.read_yaml("JD", "username"))
    # 输入密码
    driver.find_element("xpath", '/html/body/div[3]/div/div/div[1]/div/div/div[4]/div/label/input').send_keys(
        fileUtil.read_yaml("JD", "password"))
