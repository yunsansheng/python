#coding:utf-8
import requests
import json
import pymysql.cursors
import time

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123',
          'db':'firstbaby',
          'charset':'utf8'
          }


headers={
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"zh-CN,zh;q=0.9",
        "upgrade-insecure-requests":"1",
	"user-agen":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"cache-control":"max-age=0",
	"authority": "www.wukong.com",
	"cookie": "_ga=GA1.2.286306185.1513842764; tt_webid=70480784642; _ba=BA0.2-20171221-516a9-f1KeQeQJJmn0yMAhj9PD" 
}


def get_wenda():
    connect = pymysql.connect(**config)
    cursor = connect.cursor()
    cursor.execute("select count(1) from tiku")
    start=cursor.fetchone()[0]
    url="https://www.wukong.com/wenda/wapshare/subject/tab/brow/?subject_id=6509045544260731143&offset=0&tab_id=1"
    r=requests.get(url,headers=headers)
    json_str=json.loads(r.text)
    if json_str["err_no"]==0:
        datalst=json_str["data"]["tab_item_list"]
        for i in datalst:
            qid=i["question"]["qid"]
            title=i["question"]["title"]
            content=i["question"]["content"]["text"]
            create_time= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["question"]["create_time"]))
            #cursor.execute("insert into tiku(qid,title,content,create_time) values (%s,%s,%s,%s)",[qid,title,content,create_time])
            cursor.execute("INSERT INTO tiku(qid, title, content,create_time) SELECT %s, %s,%s,%s  FROM DUAL WHERE NOT EXISTS(SELECT qid FROM tiku WHERE qid = %s)",[qid,title,content,create_time,qid])
            connect.commit()
            
            
    else:
        print("获取失败..")
    print(title)

    cursor.execute("select count(1) from tiku")
    end=cursor.fetchone()[0]
    count=end-start
    
    print("新增了%s条数据,共%s条数据"% (count,end))


    cursor.close()
    connect.close()
    print("over")

while True:
    get_wenda()
    time.sleep(5)
    

    

