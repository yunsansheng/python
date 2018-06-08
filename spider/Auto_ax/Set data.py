#Coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#data={"H001":[...],"H002":[...]}
data={"H001":['FE01', 'FE02', 'FE03', 'FE04', 'FE05', 'FE06', 'FE07', 'FE08', 'FE99', 'FL01', 'LB01', 'LI01', 'MV01', 'PM01', 'PM02', 'PM03', 'PM04', 'PM05', 'PM06', 'PM07', 'PM08', 'PM09', 'PM10', 'PM11', 'PM21', 'PM22', 'PM23', 'PM99', 'TC01', 'YA01']}



def autoax(url):
    #login
    browser = webdriver.Chrome()
    browser.get(url)
    input = browser.find_element_by_id("i0116")
    input.send_keys('milly.fan@win-hanverky.com.hk')#传送帐号
    button = browser.find_element_by_id('idSIButton9')#找到Next按钮
    button.click()
    time.sleep(5)
    input_psw = browser.find_element_by_id("passwordInput")
    input_psw.send_keys('History9090')#psw
    button_log = browser.find_element_by_id('submitButton')#找到Next按钮
    button_log.click()

    time.sleep(3)
    button_stay = browser.find_element_by_id('idBtn_Back')#stay sign in
    button_stay.click()
    time.sleep(5)

    #start..
    for item in data[company]:
    	#搜索
    	search =browser.find_element_by_id("assetgroup_1_QuickFilterControl_Input_input")
    	search.send_keys(item)
    	browser.find_element_by_id("assetgroup_1_QuickFilterControl_Input_input").send_keys(Keys.ENTER)
    	time.sleep(2)

    	#找到后
    	one=browser.find_element_by_id('assetgroup_1_Grid_RowTemplate_Row0')
    	one.click()
    	time.sleep(2)

    	bookbtn=browser.find_element_by_id('assetgroup_1_AssetGroupBookSetupBooks')
    	bookbtn.click()
    	time.sleep(3)

    	editbtn=browser.find_element_by_id('AssetGroupBookSetup_2_SystemDefinedViewEditButton_label')
    	editbtn.click()
    	time.sleep(3)

    	depstartm=browser.find_element_by_id('AssetGroupBookSetup_2_Depreciation_oadDepreciationStartMonth_input')

    	if depstartm.text =="Next month" or depstartm.text =="":
    	    print(company,"\t",item,"\t","未修改")
    	    time.sleep(1)
    	else:
    	    depstartm.send_keys("Next month")
    	    time.sleep(3)
    	    save_button=browser.find_element_by_id('AssetGroupBookSetup_2_SystemDefinedSaveButton_label')
    	    save_button.click()
    	    print(company,"\t",item,"\t","已修改")
    	    time.sleep(1)
    	close=browser.find_element_by_id('AssetGroupBookSetup_2_SystemDefinedCloseButton_label')
    	close.click()
    	time.sleep(1)
    	#清空search
    	search =browser.find_element_by_id("assetgroup_1_QuickFilterControl_Input_input")
    	search.send_keys("")
    	browser.find_element_by_id("assetgroup_1_QuickFilterControl_Input_input").send_keys(Keys.ENTER)



    #全部执行完后,quit,执行下一个公司.
    browser.quit()





#44家公司(45)
for i in range(1,2):
    company="H0"+str(i).zfill(2)
    url='https://win-prd.operations.dynamics.com/?cmp='+company+'&mi=AssetGroup'
    autoax(url)





    
    
