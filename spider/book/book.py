#coding:utf-8
#encoding:utf-8
#http://m.biqiuge.com/book_9952/7136661_2.html

#id  chaptercontent
#http://m.biqiuge.com/book_9952/7136662_2.html
#id pb_next

import requests
import time
from bs4 import BeautifulSoup
import re

#第1168章 灵乳 (第2/2页)
def is_ignore(s):
    matchobj= re.match('\r\n\t.*(\(第2/\d页\))',s)
    matchtitle =re.match('\r\n\t.*(第\d+章).*',s)
    if matchobj:
        return 'vice'
    elif matchtitle:
        return 'title'
    else:
        return 'normal'


current_url ="/book_9952/17185951.html"


f = open("dykf2.txt", 'a', encoding="utf-8")

while current_url !="/book_9952/24809863.html":
    print(current_url)

    try:
        time.sleep(1)
        url ="http://m.biqiuge.com%s" %current_url
        html=requests.get(url)
        Bsobj=BeautifulSoup(html.text,"html.parser")
        content =Bsobj.find(id="chaptercontent")
        nexturl= Bsobj.find(id="pb_next").get("href")
        #print("当前是%s" %url)
        current_url=nexturl

        for i in list(content.children)[:-5]:
            if str(i)=="<br/>":
                f.write("\n")
            elif is_ignore(i) =='vice':
                pass
            elif is_ignore(i)=='title':
                f.write('\n\n\n'+i+'\n\n\n')
            else:
                f.write(i)

    except Exception as e:
        print("运行错误%s"%url)
        print(e)



f.close()
