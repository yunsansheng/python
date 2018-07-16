#coding:utf-8

import json
import xlrd
import re
import ast



#定义常量
title_row = 7
caseid_col = 2
filename="Starbucks_AMS_Public_API_TestCase_to change to postman .xlsx"
#rooturl=r"http://172.16.98.195:3006"
rooturl=r"{{URL}}"


def fm_dct(dct,atype):
        lst=[]
        lst.append({"key":"Accept","value":atype})
        lst.append({"key":"Content-Type","value":atype})
        for i in dct:
                lst.append({"key":i,"value":dct[i]})
        return lst

def clean(name):
        return name.capitalize().strip(" ")

def delbrk(name):
        return name.replace("\n","").replace("  ","")
                

def fil_sheet(name):
        return name[:2] =="1."



def search_index(olst,ktype):
        lst=list(map(clean,olst))
        if ktype in lst:
                st =lst.index(ktype)
                end=st+1
                for i in lst[st+1:]:
                        if i =='':
                                end=end+1
                        else:
                                break
        else:
                st = -1
                end = -1
        #print(st,end)
        return [st,end]

        
def search_items(olst):
        dct_item =[]
        #print(lst)
        lst=list(map(clean,olst))
        if "Url" in lst:
                dct_item.append("Url")
        if "Header" in lst:
                dct_item.append("Header")
        if "Body" in lst:
                dct_item.append("Body")

        return dct_item




def output_text(text,key,values):
        op_text='%s:\n'% text
        a_key =key[text]
        a_value =values[text]
        for i in range(len(a_key)):
                op_text = op_text +str(delbrk(a_key[i]))+" :"+str(a_value[i])+"\n"

        
        return op_text
        

def fun_com(items_rs,rs_key,rs_value):
        com_text=''
        #print(rs_key)
        #print(rs_value)
        for i in items_rs:
                com_text=com_text+ output_text(i,rs_key,rs_value)
   
        com_text=com_text[:-1]      
        return com_text

def get_imp(oname):
        name=oname.lower()
        if "all valid value" in name:
                return "High"
        elif "invalid" in name:
                return "Medium"
        elif "empty" in name or "all empty"in name:
                return "Low"
        else:
                return "Medium"

def get_after(name):
        return name.split("_")[1]


def get_sheet_name(sheet):
        m = re.match(r'^1\.\d{1,2}\s?_?(.*)',sheet).group(1)
        return m

def get_summary(keywords,ocaseid):
        
        #取第一个_后的所有内容
        #caseid =("_").join(ocaseid.split("_")[1:])
        #return keywords+"_"+caseid

        #只取第一个_到第二个_中间的内容
        return keywords+"_"+get_after(ocaseid)

#传入re_key or re_value
def get_dct(key,dct):
        if key in dct:
                return dct[key]
        else:
                return []
        

def rule(data):
        if data =="":
                return ""
        elif type(data) ==float or type(data) ==(int):
                return data
        elif data.lower().strip()=="empty" or data.lower().strip()=="空" or data.lower().strip()=="n/a":
                return ""
        elif data.strip()=="非空字符":
                return "12345abc"
        elif "特殊字符" in data:
                return "@#$%^&*"
        elif "#eg" in data:
                m = re.match(r'^.*#eg(.*)',data).group(1)
                #print(m)
                return m.strip()
        else:
                return data
        
def fil_null(name):
        return name != ""

def maprule(lst):
        all_l=list(map(rule,lst))
        return all_l
        #return list(filter(fil_null,all_l))
        

def parse_url(url,method,urlkey,urlvalue):
        urlvalue=maprule(urlvalue)
        
        url=url.strip()
        if url[:1]=="/":
                pass
        else:
                print("请检查URL参数是否正确" )
                print(url)
        
        url_param =re.findall("{(.*?)}",url)
        if url_param !=[]:
                #url中有参数需要补全
                url_param
                url=url.format(**dict(zip(urlkey,urlvalue)))
                
        
        return rooturl+url


def parse_head(header,headkey,headvalue):
        
        
        headvalue=maprule(headvalue)
        atype=""
        if "application/vnd.api+json" in header.lower():
                atype="application/vnd.api+json"
        else:
                atype="application/json"
        rs_header=fm_dct(dict(zip(headkey,headvalue)),atype)

        return rs_header
        

def rmkuohao(name):
        try:
                m = re.match(r'^(.*)\n?\(.*\)',name).group(1)
                #print(m)
                return m
        except:
                return name
                

def up_dict(dct,upkey,upval):
        if isinstance(dct,dict):
                for x in range(len(dct)):
                        tmp_key =list(dct.keys())[x]
                        tmp_value=dct[tmp_key]
                        if tmp_key ==upkey:
                                dct[tmp_key]=upval
                        up_dict(tmp_value,upkey,upval)
  
def parse_body(bodykey,bodyvalue,param):
        
        bodykey=maprule(list(map(rmkuohao,bodykey)))
        bodyvalue=maprule(bodyvalue)
        
        body={}  
        body["mode"]="raw"
        dctbody=dict(zip(bodykey,bodyvalue))
        '''
        if len(dctbody) !=0:
                bodyraw={}
                bodyraw["data"]={}
                for i in dctbody:
                        bodyraw["data"][i]= dctbody[i]
                
                body["raw"]=json.dumps(bodyraw,indent=4)
                
                #print(body["raw"])
        else:
        
                body["raw"]=""
                
        return body
        '''
        #print(dctbody)

        if param !="":
                if len(dctbody)!=0:
                        bodyraw={}
                        bodyraw["data"]={}
                        #print(param)
                        bodydict=ast.literal_eval(param)
                        for i in dctbody:
                                up_dict(bodydict,i,dctbody[i])
                        
                        body["raw"]=json.dumps(bodydict,indent=4)
                else:
                        bodydict=ast.literal_eval(param)
                        body["raw"]=json.dumps(bodydict,indent=4)
                #print(body["raw"])
                
        else:
                if len(dctbody) !=0:
                        bodyraw={}
                        bodyraw["data"]={}
                        for i in dctbody:
                                bodyraw["data"][i]= dctbody[i]
                        body["raw"]=json.dumps(bodyraw,indent=4)
                else:
                     body["raw"]=""   
        

        return body
                

            

#filename -> casesheet -> dtlcase 
#filename -> excel name
#casesheet -> sheet name
#dtlcase -> caseid


#处理json
#init data
data={"info":{},"item":[]}
data["info"]["name"]=filename[:-5]
data["info"]["_postman_id"]=""
data["info"]["description"]=""
data["info"]["schema"] = r"https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
    
wb =xlrd.open_workbook(filename)
sheets=list(filter(fil_sheet,wb.sheet_names()))

for sheet in sheets:
        obj={}
        obj["name"]=sheet
        obj["description"]=""
        obj["item"]=[]

        data["item"].append(obj)

        table = wb.sheet_by_name(sheet)
        nrows = table.nrows

        title_lst= table.row_values(title_row)
        #查找拥有的类型,返回lst集合 itmes_rs
        items_rs =search_items(title_lst)
        #查找每个类型的区间，返回dict  rs_dct
        rs_dct={}
        for rs in items_rs:
                rs_dct[rs]=search_index(title_lst,rs)
        #返回项目集合res_key
        rs_key={}
        for ky in items_rs:
                rs_key[ky]=table.row_values(title_row+1)[rs_dct[str(ky)][0]:rs_dct[str(ky)][1]]

        #method
        method= table.row_values(title_row-3)[2].strip().upper()
        #url
        url =table.row_values(title_row-1)[2]
        header =table.row_values(title_row-2)[2].lower()
        param = table.row_values(title_row+1)[1].strip()
        
        print(sheet)
        #print(param)

        #写入json
        for i in range(title_row+2,nrows):
                v_item =table.row_values(i)
                caseid =v_item[caseid_col]

                rs_value={}
                #返回项目的value rs_value
                for va in items_rs:
                        rs_value[str(va)]=v_item[rs_dct[str(va)][0]:rs_dct[str(va)][1]]

                if caseid !='':
                        single_rq={}
                        single_rq["name"]=caseid
                        single_rq["request"]={}
                        single_rq["response"]=[]
                        #req
                        single_rq["request"]["url"]=parse_url(url,method,get_dct("Url",rs_key),get_dct("Url",rs_value))
                        single_rq["request"]["method"]=method
                        single_rq["request"]["header"]=parse_head(header,get_dct("Header",rs_key),get_dct("Header",rs_value))
                        single_rq["request"]["body"]=parse_body(get_dct("Body",rs_key),get_dct("Body",rs_value),param)
                        obj["item"].append(single_rq)
                                
        
            
        
        
#将data写入对象
json_str=json.dumps(data,indent =4)            
        
with open(filename[:-5]+".json","w") as f:
        f.write(json_str)
    
    
    
    

    

