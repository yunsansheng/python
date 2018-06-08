# -*- coding: utf-8 -*-

import url_manager,html_downloader
import time
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import urljoin
import json
import urllib.parse


import xlrd
import xlsxwriter


class HtmlParser(object):
	
	def _get_new_urls(self,page_url,soup):
		new_urls = set()

		links = soup.find_all('a',class_='vd_folder')

		for link in links:
			new_url = link['href']
			new_urls.add(new_url)
		return new_urls
		
	def _get_new_data(self,page_url,soup):
		res_data=[]
		lists= soup.find_all(class_="filelist")
		for i in lists:
			#print(i.find('div',class_='sort_name_detail').find('a')['title'])
			title=i.find('div',class_='sort_name_detail').find('a')['title']
			href=i.find('div',class_='sort_name_detail').find('a')['href']
			res_data.append([title,href])
		return res_data

	
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')


		new_urls  = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data


class HtmlOutputer(object):

	#从结果中提取.mobi的内容
	#去掉.后面的，前面的作为内容存到res.txt
	
	#other spider
	#根据每一个文件名去豆瓣搜，然后附上评分
	#最终输出到excel
	def __init__(self):
		self.res=[]
		self.mobi=[]
		self.out=[]

	def add_new_data(self,data):
		self.res.extend(data)

	def output(self):
		#print(self.res)
		def is_mobi(n):
			return n[0][-5:]=='.mobi'

		def to_mobi(n):
			return [n[0][:-5],n[1]]

		self.mobi=list(map(to_mobi,list(filter(is_mobi, self.res))))
		#print(self.mobi)

	def out_crawl_again(self):
		#抓取方法
		def douban_score(name,url):
			outname= urllib.parse.quote(name) 
			api_url="https://api.douban.com/v2/book/search?q={"+outname+"}"
			api_html=urlopen(api_url)

			data=api_html.read().decode()
			api_json =json.loads(data)
			bk_dict={}
			try:
				bk_dict["oname"]=name
				bk_dict["ourl"]=url
				bk_dict["name"]=api_json["books"][0]["title"]
				bk_dict["score"]=api_json["books"][0]["rating"]["average"]
				bk_dict["summary"]=api_json["books"][0]["summary"]
				if bk_dict!={}:
					self.out.append(bk_dict)
					#print(self.out)
					print("success")

			except:
			    print("failed")

		#逐个去爬
		for iv in self.mobi:
			douban_score(iv[0],iv[1])
			time.sleep(5)

	def out_to_xlsx(self):
		workbook = xlsxwriter.Workbook('mobi.xlsx')
		worksheet = workbook.add_worksheet()
		row=0
		col=0
		for item in self.mobi:
			worksheet.write(row,col,item[0])
			worksheet.write(row,col+1,item[1])
			# worksheet.write(row,col,item["oname"])
			# worksheet.write(row,col+1,item["ourl"])
			# worksheet.write(row,col+2,item["name"])
			# worksheet.write(row,col+3,item["score"])
			# worksheet.write(row,col+4,item["summary"])
			
			row+=1

		workbook.close()






class SpiderMain(object):
	
	#构造函数，初始化各类管理器，解析器，下载器等
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = HtmlParser()
		self.outputer = HtmlOutputer()
	
	def craw(self,root_url):
		#将入口url添加进url管理器，url管理器中有一个待爬取的url,就可以启动循环了
		count = 1 #用于计数，计算当前爬取的是第几个url
		self.urls.add_new_urls(root_url)
		
		while self.urls.has_new_url():
			time.sleep(5)
			print("请等待五秒")
			
			try:#加入异常处理，有的网页打开没有数据

				new_url = self.urls.get_new_url()#从url管理器获取一个url
			
				print('crawl %d: %s'% (count,new_url)) 
				html_cont  = self.downloader.download(new_url)#获取完url，就要去下载它
				#print(html_cont[0:8])
				new_urls,new_data = self.parser.parse(new_url,html_cont)#下载url，就会得到新的url列表，和新的数据，那么我们就要去处理它
				self.urls.add_new_urls(new_urls)#将新的urls 添加到url管理器中
				# self.outputer.collect_data(new_data)
				#将新的数据收集起来
				#self.res.append(new_data)
				self.outputer.add_new_data(new_data)

				#if count == 10:
					#break
			
				count = count +1
			except:
				print('craw_fail')
		
		self.outputer.output()
		#self.outputer.out_crawl_again()
		self.outputer.out_to_xlsx()

if __name__ == "__main__":

	root_url = {"http://vdisk.weibo.com/s/z-wufAcWPQ4KC","http://vdisk.weibo.com/s/EsJ0GMTfrreA","http://vdisk.weibo.com/s/z67enMUwllHLh",
	"http://vdisk.weibo.com/s/ahLfbselke2yx",
	"http://vdisk.weibo.com/s/yWFwwqkLeauT-?category_id=27&parents_ref=yWFwwqkLeauU3",
	"http://vdisk.weibo.com/s/zhZlehUPpSJMf",
	"http://vdisk.weibo.com/s/dqrB1XjvMO4ej",
	"http://vdisk.weibo.com/s/th_71uozfOxu",
	"http://vdisk.weibo.com/s/tyirFJIwJmlb",
	"http://vdisk.weibo.com/s/FyX9kwddxBMHo",
	"http://vdisk.weibo.com/s/zEMMWN71QGb7p"}
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)

