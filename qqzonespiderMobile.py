#!/usr/bin/python3
from selenium import webdriver

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
browser=webdriver.Chrome()
# 打开qq空间登录界面
browser.get('https://ui.ptlogin2.qq.com/cgi-bin/login?pt_hide_ad=1&style=9&pt_ttype=1&appid=549000929&pt_no_auth=1&pt_wxtest=1&daid=5&s_url=https%3A%2F%2Fh5.qzone.qq.com%2Fmqzone%2Findex')
# 全屏截取
print('11')
browser.maximize_window()
#time.sleep(2)
# 确定打开了登录页面，保存截图
#browser.save_screenshot('qq1.png')
# 切换至登录框架
#browser.switch_to.frame("login_frame")
# # 点击使用用户名和密码登录
#browser.find_element_by_id('switcher_plogin').click()
# # 获取登录名和密码输入框的id，使用id获取元素并在对应输入框内输入登录信息
browser.find_element_by_id('u').send_keys('1280041038')
browser.find_element_by_id('p').send_keys('password')
print('333')
# browser.save_screenshot('qq2.png')
# # 获取登录按钮的id，点击
browser.find_element_by_id('go').click()
time.sleep(5)
browser.switch_to_frame('tcaptcha_iframe')
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
# 直接点击头像登录
#browser.find_element_by_id('img_out_*********').click() # 此处*为qq密码
# 保存屏幕快照
#time.sleep(10)
browser.save_screenshot('qq3.png')


