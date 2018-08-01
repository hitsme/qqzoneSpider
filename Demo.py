from selenium import webdriver
from selenium.webdriver.common.by import By
from pillow import Image, ImageEnhance
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import cv2
import numpy as np
from io import BytesIO
import time, requests

class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """
    def __init__(self):
        super(CrackSlider, self).__init__()
        # 实际地址
        self.url = 'http://3g.163.com/wap/special/newsapp_idol_personal/?starId=14#/home'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.zoom = 2

    def open(self):
        self.driver.get(self.url)

    def get_pic(self):
        time.sleep(2)
        target = browser.find_element_by_class_name("yidun_bg-img")
        template = browser.find_element_by_class_name("yidun_jigsaw")
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 320 / int(size_loc[0])

    def get_tracks(self, distance):
        print(distance)
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3/5
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t**2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3,-3,-2,-2,-2,-2,-2,-1,-1,-1]
        return {'forward_tracks':forward_tracks,'back_tracks':back_tracks}

    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template,0)
        run = 1
        w, h = template.shape[::-1]
        print(w, h)
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            if threshold < 0:
                print('Error')
                return None
            loc = np.where( res >= threshold)
            #print(len(loc[1]))
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2

        return loc[1][0]

    def crack_slider(self,browser):
        #self.open()
        target = 'target.jpg'
        template = 'template.png'
        self.get_pic()
        distance = self.match(target, template)
        zoo = 1.36 #缩放系数，需要自己调整大小
        tracks = self.get_tracks((distance + 7 )*zoo) # 对位移的缩放计算
        #print(tracks)
        slider = browser.find_element_by_class_name("yidun_slider")
        ActionChains(browser).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.5)
        for back_tracks in tracks['back_tracks']:
            ActionChains(browser).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        ActionChains(browser).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(browser).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(browser).release().perform()
        try:
            failure = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_tips__text'), '向右滑动滑块填充拼图'))
            print(failure)
        except:
            print('验证成功')
            return None

        if failure:
            self.crack_slider(browser)

#if __name__ == '__main__':
browser = webdriver.Chrome()

username="11111111"  #填自己的用户名
passwd="1111111" #填用户名对应的密码
browser = webdriver.Chrome()
# 打开的是QQ登录界面，可以自己改
browser.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=716027609&pt_3rd_aid=100374397&daid=383&pt_skey_valid=0&style=35&s_url=http%3A%2F%2Fconnect.qq.com&refer_cgi=authorize&which=&client_id=100374397&redirect_uri=https%3A%2F%2Freg.163.com%2FouterLogin%2Foauth2%2Ftencent_connect.do%3Furl%3Dhttp%253A%252F%252F3g.163.com%252Fwap%252Fspecial%252Fnewsapp_idol_personal%252F%253FstarId%253D14%26url2%3Dhttp%253A%252F%252F3g.163.com%252Ftouch%252Flogin%252F%253Furl%253Dhttp%253A%252F%252F3g.163.com%252Fwap%252Fspecial%252Fnewsapp_idol_personal%252F%253FstarId%253D14%2523%252Fhome%2526fail%26product%3D3g_163%26domains%3D163.com%26display%3Dmobile%26urs_tg%3D1&response_type=code&state=f8ccbd6b5d42d1a87da1a9f33d1920b7&scope=get_user_info&display=mobile')
browser.implicitly_wait(10)
# 需要自己按F12查原网址对应的用户名和密码框的id_name
elem=browser.find_element_by_id("u")
elem.send_keys(username)
elem=browser.find_element_by_id("p")
elem.send_keys(passwd)
elem=browser.find_element_by_id("go")
elem.click()

browser.implicitly_wait(10)
browser.switch_to_window(browser.window_handles[-1])
c = CrackSlider()
k = 1
for i in range(1,70000):
    try:
        elem=browser.find_element_by_class_name("idol_vote_info")
        elem.click()
        time.sleep(0.2)
        # 设置点击50次刷新一次
        if k%50 == 0:
            browser.refresh()   # 刷新方法 refresh
            print ('test pass: refresh successful')
        # 点击110次休眠50s，可以自己设置
        if k%110 == 0:
            print ("click",k)
            time.sleep(50)
        k += 1
    except:
        print('-----需要验证-----')
        c.crack_slider(browser)