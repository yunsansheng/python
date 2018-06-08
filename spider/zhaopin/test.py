#coding:utf-8


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.parse
import json
import time
import csv

with open("lagou.csv","w",newline="") as datacsv:
    csvwriter = csv.writer(datacsv,dialect = ("excel"))
    csvwriter.writerow(["公司","职位","薪资","职位类型","发布时间","经验","教育","区块","地址","行业","公司规模","融资","职位备注","福利"])
    #csvwriter.writerows(result_lst)

def write_csv(lst):
    with open("lagou.csv","a+",newline="") as datacsv:
        csvwriter = csv.writer(datacsv,dialect = ("excel"))
        csvwriter.writerows(lst)


def explain(page):
    try:
        print("begin...")
        Bsobj=BeautifulSoup(urlopen(url.format(page=page)),"html.parser")
        lst=json.loads(str(Bsobj))
        if lst["success"]==True:
            
            try:
                result=lst["content"]["positionResult"]["result"]
                
                result_lst=[] 
                for i in result:
                    addlst=[]
                    addlst.append(i["companyFullName"])
                    addlst.append(i["positionName"])
                    addlst.append(i["salary"])
                    addlst.append(i["jobNature"])
                    addlst.append(i["formatCreateTime"])
                    addlst.append(i["workYear"])
                    addlst.append(i["education"])
                    addlst.append(i["businessZones"])
                    addlst.append(i["district"])
                    addlst.append(i["industryField"])
                    addlst.append(i["companySize"])
                    addlst.append(i["financeStage"])
                    addlst.append(','.join(i["positionLables"]))
                    addlst.append(i["positionAdvantage"])
                    print(addlst)
                    result_lst.append(addlst)

                #put into csv file...
                print("ready to put into scv")    
                write_csv(result_lst)
                print("add to scv successed")
                
            except:
                print("page %s failed" %page)
        else:
            print("get the url failed")
                
    except:
        print("strart failed")


#=====main==================

url="https://www.lagou.com/jobs/positionAjax.json?city=%E6%97%A0%E9%94%A1&needAddtionalResult=false&pn={page}"

page=1
while page<20:
    explain(page)
    page=page+1
    print("wait 15 second...")
    time.sleep(15)




            

# for i in result:
#     i["companyFullName"]  公司
#     i["positionName"]     职位
#     i["salary"]           薪资
    
#     i["jobNature"]        全职\兼职 
#     --------------------------------i["createTime"]       发布时间
#     i["formatCreateTime"] 格式化发布时间


#     公司要求

#     i["workYear"]  经验
#     i["education"]  教育
#     i["businessZones"] 区块
#     i["district"]      地址 

#     公司行业规模
#     i['industryField'] 行业
#     i["companySize"]
#     i["financeStage"]

#     其他说明
#     ','.join(i["positionLables"])
#      i["positionAdvantage"]





