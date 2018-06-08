#coding:utf-8


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.parse
import json
import time


html=urlopen("http://www.piaohua.com/")
Bsobj=BeautifulSoup(html,"html.parser")

ul= Bsobj.find(id="iml1").ul
#print(type(lst))


#电影名称
#网址
#更新日期
#进入网址爬取豆瓣评分



def getscore(url):#从对应网址中获取到豆瓣评分
    inner_html=urlopen(url)
    inner_obj=BeautifulSoup(inner_html,"html.parser")
    
    try:
        t=str(inner_obj.find(string=re.compile("豆瓣评分"))).strip()
    except:
        t=""
        
    return t

    
#从豆瓣中获取评分
def douban_score(name):
    outname= urllib.parse.quote(name)
    api_url="https://api.douban.com/v2/movie/search?q={"+outname+"}"
    api_html=urlopen(api_url)
    
    data=api_html.read().decode()
    api_json =json.loads(data)
  
    try:
        api_mv_name=api_json["subjects"][0]["title"]
        api_mv_score=api_json["subjects"][0]["rating"]["average"]
        api_mv_year=api_json["subjects"][0]["year"]
        content="名称："+str(api_mv_name)+" 评分："+str(api_mv_score)+" 年份："+str(api_mv_year)
    except:
        content="爬取失败"
      
    return content

    
    
    
    
for li in ul.find_all("li"):
    mov_name=li.a.find_next_sibling("a").strong.font.font.get_text()
    mov_url="http://www.piaohua.com"+str(li.a.find_next_sibling("a").get('href'))
    mov_date=li.a.find_next_sibling("span").get_text()
    mov_score=getscore(mov_url)
    print(mov_name)
    print(mov_date)
    #print(mov_score)
    print(mov_url)
    print("===========豆瓣电影搜索结果===========")
    print(douban_score(mov_name))
    print("\n")
    time.sleep(2)




    
    
