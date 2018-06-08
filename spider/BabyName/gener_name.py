#coding:utf-8

import xlrd
import xlsxwriter
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlencode
import re
import time 

setting={}

setting["name_prefix"] = "汪"
setting["sex"] = "0"  #boy 1,girl 0 
setting["area_province"] = "江苏"
setting["area_region"] = "无锡"
setting['year'] = "2017"
setting['month'] = "9"
setting['day'] = "1"
setting['hour'] = "10"
setting['minute'] = "42"




def get_names_from_xlsx(sex):
	if int(sex)==1:
		data = xlrd.open_workbook('name_dict.xlsx')
		table = data.sheet_by_name('男双字')
	else:
		data = xlrd.open_workbook('name_dict.xlsx')
		table = data.sheet_by_name('女双字')
	name_lst= table.col_values(0)
	return name_lst


def get_score(name):
	
	url="http://life.httpcn.com/xingming.asp"

	params = {}
	params['data_type'] = "0"
	params['year'] = setting['year']
	params['month'] = setting["month"]
	params['day'] = setting["day"]
	params['hour'] = setting["hour"]
	params['minute'] = setting["minute"]
	params['pid'] = setting["area_province"].encode('GB18030')
	params['cid'] = setting["area_region"].encode('GB18030')

	params['wxxy'] = "0"
	params['xing'] = setting["name_prefix"].encode('GB18030')
	params['ming'] = name.encode('GB18030')  

	if setting["sex"] == "1":
	    params['sex'] = "1"
	else:
	    params['sex'] = "0"
	    
	params['act'] = "submit"
	params['isbz'] = "1"

	post_data = urlencode(params).encode('GB18030')
	Bsobj=BeautifulSoup(urlopen(url,data=post_data),"html.parser",from_encoding="GB18030")
	try:
		wuge_score=float(Bsobj.find(string=re.compile("姓名五格评分")).next_sibling.get_text()[:-1])
		bazi_score=float(Bsobj.find(string=re.compile("姓名八字评分")).next_sibling.get_text()[:-1])
	except:
		wuge_score=0
		bazi_score=0
	return wuge_score,bazi_score



def main(name_lst,start):
	res=[]
	count=start
	for name in name_lst:
		wuge_score,bazi_score=get_score(name)
		full_name=setting["name_prefix"]+name
		print(count,full_name,wuge_score,bazi_score,wuge_score+bazi_score)
		res.append([full_name,wuge_score,bazi_score])
		count+=1
		time.sleep(1)
	return res









if __name__=="__main__":
	start=7023
	name_ge =(x for x in get_names_from_xlsx(setting["sex"])[start:])#获取数据
	print("获取数据成功，准备进行计算...")
	main(name_ge,start)



