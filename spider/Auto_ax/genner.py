import xlrd

data = xlrd.open_workbook('DynamicsExport (20).xlsx')
table = data.sheets()[0]
nrows = table.nrows

lst=[]
for i in range(1,nrows ):
    lst.append(table.row_values(i)[0])


print(lst)
    
