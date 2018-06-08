# -*- coding: utf-8 -*-
from selenium_pack import Selepack
import time




class Nielsen_auto(object):
    def __init__(self,url):
        self.url = url
        self.browser=Selepack()
        
    def log(func):
        def wrapper(*args,**kw):
            print("\n")
            print(func.__doc__)
            return func(*args,**kw)
        return wrapper

    def login(self,user,pwd):
        self.browser.connect(self.url)    
        self.browser.xpath_input('//*[@id="userName"]',user)
        self.browser.xpath_input('//*[@id="password"]',pwd)
        time.sleep(2)
        self.browser.xpath_click('//*[@id="root"]/div/div[1]/div[2]/div/form/div/div[2]/div/div/span/button')

    def run_login_test(self,user):
        #不同密码登录
        pwddata=["","22332211","&@!","123456"] #空的密码，错误密码，特殊字符，正确密码
        for i in pwddata:
            self.login(user,i)
        
        #退出再登录
        for t in range(2):#运行2次
            self.browser.xpath_click('//*[@id="root"]/div/div/div[1]/div/div[2]/p')
            self.login(user,i)
            
        #关闭浏览器
        self.browser.quit()
        print("登录测试完毕")

    def run_main(self,user,pwd,module):
        self.login(user,pwd)
        time.sleep(2)
        
        for i in module:
            if i ==1:
                self.run_grid()
            elif i == 2:
                self.run_cbd()
            elif i == 3:
                self.run_store()
            else:
                print("%s菜单不存在"%i)


    #====###########方法区域###################
    @log            
    def grid_filter_city(self):
        '检查栅格期数和省市区'
  
                
    #====###########方法区域###################
            
    def run_grid(self):
        print("运行栅格分析")
        self.browser.xpath_click("//a[@href='/grid/cover']")
        self.browser.xpath_click("//a[@href='/grid/map']")
        self.grid_filter_city()



    def run_cbd(self):
        print("运行商圈分析")
        self.browser.xpath_click("//a[@href='/business-cluster/cover']")
        self.browser.xpath_click("//a[@href='/business-cluster/map']")
        


    def run_store(self):
        print("运行门店分析")
        self.browser.xpath_click("//a[@href='/store/cover']")
        self.browser.xpath_click("//a[@href='/store/map']")

        
        
        
if __name__ ==  "__main__":
    autoweb = Nielsen_auto("http://172.16.98.194")
    ##==============##test login
    #autoweb.run_login_test("admin")

    ##==============##test main
    autoweb.login("admin","123456")

    #autoweb.run_main("admin","123456",[1])#按照顺序运行数组中的菜单，1栅格，2商圈，3门店
    




