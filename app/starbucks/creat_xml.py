#coding:utf-8
from xml.dom.minidom import Document

'''
#状态说明
pass p
fail f

分别输入成功和失败的id
失败的优先级高级成功，如果同时设置了一个case p和f,将默认为失败。
如果成功[1,100],失败7,那么7将失败,其余均为成功
'''

##参数区
project="WCL系统知识回收"
prefix ="WCL-"
build="Round1"
testertxt="xx@softtek.com"
#输入成功caseid
pass_case=[1,2,3]
#输入失败caseid
fail_case=[1,2]

#优先级参数,默认失败的优先级高,参数是小写的p和f
#如果是p，则成功的优先级高
#如果是f,则失败的优先级高
pr="f"




#-====================#
def parse(ls):
    setlst=set()
    for i in ls:
        if type(i) is int:
            setlst.add(i)
        elif type(i) is tuple and len(i) ==2 and i[1]>i[0]:
            if  type(i[0]) is int and type(i[1]) is int:
                for num in range(i[0],i[1]+1):
                    setlst.add(num)
            else:
                print("请输入整数")
                break
        else:
            print("输入格式不符合要求,请检查")

    return setlst

def setsort(set):
    lst =list(set)
    lst.sort()
    return lst
        
def get_res(pass_case,fail_case):
    dct={}
    if pr=="f":
        p =parse(pass_case) -parse(fail_case)
        f =parse(fail_case)
    elif pr =="p":
        p =parse(pass_case)
        f =parse(fail_case)-parse(pass_case)
    else:
        print("输入的pr参数不对，请检查")


    print("成功的case:%s" % setsort(p))
    print("失败的case:%s" % setsort(f))

    for i in setsort(p):
        dct[i]="p"
        
    for o in setsort(f):
        dct[o]="f"

    return dct   



# 创建dom文档
doc = Document()

#创建根节点
rootlist = doc.createElement('results')
# 根节点插入dom树
doc.appendChild(rootlist)

testproject = doc.createElement('testproject')
testproject.setAttribute("name",project)
testproject.setAttribute("prefix",prefix)
rootlist.appendChild(testproject)

testplan = doc.createElement('testplan')
testplan.setAttribute("name",project)
rootlist.appendChild(testplan)

bulid = doc.createElement('bulid')
bulid.setAttribute("name",project+build)
rootlist.appendChild(bulid)


dct=get_res(pass_case,fail_case)
for key in sorted(dct.keys()):
    testcase = doc.createElement('testcase')
    testcase.setAttribute("external_id",prefix+str(key))

    result = doc.createElement('result')
    result_text =doc.createTextNode(dct[key])
    result.appendChild(result_text)
    testcase.appendChild(result)

    tester = doc.createElement('tester')
    tester_text =doc.createTextNode(testertxt)
    tester.appendChild(tester_text)
    testcase.appendChild(tester)

    rootlist.appendChild(testcase)


# 将dom对象写入本地xml文件
with open("imp.xml", 'wb') as f:
    f.write(doc.toprettyxml(indent='\t', encoding='UTF-8'))


