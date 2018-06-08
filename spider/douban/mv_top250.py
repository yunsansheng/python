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


url = r'https://api.douban.com/v2/movie/top250?start={page}'

runtime=time.time()


def get_mvtop250(url):
    print("start "+str(url))
    r=requests.get(url)
    json_str=json.loads(r.text)
    for key in json_str["subjects"]:
        mvid=int(key['id'])
        title=key['title']
        year=int(key['year'])
        average=key['rating']['average']
        collect =int(key['collect_count'])
        genres=','.join(key['genres'])  #lst 会有多个  影片类型
        img_url=key['images']['medium']
        addtime= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(runtime))
        cursor.execute("INSERT INTO mv_top250(mvid, title, year,average,collect,genres,img_url,addtime) SELECT %s,%s,%s,%s,%s,%s,%s,%s  FROM DUAL WHERE NOT EXISTS(SELECT mvid FROM mv_top250 WHERE mvid = %s)",[mvid, title, year,average,collect,genres,img_url,addtime,mvid])
        connect.commit()
        
        
        
        
    
        
        

    




    

print("begin...")
connect = pymysql.connect(**config)
cursor = connect.cursor()

p=1
while p <=13:
    get_mvtop250(url.format(page=(p-1)*20))
    p+=1
    time.sleep(3)


cursor.close()
connect.close()
print("end...")
    



    

# while p <=13:   
#     try:
#         hjson = json.loads(urllib2.urlopen(html.format(page=(p-1)*20)).read())
#         # list数据集中提取数据
#         for key in hjson['subjects']:
#             mvid=int(key['id'].encode('utf-8'))
#             title=key['title'].encode('utf-8')
#             year=int(key['year'])
#             average=key['rating']['average']
#             collect =int(key['collect_count'])
#             genres=','.join(key['genres']).encode('utf-8')  #lst 会有多个  影片类型
#             img_url=key['images']['medium'].encode('utf-8')

           
#             cursor.execute('insert into mv_top250(mvid, title,year,average,collect,genres,img_url) values (%s,%s,%s,%s,%s,%s,%s)', [mvid, title,year,average,collect,genres,img_url])    
            
#             conn.commit()



#     except Exception as e:
#         print e
    

