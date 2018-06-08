#coding:utf-8


from bs4 import BeautifulSoup
import re
import urllib.parse
import json
from urllib import request
import time


class Get_root_url(object):
        def __init__(self,url):
                self._url = url
                self._statu = False
                self._links=[]
                self._nolinks=["read.php?tid=5877","htm_data/8/1607/1971556.html","htm_data/8/1402/1163961.html","htm_data/8/1109/594739.html","htm_data/8/1106/524775.html","htm_data/8/0907/344500.html","htm_data/8/0706/36794.html"]
                
        def get_url(self):
                req=request.Request(self._url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
                
                while self._statu == False:
                        try:
                                html = request.urlopen(req)
                                if html.status == 200:
                                        print("its okay")
                                        self._statu =True
                        except:
                                print("加载失败，准备重新进入")
                                time.sleep(1)

                Bsobj=BeautifulSoup(html,"html.parser")
                trs= Bsobj.find_all(class_="tr3 t_one tac")

                for tr in trs:
                	    try:
                            link=tr.find("td").find("a")["href"]
                            if link not in self._nolinks:
                            	self._links.append(link)
                            	print(link)

            
                        except:
                    	    pass
                        
                


if __name__ =="__main__":
        root_url=Get_root_url("http://dz.zh4.co/thread0806.php?fid=8")
        root_url.get_url()


