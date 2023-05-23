import time
from selenium import webdriver
import yaml
import os

yaml_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"seleniumDemo/test.yml")
def read_yaml(n,k):
    # 打开文件
    with open(yaml_path,"r",encoding="utf-8") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        try:
            #判断传入的n是否在存在
            if n in data.keys():
                return data[n][k]
            else:
                print(f"n：{n}不存在")
        except Exception as e :
            print(f"key值{e}不存在")

# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
driver = webdriver.Chrome()

# 访问力扣管网
driver.get("https://leetcode.cn/")
# 右上角的登录按钮
driver.find_element("xpath",'//*[@id="lc-header"]/nav/div/div[2]/a[2]').click()
time.sleep(1)
# 账号密码登录
driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div/div/div[6]/div').click()
time.sleep(1)
# 输入用户名
driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div/div/div[3]/div/label/input').send_keys(read_yaml("leetcode","username"))
# 输入密码
driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div/div/div[4]/div/label/input').send_keys(read_yaml("leetcode","password"))
# 勾选用户协议
driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div/div/div[8]/div/span[1]/svg').click()
# 登录
driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div/div/button/span').click()


# time.sleep(6)
# # 退出浏览器
# driver.quit()