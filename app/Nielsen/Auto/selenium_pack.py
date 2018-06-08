# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys                   #调用键盘事件类
from selenium.webdriver.common.action_chains import ActionChains  #调用鼠标事件类
from selenium.webdriver.common.by import By                       #调用元素等待
from selenium.webdriver.support.ui import WebDriverWait           #调用元素等待
from selenium.webdriver.support import expected_conditions as EC  #调用元素等待
import time
#import SendKeys
import sys

class Selepack(object):
    
    def __init__(self):
        self.browser = webdriver.Chrome()
    '''
        
    def run_browser(self):                    #启动浏览器
        self.browser = webdriver.Chrome()
    '''

    def connect(self, link):                  #进入指定的链接
        self.browser.get(link)

    def set_window_size(self,window_size):    #设置浏览器窗口大小
        self.browser.set_window_size(window_size)

    def back(self):                           #后退一步
        self.browser.back()
        time.sleep(3)
 
    def forword(self):                        #前进一步
        self.browser.forward()
        time.sleep(3)

    def refresh(self):                        #刷新页面
        self.browser.refresh()
        time.sleep(3)
 
    def quit(self):                           #退出
        self.browser.quit()
        
    def name_input(self, name, content):      #以name元素的输入
        self.browser.find_element_by_name(name).clear()
        self.browser.find_element_by_name(name).send_keys(content)
        time.sleep(2)
        
    def xpath_click(self, xpath):             #点击以xpath元素的按钮
        self.browser.find_element_by_xpath(xpath).click()
        time.sleep(3)

    def class_click(self, classname):         #点击以class元素的按钮
        self.browser.find_element_by_class_name(classname).click()
        time.sleep(3)

    def linktext_click(self, linktext):       #点击文本链接
        self.browser.find_element_by_link_text(linktext)

    def xpath_input(self, xpath, content):    #以xpath元素的输入
        #self.browser.find_element_by_xpath(xpath).clear()
        self.browser.find_element_by_xpath(xpath).send_keys(content)
        #time.sleep(3)

    def class_input(self, classname,content): #以class元素的输入
        self.browser.find_element_by_class_name(classname).clear()
        self.browser.find_element_by_class_name(classname).send_keys(content)
        time.sleep(3)

    def print_title(self):                    #打印当前页的title
        title=self.browser.title
        print(title)

    def print_nowurl(self):                   #获取当前页面的url
        nowurl=self.browser.current_url
        print(nowurl)
        return nowurl

    def xpath_text(self, xpath):              #获取元素的文本
        content=self.browser.find_element_by_xpath(xpath).text
        print(content)

    def xpath_size(self, xpath):              #返回元素的尺寸
        text = self.browser.find_element_by_xpath(xpath).size
        print(text)

    def xpath_displayed(self, xpath):         #返回元素的结果是否可见，True/False
        displayed = self.browser.find_element_by_xpath(xpath).is_displayed()
        print(displayed)

    def xpath_attribute(self, xpath):         #返回元素的属性
        attribute = self.browser.find_element_by_xpath(xpath).get_attribute('type')
        print(attribute)
        return attribute

    def xpath_right_click(self, xpath):       #鼠标右击
        right_click = self.browser.find_element_by_xpath(path)
        ActionChains(self.browser).context_click(right_click).perform()

    def xpath_xuanting(self, xpath):          #鼠标悬停
        xuanting = self.browser.find_element_by_xpath(xpath)
        ActionChains(self.browser).move_to_element(xuanting).perform()
        time.sleep(3)

    def xpath_double_click(self, xpath):      #鼠标双击
        double_click = self.browser.find_element_by_xpath(path)
        ActionChains(self.browser).double_click(double_click).perform()

    def drag_and_drop(self, xpath1, xpath2):  #鼠标拖拽
        location1 = self.browser.find_element_by_xpath(xpath1)
        location2 = self.browser.find_element_by_xpath(xpath2)
        ActionChains(self.browser).drag_and_drop_(location1,Location2).perform()

    def xpath_keyboard(self, xpath, keyboard):
        self.browser.find_element_by_xpath(xpath).send_keys(keyboard)

    def element_wait(self,xpath):
        element_wait = WebDriverWait(self.browser, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        
    def all_input(self,tagname,content):
        inputs = self.browser.find_elements_by_tag_name(tagname)
        for i in inputs:
            if i.get_attribute("type") == "text":
                #i.clear()
                i.send_keys(content)
             
    def checkbox(self,tagname):                    #定位一组元素，以页面所有checkbox勾选为例
        inputs = self.browser.find_elements_by_tag_name(tagname)
        for i in inputs:
            if i.get_attribute("type") == "checkbox":
                i.click()        
 
    def save_screenshot(self,path):
        self.browser.save_screenshot(path)
        
    def find_id(self, ID):
        self.browser.find_element_by_id(ID)
    def find_name(self, name):
        self.browser.find_element_by_name(name)
    def find_class_name(self, classname):
        self.browser.find_element_by_class_name(classname)
    def find_tag_name(self, tagname):
        self.browser.find_element_by_tag_name(tagname)
    def find_xpath(self, xpath):
        self.browser.find_element_by_xpath(xpath)
    def find_css(self, css):
        self.browser.find_element_by_css_selector(css)
    def find_link_text(self,linktext):
        self.browser.find_element_by_link_text(linktext)

    """    
    def checkbox(self):                    #定位一组元素，以页面所有checkbox勾选为例..
        inputs = self.browser.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[5]")
        for i in inputs:
            if i.get_attribute("type") == "checkbox":
                i.click()
    """       
if __name__ ==  "__main__":
	pass
    
