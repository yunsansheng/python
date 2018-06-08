#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.parse
import json
import time
import pymysql


#for zhihu huati....
#test 19624363 =5 , 19768460 =1   19554405=50
def get_max_page(topic):
	url="https://www.zhihu.com/topic/{topic}/top-answers".format(topic=topic)
	try:
		Bsobj=BeautifulSoup(urlopen(url),"html.parser")
		max_page=int(Bsobj.find('div',class_="zm-invite-pager").find_all("span")[-2].get_text())
		return max_page
	except:
		return 1



#把数据存入josn文件.
def get_zhihu(topic,page,data_lst):
	time.sleep(8)
	url="https://www.zhihu.com/topic/{topic}/top-answers?page={page}".format(topic=topic,page=page)

	try:
		print("begin...page %s..."% page)
		Bsobj=BeautifulSoup(urlopen(url.format(page=page)),"html.parser")
		lst=Bsobj.find_all('div',class_="feed-item")
		for i in lst:
			data={}
			data["title"]=i.find('div',class_="content").find('h2').find('a').get_text().strip()
			data['question_no']=i.find('a',class_="question_link")['href'].split('/')[2]

			data['answerCount']=i.find('meta',itemprop="answerCount")["content"]
			data['best_answer_no']=i.find('meta',itemprop="answer-url-token")["content"]
			data["vote"]=i.find('div',class_="zm-item-vote-info")["data-votecount"]
			
			data["sourcefrom"]="知乎话题"
			data["source_topic"]=topic_dct[topic]
			data["topic_no"]=topic

			data_lst.append(data)
	except:
		print("page %s run failed"% page)


#json的一些文件操作
# def store(data):
#     with open('data.json', 'w') as json_file:
#         json_file.write(json.dumps(data))

def save_into_mysql(data):
	print("begin start save")
	conn= pymysql.connect(
	                host='localhost',
	                port =3306,
	                user='root',
	                passwd='123',
	                db ='firstbaby',
	                charset ='utf8'
	                )

	cursor= conn.cursor()
	for item in data:


		if cursor.execute('select * from news_artical where question_no=%s', [item['question_no']])==0:
			cursor.execute('insert into news_artical(title,sourcefrom,source_topic,topic_no,best_answer_no,vote,answerCount,question_no) values (%s,%s,%s,%s,%s,%s,%s,%s)', [item["title"],item["sourcefrom"],item["source_topic"],item["topic_no"],item["best_answer_no"],item["vote"],item["answerCount"],item["question_no"]]) 
		else:
			cursor.execute('select max(vote) from news_artical where question_no=%s',[item['question_no']])
			a=cursor.fetchall()[0][0]
			print(a)
			
			if int(item['vote'])>a:
				
				cursor.execute("update news_artical set vote=%s and best_answer_no=%s where question_no=%s",[item['vote'],item['best_answer_no'],item['question_no']])
			else:
				
				pass
		
		conn.commit()


	cursor.close()
	conn.close()
	print('save over!')








def get_topic_all(topic_lst):


	for tp in topic_lst:
		max_page=get_max_page(tp)

		page=1
		data_lst=[]

		while page<=max_page:
			get_zhihu(tp,page,data_lst)
			page=page+1

		# store(data_lst);	
		save_into_mysql(data_lst);

#=======main============
#topic_dct={19624363:"育儿社区",19768460:"育儿书籍"}
topic_dct={19554405:"育儿",19946832:"育儿经验"}
topic_lst=list(topic_dct.keys())
get_topic_all(topic_lst);










# url="https://www.zhihu.com/topic/19554405/top-answers?page={page}"
# try:
# 	print("begin...")
# 	Bsobj=BeautifulSoup(urlopen(url.format(page=page)),"html.parser")
# 	lst=Bsobj.find_all('div',class_="feed-item")
# 	#print(lst)
# 	for i in lst:
#                 title=i.find('div',class_="content").find('h2').find('a').get_text().strip()
#                 url=i.find('div',class_="content").find('div',class_="expandable").find('link')['href']
#                 vote=i.find('div',class_="content").find('div',class_="expandable").find("div",class_='zm-item-vote').find('a').get_text()

# except:
# 	print("page %s run failed.." % page )





# def get_zhihu(page):
# 	url="https://www.zhihu.com/topic/19554405/top-answers?page={page}"
# 	try:
# 		print("begin...")
# 		Bsobj=BeautifulSoup(urlopen(url.format(page=page)),"html.parser")
# 		lst=Bsobj.find_all('div',class_="feed-item")
# 		print(lst)

# 	except:
# 		print("page %s run failed.." % page )










#from div class="zm-invite-pager"获取倒数第二个的span里获得页数...确定循环.

#content
#find  div class="zu-top-feed-list"
            #---feed-item
            #url 和赞同数.
               #-----feed-main  content  h2  a text
               

#https://www.zhihu.com/topic/19554405/top-answers?page=2


#https://www.zhihu.com/topic/19554405/top-answers
