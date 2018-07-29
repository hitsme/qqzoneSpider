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
# 启动phantomjs无界面浏览器
browser=webdriver.PhantomJS()
# 打开qq空间登录界面
browser.get('https://ui.ptlogin2.qq.com/cgi-bin/login?pt_hide_ad=1&style=9&pt_ttype=1&appid=549000929&pt_no_auth=1&pt_wxtest=1&daid=5&s_url=https%3A%2F%2Fh5.qzone.qq.com%2Fmqzone%2Findex')
# 全屏截取
browser.maximize_window()
time.sleep(2)
# 确定打开了登录页面，保存截图
browser.save_screenshot('qq1.png')
# 切换至登录框架
#browser.switch_to.frame("login_frame")
# # 点击使用用户名和密码登录
#browser.find_element_by_id('switcher_plogin').click()
# # 获取登录名和密码输入框的id，使用id获取元素并在对应输入框内输入登录信息
browser.find_element_by_id('u').send_keys('1334347212')
browser.find_element_by_id('p').send_keys('bingo2146295901')
# browser.save_screenshot('qq2.png')
# # 获取登录按钮的id，点击
browser.find_element_by_id('go').click()
# 直接点击头像登录
#browser.find_element_by_id('img_out_*********').click() # 此处*为qq密码
# 保存屏幕快照
time.sleep(10)
browser.save_screenshot('qq3.png')


