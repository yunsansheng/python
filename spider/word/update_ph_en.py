#coding:utf-8

import pymysql.cursors
import requests
import json
import time

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'web',
          'charset':'utf8'
          }


config2 = {
          'host':'qdm170694251.my3w.com',
          'port':3306,
          'user':'qdm170694251',
          'password':'yunfei1314',
          'db':'qdm170694251_db',
          'charset':'utf8'
          }

connect = pymysql.connect(**config)
cursor = connect.cursor()
cursor.execute("select id,ph_am  from word_list")
rs = cursor.fetchall()

word_dict=[]

for item in rs:
    word_dict.append([item[0],item[1]])

#print(word_dict[:3])
cursor.close()
connect.close()

connect2 = pymysql.connect(**config2)
cursor2 = connect2.cursor()

for i in word_dict:
    oid=i[0]
    ph_am =i[1]
    cursor2.execute('update word_list set ph_am ="%s" where id =%d'%(str(ph_am),oid))

cursor2.close()
connect2.close()
