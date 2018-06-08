import psycopg2
from Common import db_config
import math
import collections


conn =psycopg2.connect(**db_config)
cur =conn.cursor()



#查询tree表,构造tree对象
def get_tree_dict():
    tree_dict={}
    
    cur.execute("select attr_key,descr_en,attr_type from t_attr_tree")
    tree_data =cur.fetchall()
    for i in tree_data:
        attr_key=i[0]
        desc =i[1]
        attr_type=i[2]
        tree_dict[attr_key]=[desc,attr_type]

    return tree_dict



#传入ad_code,priod_time查询出 ad_data
def get_map_data(code,date):
    cur.execute("select ad_data  from t_admin_attr where ad_code='%s' and period_time ='%s';"%(str(code),str(date)))
    map_data=cur.fetchone()[0]
    return map_data

'''
def get_base(code,date):
    cur.execute("select COALESCE(sum((ad_data->>'2')::decimal),0) dataValue from t_admin_attr,t_admin where t_admin_attr.ad_code = t_admin.ad_code and t_admin.ad_parent_code = '%s' and t_admin_attr.period_time='%s'; "%(str(code),str(date)))
    base=cur.fetchone()[0]
    return math.ceil(base)
'''

tree_dict=get_tree_dict()
#南京320100000000
#玄武320102000000
map_data =get_map_data("320102000000","2018-01-01")

#base =get_base("320100000000","2018-01-01")

data={}
for i in map_data.keys():
    data[i]=[tree_dict[i][0],map_data[i],tree_dict[i][1]]
    #print(i,"\t",tree_dict[i][0],"\t",map_data[i],"\t",tree_dict[i][1])


cur.close()
conn.close()


class Parse_data(object):
    def __init__(self,data):
        self._data=data
        self._base= data["6"][1]


    def log(func):
        def wrapper(*args,**kw):
            print("\n")
            print(func.__doc__)
            return func(*args,**kw)
        return wrapper
    def cal_per(slef,num,base):
        #给定两个数值，计算比例,三位小数
        return round(num/base,3)
    def cal_num(self,per,base):
        #给定比例，计算数量，取整
        return math.ceil(per*base)
    def cal_round(self,num,pos):
        return round(num,pos)

    def format_data(self,f_data):
        for k,v in f_data.items():
            print(k,v)
        


    def output_sidebar(self):
        #print(dir(self))
        for i in dir(self):
            if i[:5] =="side_":
                eval("self."+str(i)+"()")

    def output_detial(self):
        #print(dir(self))
        for i in dir(self):
            if i[:3] =="de_":
                eval("self."+str(i)+"()")



        
    @log
    def side_1(self):
        '人口数量'
        jz=math.ceil(data["3"][1])
        gz=math.ceil(data["4"][1])
        
        d=collections.OrderedDict()
        d["总人数"]=jz+gz
        d["居住人数"]=jz
        d["工作人数"]=gz
        self.format_data(d)

        
    @log
    def side_2(self):
        '销售潜力指数'
        print("暂无")

    @log
    def side_3(self):
        '店铺数量'
        d=collections.OrderedDict()
        ct_num=data["119-149"][1]
        xd_num=data["119-144"][1]
        d["传统渠道"]=ct_num
        d["现代渠道"]=xd_num
        d["传统渠道占比"]=self.cal_per(ct_num,ct_num+xd_num)
        d["现代渠道占比"]=self.cal_per(xd_num,ct_num+xd_num)

        self.format_data(d)

    @log
    def side_4(self):
        '性别分布(比例吻合，人数检查前四位即可)'
        d=collections.OrderedDict()
        male=data["10"][1]
        female=data["9"][1]
        d["男"]=self.cal_num(male,self._base)
        d["女"]=self.cal_num(female,self._base)
        d["男占比"]=self.cal_round(male,3)
        d["女占比"]=self.cal_round(female,3)

        self.format_data(d)


    @log
    def side_5(self):
        '年龄分布(比例吻合，人数检查前四位即可)'
        d=collections.OrderedDict()
        d["18以下比"]=self.cal_round(data["12"][1],3)
        d["18-24比"]=self.cal_round(data["13"][1],3)
        d["25-34比"]=self.cal_round(data["14"][1],3)
        d["35-44比"]=self.cal_round(data["15"][1],3)
        d["45-54比"]=self.cal_round(data["16"][1],3)
        d["55-64比"]=self.cal_round(data["17"][1],3)
        d["64以上比"]=self.cal_round(data["18"][1],3)

        d["18以下"]=self.cal_num(data["12"][1],self._base)
        d["18-24"]=self.cal_num(data["13"][1],self._base)
        d["25-34"]=self.cal_num(data["14"][1],self._base)
        d["35-44"]=self.cal_num(data["15"][1],self._base)
        d["45-54"]=self.cal_num(data["16"][1],self._base)
        d["55-64"]=self.cal_num(data["17"][1],self._base)
        d["64以上"]=self.cal_num(data["18"][1],self._base)
        

        self.format_data(d)




    #####detial#####
    def de_1(self):
        self.side_1()
        
            

    



        
        
        


        


if __name__=="__main__":
    parse=Parse_data(data)
    #parse.output_sidebar()
    parse.output_detial()





    

