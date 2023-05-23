
def TaobaoLogin(driver):
    driver.get('https://main.m.taobao.com/')
    driver.find_element("id", 'SLK_manualPopCancel').click()

