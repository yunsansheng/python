#coding:utf-8


from bs4 import BeautifulSoup
import re
import urllib.parse
import json
from urllib import request
import time
from Down_picture import Down_picture

class Req_again(object):
        def __init__(self,url):
                self._url = url
                self._statu = False
        def req_run(self):
                req=request.Request(self._url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')

                while self._statu ==False:
                        try:
                                html= request.urlopen(req)
                                if html.status == 200:
                                        print("its okay")
                                        self._statu = True
                        except:
                                print("加载失败,准备重新进入")
                return html
                


class Get_root_url(object):
        def __init__(self,url):
                self._url = url
                self._links=[]
                self._nolinks=["read.php?tid=5877","htm_data/8/1607/1971556.html","htm_data/8/1402/1163961.html","htm_data/8/1109/594739.html","htm_data/8/1106/524775.html","htm_data/8/0907/344500.html","htm_data/8/0706/36794.html"]
                
        def get_url(self):

                html = Req_again(self._url).req_run()

                Bsobj=BeautifulSoup(html,"html.parser")
                trs= Bsobj.find_all(class_="tr3 t_one tac")

                for tr in trs:
                            try:
                                    link=tr.find("td").find("a")["href"]
                                    if link not in self._nolinks and link[:4]!="read":
                                            self._links.append(link)
                                            print(link)

            
                            except:
                                pass
                return self._links
        
                
                
class Parse_url(object):
        def __init__(self,url):
                self._url = "http://xxx/"+url
                self._title=''
                self._imgurl=[]
                

        def get_img_url(self):

                html = Req_again(self._url).req_run()

                Bsobj=BeautifulSoup(html,"html.parser")
               
                self.title =Bsobj.find('h4').get_text()
                lst = Bsobj.find("div",class_="tpc_content do_not_catch").find_all("input")
                for i in lst:
                        #print(i["src"])
                        self._img_url.append(i["src"])
                return self._imgurl
        def get_title(self):
                return self._title
                        
                        
                


if __name__ =="__main__":
        root_urls=Get_root_url("http://xxx").get_url() #获取首页的列表合集.

        for root_url in root_urls:
                parse_url= Parse_url(root_url)
                imgurls =parse_url.get_img_url()
                title=parse_url.get_title()
                
                down_jpg=Down_picture(imgurls,title)
                down_jpg.down_pic()
        

        

