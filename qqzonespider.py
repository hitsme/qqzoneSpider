#!/usr/bin/python3
from selenium import webdriver
import  json
#driver = webdriver.PhantomJS()
#driver.get('http://www.baidu.com')  # 加载网页
#data = driver.page_source  # 获取网页文本
#driver.save_screenshot('1.png')  # 截图保存
#print(data)
#driver.quit()
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
# 启动phantomjs无界面浏览器
#browser=webdriver.PhantomJS()
browser=webdriver.Chrome()
# 打开qq空间登录界面
browser.get('https://qzone.qq.com/')
# 全屏截取
browser.maximize_window()
time.sleep(2)
# 确定打开了登录页面，保存截图
browser.save_screenshot('qq1.png')
# 切换至登录框架
browser.switch_to.frame("login_frame")
# # 点击使用用户名和密码登录
browser.find_element_by_id('switcher_plogin').click()
# # 获取登录名和密码输入框的id，使用id获取元素并在对应输入框内输入登录信息
browser.find_element_by_id('u').send_keys('1009330792')
browser.find_element_by_id('p').send_keys('bingo8496982587')
# browser.save_screenshot('qq2.png')
# # 获取登录按钮的id，点击
time.sleep(1)
browser.find_element_by_id('login_button').click()
time.sleep(5)
browser.switch_to_frame(0)
action=ActionChains(browser)
slidepic=browser.find_element_by_id('tcaptcha_drag_button')
#print(slidepic)
xylocation=browser.find_element_by_id('tcaptcha_drag_button').location
print("x="+str(xylocation['x'])+"  y="+str(xylocation['y']))
action.click_and_hold(slidepic).perform()
action.move_to_element_with_offset(slidepic, 50, 0).perform()
time.sleep(0.5)
action.move_to_element_with_offset(slidepic, 60, 0).perform()
time.sleep(0.8)
action.move_to_element_with_offset(slidepic, 74, 0).release().perform()
browser.save_screenshot('test.png')
#action.release().perform()
#action.move_to_element_with_offset(slidepic, 200, 0)
#action.release().perform()
#action.move_to_element_with_offset(slidepic, 200, 0)
#action.release().perform()
#action.move_to_element_with_offset(slidepic, 480, 0).perform()
time.sleep(5)
#action.release().perform()
print('333')
time.sleep(1)
# 直接点击头像登录
#browser.find_element_by_id('img_out_*********').click() # 此处*为qq密码
# 保存屏幕快照
time.sleep(5)
browser.save_screenshot('qq3.png')
#cookies = browser.get_cookies()
#with open("cookies.txt", "w") as fp:
    #json.dump(cookies, fp)
def read_cookies(driver):
    # 设置cookies前必须访问一次百度的页面
    driver.get("https://qzone.qq.com/")
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            print(cookie['name'])
            #driver.add_cookie(cookie)
            # cookie.pop('domain')  # 如果报domain无效的错误
            driver.add_cookie({
        #'domain': '.xxxx.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
       'path': '/',
       'expires': None
    })
    driver.get('https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F1334347212')
    return driver
#read_cookies(browser)
