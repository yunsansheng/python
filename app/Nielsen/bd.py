#coding:utf-8

import datetime
import json
import requests
from urllib.parse import urlparse 

import hashlib
import hmac
import base64

with open("/Users/henry.wang/documents/account.json") as f:
    ac = json.load(f)
    AK = ac["nielsen"]["account"]["bdkey"]["ak"]
    SK = bytes(ac["nielsen"]["account"]["bdkey"]["sk"],encoding="utf-8")


GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
nowtime = datetime.datetime.utcnow().strftime(GMT_FORMAT)
url ="http://180.76.38.221/crmap/CRMap/GeoLevel"

sign =''
#def sign_cal(method,content,curl):
def sign_cal(curl):
    #HTTP_METHOD =method
    #CONTENT_MD5 = '' if content =='' else hashlib.md5(content.encode('utf-8')).hexdigest().upper()   
    #CONTENT_TYPE = "Application/json" if method.upper() != "GET" else ""
    HTTP_METHOD ='POST'
    CONTENT_MD5='8ADA537A831DA396531BF4E7032B9AAE'
    CONTENT_TYPE ='Application/json'




    DATE= nowtime
    URLPATH = '/crmap/CRMap/GeoLevel?'
    global sign 
    sign = HTTP_METHOD+'\n'+CONTENT_MD5+'\n'+CONTENT_TYPE+'\n'+DATE+'\n'+URLPATH
    print(sign)

    #m = hashlib.sha256(sign.encode('utf-8'),SK.encode('utf-8'))
    m =hmac.new(SK,sign.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    print(m)
    #m ='7fd37583a9af8ece9b8b836672db71f9bfd9d613e0983e327789649484932c81'
    ###'ffead0e0e8e3a2ccf5938ef12393e1bd5dfafb7c36743cfd53aabd999064d264'
    return m

def res(url):
    path =urlparse(url).path
    query = urlparse(url).query
    return path+'?'+query

data={
 "version":"201806",
 "adcode":"610122000000",
 "measure":"2"
}


header ={}
header["Date"] = nowtime
signature =sign_cal(url)
header["Authorization"]  = "hmac-sha256 {0}:{1}".format(AK,signature)
#header["Content-Type"]="application/json"

r= requests.post(url,json = data,headers= header)
print(r.text)