#coding:utf-8

import requests
import json

ids=('2',
 '3',
 '4',
 '5',
 '9',
 '10',
 '12',
 '13',
 '14',
 '15',
 '16',
 '17',
 '18',
 '20',
 '21',
 '22',
 '24',
 '25',
 '26',
 '28',
 '29',
 '30',
 '31',
 '34',
 '40',
 '188',
 '189',
 '45',
 '46',
 '48',
 '49',
 '50',
 '51',
 '52',
 '53',
 '54',
 '55',
 '56',
 '57',
 '58',
 '59',
 '60',
 '61',
 '62',
 '63',
 '64',
 '65',
 '66',
 '67',
 '68',
 '69',
 '70',
 '71',
 '72',
 '73',
 '74',
 '75',
 '77',
 '78',
 '79',
 '80',
 '81',
 '82',
 '83',
 '84',
 '85',
 '86',
 '87',
 '88',
 '89',
 '90',
 '91',
 '92',
 '93',
 '94',
 '95',
 '96',
 '110',
 '111')

def get_token():
	url="http://172.16.98.194/nielsen/user/login"
	header={"Content-Type":"application/json"}
	data={'userName':'admin','password':'nielsen_123'}
	r=requests.post(url,json=data,headers={'Content-Type':'application/json'})
	#print(json.loads(r.text)['data']['token'])
	return json.loads(r.text)['data']['token']


def grid_baidu(gridId,meshId):
	kpi_codes=ids
	periodDate='2018-06-01'

	url="http://172.16.98.194/nielsen/gridDetail/singleGridBaidu"
	header={"Content-Type":"application/json"}
	header["authorization"]=get_token()
	data={'periodDate':periodDate,'gridId':gridId,'meshId':meshId,"kpiCodes":kpi_codes}
	#print(header)
	r=requests.post(url,json=data,headers=header)
	print(r.text)

grid_baidu(226,17697)