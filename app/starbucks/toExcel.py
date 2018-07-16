#coding:utf-8

import json
import re
import xlsxwriter


def get_data():
    with open("data.json") as f:
        data=f.read()
        json_lst=json.loads(data)
        return json_lst


def get_statu(name):
    m = re.match(r'^<.*title=(.*)alt=.*',name).group(1)
    return m
    

data=get_data()


workbook = xlsxwriter.Workbook("allcase.xlsx")

for i in range(len(data)):
    md=data[i]
    #print(md["id"])
    md_name= md["name"][:-9]#excel name can't over 31
    worksheet = workbook.add_worksheet(md_name)
    row=0
    worksheet.write_row(row,0,("MDname",'Casename','detail','Statu'))
    for f in md["children"]:
        casename=f["name"]
        for l in f["children"]:
            dtlname=l["name"]
            statu=l["text"]
            row +=1
            worksheet.write_row(row,0,(md_name,casename,dtlname,get_statu(statu)))

            
workbook.close()                  
        


