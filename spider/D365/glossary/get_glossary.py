#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.parse
import json


html=urlopen("https://docs.microsoft.com/zh-cn/dynamics365/unified-operations/fin-and-ops/get-started/glossary?toc=/dynamics365/unified-operations/fin-and-ops/toc.json")
Bsobj=BeautifulSoup(html,"html.parser")


lst= Bsobj.find(id="a-nameaaa").find_next_siblings("h6")
lst2= Bsobj.find(id="a-nameaaa").find_next_siblings("p")

# for i in lst:
# 	print(i.find("strong").get_text())

# for i in lst2:
# 	print(i.get_text())