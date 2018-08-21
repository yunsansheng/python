#coding:utf-8
import xlrd

worker_col ='AB'
percent_col ='AC'
showall =False

def col_index(col):
	if len(col)==1:
		return ord(col)- ord('A')
	elif len(col)==2:
		return (ord(col[0])-ord('A')+1)*26+ord(col[1])-ord('A')
	else:
		raise Exception("length of col must be 1 or 2",col)

wb =xlrd.open_workbook("Rolling forecast Q2&Q3_Kaishen_0820.xlsx")
sheet = wb.sheet_by_name("Domestic")

maxrow = sheet.nrows


 
col_worker=sheet.col_values(col_index(worker_col))[2:]
worker_set =set(col_worker)
worker_set.remove('') 
#print(len(col_worker))
#create a dict
out_dict={}
for i in worker_set:
	out_dict[i]=0

#print(out_dict)

col_effort =sheet.col_values(col_index(percent_col))[2:]
#print(len(col_effort))

data= list(zip(col_worker,col_effort))

for item in data:
	if item[0] in worker_set:
		out_dict[item[0]]=out_dict[item[0]]+float(item[1])
	

#print(out_dict)

for k,v in out_dict.items():
	if showall == False:
		if v !=1:
			print(k,v)

	else:
		print(k,v)








