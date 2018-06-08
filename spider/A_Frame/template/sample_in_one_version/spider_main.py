# -*- coding: utf-8 -*-

import url_manager,html_downloader
import time
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from urllib.parse import urljoin

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
			print(i.find('div',class_='sort_name_detail').find('a')['title'])
			res_data.append(i.find('div',class_='sort_name_detail').find('a')['title'])
		return res_data

	
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')


		new_urls  = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data


class HtmlOutputer(object):
	pass



class SpiderMain(object):
	
	#构造函数，初始化各类管理器，解析器，下载器等
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = HtmlParser()
		self.outputer = HtmlOutputer()
		self.res=[]
	
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
				self.res.append(new_data)
				if count == 10:
					break
			
				count = count +1
			except:
				print('craw_fail')
		# self.outputer.output_html()

if __name__ == "__main__":

	root_url = {"http://vdisk.weibo.com/s/z-wufAcWPQ4KC","http://vdisk.weibo.com/s/EsJ0GMTfrreA"}
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)

