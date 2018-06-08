#coding:utf-8


import os
import base64
import json
import requests
from selenium import webdriver
import re
import time
import shutil



browser = webdriver.Chrome()

#运行前删除遗留文件
if os.path.exists("screenshot/temp.png") ==True:
    os.remove("screenshot/temp.png")
    





def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=VGO4WqFYSx9FI9P67a0sRe0e&client_secret=E7mByWWaa8iGbiYCjesETu5UMLrQvfPN'
    headers ={"Content-Type":"application/json; charset=UTF-8"}
    r=requests.get(host,headers=headers)
    json_str=json.loads(r.text)
    #print(json_str)
    return json_str["access_token"]


#get token and creat the url
access_token =get_token()
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token

        

def do():
    if os.path.exists("screenshot/temp.png")==False:
        os.popen("getimg.bat")
        time.sleep(1)
    else:
        try:
            
            access_token =get_token()
            f = open(r'screenshot/temp.png', 'rb')
            img = base64.b64encode(f.read())
            f.close()
            params = {"image": img}
            headers ={"Content-Type":"application/x-www-form-urlencoded"}
            r=requests.post(url,data=params,headers=headers)
            json_str=json.loads(r.text)
            #print(json_str)
            str1=""
            for i in range(json_str["words_result_num"]):
                str1=str1+json_str["words_result"][i]["words"]

            m = re.match(r'^\d{1,2}\.?(.*)',str1)
            question=m.group(1)
            print(question)
            browser.get('https://www.baidu.com/s?wd='+question)
            shutil.move("screenshot/temp.png", 'screenshot/backup/'+str(time.time())+'.png')
            time.sleep(10)
        except Exception as e:
            print("0_Fial"+str(e))
            time.sleep(1)
            shutil.move("screenshot/temp.png", 'screenshot/erro/'+str(time.time())+'.png')

        

#Do it !

while True:
    try:
        do()
    except Exception as e:
        print("Fail"+str(e))

        




























    







