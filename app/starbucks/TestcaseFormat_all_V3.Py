#coding:utf-8



import xlrd
import xlsxwriter
import re



#定义常量
title_row = 7
caseid_col = 2



Read_sheet="Starbucks_Push_Notification_API_TestCase"+".xlsx"
Save_sheet="233114"+".xlsx"


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
        
                




#打开工作薄
wb =xlrd.open_workbook(Read_sheet)
workbook = xlsxwriter.Workbook(Save_sheet)
all_sheet=wb.sheet_names()
sheetlist=list(filter(fil_sheet,all_sheet))


for sheet in sheetlist:
        table = wb.sheet_by_name(sheet)
        nrows = table.nrows

        title_lst= table.row_values(title_row)
        
        #查找拥有的类型,返回lst集合 itmes_rs
        items_rs =search_items(title_lst)

        #查找每个类型的区间，返回dict  rs_dct
        rs_dct={}
        for rs in items_rs:
                rs_dct[rs]=search_index(title_lst,rs)
        #print(rs_dct)


        #返回项目集合res_key
        rs_key={}
        for ky in items_rs:
                rs_key[ky]=table.row_values(title_row+1)[rs_dct[str(ky)][0]:rs_dct[str(ky)][1]]

        
        #获取expectRS index
        er=table.row_values(title_row).index("Expected Results")
        #caseid =table.row_values(title_row).index("Case ID")

        #写入
        worksheet = workbook.add_worksheet(sheet)
        row=0
        worksheet.write_row(row,0,("CaseName",'Importance','Execution','Keywords','Summary','Preconditions',"StepActions","ExpectedResults","ExecutionType","Comment"))
        for i in range(title_row+2,nrows):
                v_item =table.row_values(i)
                caseid =v_item[caseid_col]
                expectRS = v_item[er]
                
                rs_value={}
                #返回项目的value rs_value
                for va in items_rs:
                        rs_value[str(va)]=v_item[rs_dct[str(va)][0]:rs_dct[str(va)][1]]
                        

                
                if caseid !='':
                        combine= fun_com(items_rs,rs_key,rs_value)
                        importance =get_imp(caseid)
                        keywords=get_sheet_name(sheet)
                        summary= get_summary(keywords,caseid)
                        
                        row += 1
                        worksheet.write_row(row,0,(caseid,importance,1,keywords,summary,'',combine,expectRS,1,""))
        print("Sheet名称:%s" %sheet)  
        print("含有类型:%s"% items_rs)#items_rs
        print("类型区间：%s"% rs_dct) #rs_dct
        print("类型详情: %s" %rs_key)#rekey
        print("\n")

     
workbook.close()                





