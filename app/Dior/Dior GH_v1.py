import time
import xlrd



class Gener_defectlist(object):

    def __init__(self,ad_v,ios_v,file,sheet_name,st):
        self.ad_v =ad_v
        self.ios_v =ios_v
        self.file =file
        self.sheet_name =sheet_name
        self.st =st #start from
    def output_header(self,data):
        str_head=r"""
**Dior Wechat H5 Defect Summary** 
Update Time: %s
Test Rounds: Second Round

                                                  

Total Defects: %d
Open Defects: %s
Close Defects: %d

Open Defects Severity: 
Fatal=%d, Critical=%d, Major=%d, Min=%d, Enhancement=%d
Close defects severity:
Fatal=%d, Critical=%d, Major=%d, Min=%d, Enhancement=%d

Description defects and need fix Fatal & Critical severity with high priority

""" % (data)
        print(str_head)
    def output_issue(self,data):
        str=r"""
- [ ] Defect ID: %d (%s)

**Severity:** %s
**Description:** %s
**Steps To Reproduce:**
```
%s
```
**Actual Result:** %s
**Expectation Result:** %s
**Device:** %s
**OS Version:** %s
**Test data:** %s

        """ %(data)
        print(str)
        
    def get_data(self):
        wb =xlrd.open_workbook(self.file)
        table = wb.sheet_by_name(self.sheet_name)
        nrows = table.nrows  #获取该sheet中的有效行数

        result=[]
        open_pro=[]
        close_pro=[]
        st_close=0   #num of close
        st_new =0
        st_open=0
        
        for i in range(1,nrows):
            item =table.row_values(i)
            
            defect_id=item[0]
            severity = item[1][2:]
            description= item[4]
            steps = item[5]
            actual = item[7]
            excepted = item[6]
            status= item[9]  
            devices=item[10]
            testdata=item[11]

            
            if devices == "Android":
                version=self.ad_v
            elif devices == "IOS":
                version =self.ios_v
            elif devices =="All":
                version = "All"
            

            if status =="Closed without change" or status =="Verified and Closed":
                out_st ="Closed"
                st_close += 1
                close_pro.append(severity)
            elif status =="Open" and defect_id > self.st:
                out_st ="New"
                st_new += 1
                open_pro.append(severity)
            elif status =="Open" and defect_id <= self.st:
                out_st ="Open"
                st_open += 1
                open_pro.append(severity)

                
            result.append((defect_id,out_st,severity,description,steps,actual,excepted,devices,version,testdata))
            
        return result,open_pro,close_pro,st_close,st_new,st_open

    def output(self):
        result,open_pro,close_pro,st_close,st_new,st_open =self.get_data()

        nowtime=time.strftime("%Y-%m-%d",time.localtime())
        total=len(result)
        openstr="%d(New=%d,Open=%d)" % (st_new+st_open,st_new,st_open)
        

        #print header
        self.output_header(data=(nowtime,total,openstr,st_close,open_pro.count("Fatal"),open_pro.count("Critical"),open_pro.count("Major"),open_pro.count("Minor"),open_pro.count("Enhancement"),close_pro.count("Fatal"),close_pro.count("Critical"),close_pro.count("Major"),close_pro.count("Minor"),close_pro.count("Enhancement")))

        #print issue
        for i in result:
            self.output_issue(data=i)

     
   


    
    def test(self):
        print(self.ad_v)
        print(self.ios_v)
        print(self.st)
    
    
if __name__=="__main__":
    #依次输入，安卓版本，IOS版本，文件名，sheet名,最后一个代表的是从这个开始都算以前的问题
    instance =Gener_defectlist("6.0","11.2.6","Bug Summary For Dior E-Loyalty Card 2018-03-13.xlsx","Dior Wechat",0)
    instance.output()

