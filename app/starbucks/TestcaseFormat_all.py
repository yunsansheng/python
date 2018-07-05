#coding:utf-8



import xlrd
import xlsxwriter




#定义常量
title_row = 7
caseid_col = 2
Header_col = 3
con_header_item ="x-transaction-id"
sheetlist=["1.1 Register a device","1.2 Remove a device","1.3 Verify a device",
           "1.4 Send apush notification PNC","1.5 Notification setting","1.6 Set User perference",
           "1.7 Get User perference","1.8 Send Notification by device"]


def get_body(lst):
        if "Body" in lst:
                st=lst.index("Body")
                end =lst.index("Expected Results")
                item ="Body"
                
        elif "URL" in lst:
                st=lst.index("URL")
                end =lst.index("Expected Results")
                item="URL"
        else:
                st=-1
                end=-1
                item=""
                
        print(st,end,item)
                
        return st,end,item



def fun_com(header_v,bodyitem,body_lst,itemtype):

        bodytext=''
        if body_lst!=[]:
                for i in range(len(body_lst)):
                        bodytext=bodytext+str(bodyitem[i])+" :"+str(body_lst[i])+"\n"
                bodytext="\n%s:"%itemtype+"\n" + bodytext[:-1]
                
        return "Header: \n%s:%s %s" %(con_header_item,header_v,bodytext)



#打开工作薄
wb =xlrd.open_workbook("Starbucks_Push_Notification_API_TestCase.xlsx")
workbook = xlsxwriter.Workbook("Expenses01.xlsx")

for sheet in sheetlist:
        table = wb.sheet_by_name(sheet)
        nrows = table.nrows

        #获取起和终（不定）index
        st,end,itemtype = get_body(table.row_values(title_row))
        bodyitem =table.row_values(title_row+1)[st:end]
        print(bodyitem)
        #获取expectRS index
        er=table.row_values(title_row).index("Expected Results")

        #写入
        worksheet = workbook.add_worksheet(sheet)
        row=0
        for i in range(title_row+2,nrows):
                item =table.row_values(i)
                caseid =item[caseid_col]
                header =item[Header_col]
                body = item[st:end]
                expectRS = item[er]

                combine= fun_com(header,bodyitem,body,itemtype)
                if caseid !='':
                        row += 1
                        worksheet.write_row(row,0,(caseid,'','','','','',combine,expectRS))


        
        
workbook.close()                





