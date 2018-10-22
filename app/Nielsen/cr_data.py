#coding:utf-8

import json
import requests

def login():
	url='http://101.132.120.66/api/user/login'
	data={'username':'xxx','password':'xxxx'}
	r=requests.post(url,json=data,headers={'Content-Type':'application/json'})
	print(r.text)
	return json.loads(r.text)['data']



def getsetting():
	url="http://101.132.120.66/api/user/setting"
	header ={'Content-Type':'application/json'}
	header["cr-data-jwt"]=login()
	r=requests.post(url,headers=header)
	print(r.text)





def getdata():
	url="http://101.132.120.66/api/data/query"
	header ={'Content-Type':'application/json'}
	header["cr-data-jwt"]=login()
	data={
	"date":"2018-01-01",
	"adCode":"610103000000",
	"module":"grid"
	}
	r=requests.post(url,json=data,headers=header)
	print(r.text)


