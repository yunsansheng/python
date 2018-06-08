#coding:utf-8


import requests as req
import json


#setting of database
db_config={
    'host':'172.16.98.182',
    'port':5432,
    'user':'postgre',
    'password':'postggre',
    'database':'nielsen'
    }



#function of get token
def get_token(username,password):
    log_url ="http://172.16.98.194/nielsen/user/login"
    payload  ={'userName':username,'password':password}
    headers={
		 'Origin':'http://172.16.98.194',
		 'Accept-Encoding':'gzip, deflate',
		 'Accept-Language':'zh-CN,zh;q=0.9',
		 'Content-Type':'application/json; charset=utf-8',
		 'Referer':'http://172.16.98.194/user/login',
		 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		 'Connection':'keep-alive',
		 'Host':'172.16.98.194'
    }
    res=req.post(log_url,data=json.dumps(payload),headers=headers)
    
    return json.loads(res.text)["data"]["token"]


 
  
if __name__=='__main__':
    a=get_token("ksf_test","123456")
    print(a)




