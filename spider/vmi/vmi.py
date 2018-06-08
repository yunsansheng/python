#coding:utf-8
import requests
import json 
from bs4 import BeautifulSoup 
import sys
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

LOGIN_URL ="https://www.avmihub.com/names.nsf?Login"
values = {'Username': '', 'Password': ''}
postdata = urllib.parse.urlencode(values).encode()

user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headersone = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
request = urllib.request.Request(LOGIN_URL, postdata, headersone)

try:
    response = opener.open(request)
    page = response.read().decode()
    # print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)

ssid=''
for item in cookie:
    if item.name=='DomAuthSessId':
        ssid=item.value
        print(ssid)



info={}
info['note_time_new']=''
info['note_time_last']=''
info['send']=False



#如何获cookie
headers ={
	'Cookie':'A=50166-JGP; B=Jabil123456; pwd=Jabil123456; LastVisitUserName=50166-JGP; A=50166-JGP; B=Jabil123456; pwd=Jabil123456; LastVisitUserName=50166-JGP; DomAuthSessId='+str(ssid),
	'Origin':'https://www.avmihub.com',
	'Accept-Encoding':'https://www.avmihub.com',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Cache-Control':'max-age=0',
	'Referer':'https://www.avmihub.com/oadata/VMI_System.nsf/f_reportform?openform&Seq=2',
	'Connection':'keep-alive'
}

data = '__Click=48257FB0000A79B0.48235d7573677a2848257fb7000b6b1d%2F%24Body%2F0.13C&pagesize=2000&pageno=1&PageJumpto=&SelectDoc=&Operation=&Form=f_reportform&ParentCompanyNumber=&TXTINDEPARTMENT=&%25%25Surrogate_SearchMode=1&SearchMode=1&%25%25Surrogate_supplier=1&supplier=50166-JGP&customerMaterial=&%25%25Surrogate_materialState=1&materialState=&deliverNo=&%25%25Surrogate_confirm=1&confirm=&F_StartDate=&F_EndDate='

r = requests.post('https://www.avmihub.com/oadata/VMI_System.nsf/f_reportform?OpenForm&Seq=1', data=data, headers=headers,verify=False)

#print(r.text)

soup =BeautifulSoup(r.text,'html.parser',from_encoding ='utf-8')





try:
    node_head=soup.find('tr',class_='font9pt').next_sibling()
    node=soup.find('tr',class_='tabledetail0').next_sibling()
    node_time=node_head[23].get_text()
    info['note_time_new']= node_time
    node_apn=node[13].get_text()
    node_num=node[22].get_text()
    content = "/:heart"+"出货提醒:"+"\n"+ "APN号: "+str(node_apn)+"\n"+"数量："+str(node_num) +"\n"+"确认: "+str(node_time) 
    #读取上次内容
    with open('vmi.txt', 'r') as f:
        info['note_time_last']=f.read()
        print("上次保存："+info['note_time_last'])
    #如果有更新写入本次内容
    if (info['note_time_new']!=info['note_time_last']) and (info['note_time_new']!=''):
        print("记录有更新"+info['note_time_new'])
        info['send']=True
        with open('vmi.txt','w') as d:
            d.write(info['note_time_new'])

except:
    info['send']=True
    content ="获取数据失败，请联系管理员"




def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib.request.urlopen(gettoken_url)
    except urllib.error.HTTPError as e:
        print (e.code)
        print (e.read().decode("utf8"))
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
def senddata(access_token,user,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,   
        "toparty":"3",    # departmentid
        "msgtype":"text",  
        "agentid":"2", #applycation id
        "text":{
            "content":content
           },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False).encode(encoding='UTF8')
    send_request = urllib.request.Request(send_url, send_data)
    #response = json.loads(urllib2.urlopen(send_request).read())
    response =urllib.request.urlopen(send_request)
    msg =response.read()
    print (str(msg))


user = 'sandy' 
corpid = 'wx812ae8d875711da7'   
corpsecret = 'sayc0NWKZ8p-sFIasvL0oTJbQipW9habOR5nMXvbBiQBdxBeqtavrG3va58ts33J' 
if info['send']==True:
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,content)


