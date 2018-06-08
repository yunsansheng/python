import xlrd
import xlsxwriter



#cell_A1 = table.cell(0,0).value
#print(cell_A1)

def get_step_Description(name,sheet,col,row):
        #input the name of excel
        data =xlrd.open_workbook(name)
        #input sheet name
        table = data.sheet_by_name(sheet)
    #input sheet and row
        data=table.col(col-1)[row:]
        return data


def generate_num(mod,data):
        fst=1
        sec=0
        thd=0
        #'.'.join([str(fst),str(sec),str(thd)])
        gener=[]
        for i in data:
                if i.value=='':
                        sec=sec+1
                        thd=0#recount
                        line=['.'.join([str(mod)+str(fst),str(sec)]),'']
                else:
                        
                        thd=thd+1
                        line=['','.'.join([str(fst),str(sec),str(thd)])]
                #add to gener
                gener.append(line)
        return gener


def write_into_xlsx(gener):
        workbook = xlsxwriter.Workbook('numseq.xlsx')
        worksheet = workbook.add_worksheet()
        row=0
        col=0
        
        for item in gener:
                worksheet.write(row,col,item[0])
                worksheet.write(row,col+1,item[1])
                row+=1
        workbook.close()
                
        

#==================================================
name ="D365_Finance Module Test Case_v1.xlsx"
sheet = u"BUD"
col = 6
row = 21

mod="BUD"


data=get_step_Description(name,sheet,col,row)
gener=generate_num(mod,data)
write_into_xlsx(gener)

print("ok,pls check")



        
        

