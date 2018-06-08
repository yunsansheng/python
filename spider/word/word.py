#coding:utf-8


import pymysql.cursors
import requests
import json
import time


'''
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'web',
          'charset':'utf8'
          }
'''
config = {
          'host':'qdm170694251.my3w.com',
          'port':3306,
          'user':'qdm170694251',
          'password':'yunfei1314',
          'db':'qdm170694251_db',
          'charset':'utf8'
          }

url = r'http://dict-co.iciba.com/api/dictionary.php?w={keyword}&type=json&key=2A6381DA00C5F55DAE52B76AF3564377'


print("begin...")
connect = pymysql.connect(**config)
cursor = connect.cursor()



word_dict=[]
cursor.execute("select word  from word_list where ph_en is null ")
rs = cursor.fetchall()


#获取全部列表
for item in rs:
    word_dict.append(item[0])

print(len(word_dict))
num =1
for i in word_dict:
    json_str=json.loads(requests.get(url.format(keyword=i)).text)
    try:
        ph_en = json_str['symbols'][0]['ph_en']
        ph_en_mp3 = json_str['symbols'][0]['ph_en_mp3']
        ph_am = json_str['symbols'][0]['ph_am']
        ph_am_mp3 = json_str['symbols'][0]['ph_am_mp3']

        cursor.execute('update  word_list set ph_en=%s,ph_en_mp3=%s,ph_am=%s,ph_am_mp3=%s where word=%s', [ph_en,ph_en_mp3,ph_am,ph_am_mp3,i])
        connect.commit()
    except:
        pass


    print(num)
    time.sleep(2)
    num += 1


    

cursor.close()
connect.close()
print("end...")

