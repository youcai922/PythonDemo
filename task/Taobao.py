import time
def TaobaoLogin(driver):
    driver.get('https://main.m.taobao.com/')
    driver.find_element("xpath", '/html/body/div[1]/div/div/div[6]/span[3]').click()
    time.sleep(6)
    # driver.find_element("css selector", '#login-form > div.login-blocks.login-links > a').click()
    # driver.find_element("xpath", '//*[@id="login-form"]/div[6]/div/label').click()

