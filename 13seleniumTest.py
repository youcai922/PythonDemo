from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    username = 13026373922
    password = "2287360627yucan"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    url = 'https://detail.damai.cn/item.htm?id=764640990021'

    chrome_driver_path = 'F:\software\chromedriver_win32\chromedriver.exe'
    s = Service(chrome_driver_path)

    # 创建ChromeOptions对象来设置浏览器选项
    options = webdriver.ChromeOptions()
    # 例如，设置无头模式（不显示浏览器界面）
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")  # 禁用GPU加速
    options.add_argument("--no-sandbox")  # 禁用沙箱模式（在Linux上需要）
    options.add_argument("--disable-dev-shm-usage")  # 禁用/dev/shm内存使用（在Linux上需要）
    options.add_argument("--disable-extensions")  # 禁用扩展
    options.add_argument("--disable-blink-features=AutomationControlled")  # 隐藏自动化控制标志
    # 设置用户代理为移动设备的用户代理
    mobile_user_agent = 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QQ2A.200305.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'
    options.add_argument(f'user-agent={mobile_user_agent}')

    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 禁用图片加载
    # No_Image_loading = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", No_Image_loading)
    # 创建Chrome浏览器实例，传入Service和ChromeOptions
    driver = webdriver.Chrome(service=s, options=options)

    # 演出详情页
    driver.get(url)

    sleep(100)
    #
    # login_btn = driver.find_element(By.CLASS_NAME, "login-user")
    # login_btn.click()
    # # 登陆页面
    # driver.switch_to.frame('alibaba-login-box')
    # username_input = driver.find_element(By.ID, "fm-login-id")
    # username_input.send_keys(username)
    # password_input = driver.find_element(By.ID, "fm-login-password")
    # password_input.send_keys(password)
    # driver.find_element(By.CLASS_NAME, "fm-btn").click()
    # sleep(4)
    # # 演出详情页，驱动切换作用域
    # driver.switch_to.default_content()
    # driver.find_element(By.CLASS_NAME, 'cafe-c-input-number-handler-up').click()
    # driver.find_element(By.CLASS_NAME, "buy-link").click()
    # sleep(1)
    # driver.execute_script("window.scrollTo(0, 70);")
    # driver.find_element(By.XPATH, '//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div[1]/div[2]/i').click()
    # driver.find_element(By.XPATH, '//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div[2]/div[2]/i').click()
    # driver.find_element(By.XPATH, '//*[@id="dmOrderSubmitBlock_DmOrderSubmitBlock"]/div[2]/div/div[2]/div[2]/div[2]') \
    #     # .click()
    # sleep(3)
    driver.quit()
