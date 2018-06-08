# -*- coding: utf-8 -*-
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
