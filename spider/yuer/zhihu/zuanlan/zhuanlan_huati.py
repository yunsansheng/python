# -*- coding: utf-8 -*-
import json
import time
import csv





#https://zhuanlan.zhihu.com/api/recommendations/columns?limit=8888&offset=0&seed=77

def load():
    with open('zhuanlan.json') as json_file:
        data = json.load(json_file)
        return data

data=load()



def write_csv(lst):
    with open("zhuanlan.csv","w",newline="") as datacsv:
        csvwriter = csv.writer(datacsv,dialect = ("excel"))
        csvwriter.writerows(lst)


lst=[]
for i in data:
    lst.append([i["name"],i["followersCount"],i["url"]])

write_csv(lst)
    
