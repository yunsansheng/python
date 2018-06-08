#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




browser = webdriver.Chrome()
browser.get("http://172.16.98.194")



class Nielsenweb(object):
    
    def __init__(self,url,user,pwd):
        self.url = url
        self.user = user
        self.pwd = pwd

    def runweb(self):
        
    pass
