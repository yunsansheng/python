#coding:utf-8


import pymysql.cursors
import requests
import json
import time


config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123',
          'db':'firstbaby',
          'charset':'utf8'
          }



url = r'https://api.douban.com/v2/movie/{mvid}'


print("begin...")
connect = pymysql.connect(**config)
cursor = connect.cursor()

cont = 1
mvid_dict=[]
cursor.execute("select mvid  from mv_top250 where country is null ")
rs = cursor.fetchall()

#获取全部列表
for item in rs:
    mvid_dict.append(item[0])
    
cont = 1
for i in mvid_dict:
    json_str=json.loads(requests.get(url.format(mvid=i)).text)
    country =json_str['attrs']['country'][0]
    cursor.execute('update  mv_top250 set country=%s where mvid=%s', [country,i])
    connect.commit()
    print(cont)
    time.sleep(20)
    cont +=1
    


cursor.close()
connect.close()
print("end...")
