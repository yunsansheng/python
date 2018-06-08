#coding:utf-8
from urllib.request import urlopen


class Down_picture(object):
        def __init__(self,lst,title):
                self._gen = (x for x in lst)
                self._title=title

        def down_pic(self):
                count=1
                for url in self._gen:
   
                        
                        try:
                                res = urlopen(url)
                                if str(res.status)=='200':
                                        filename=self._title+"_"+str(count)+".jpg"
                                        with open(filename,'wb') as f:
                                                f.write(res.read())
                                                print("下载完成")
                                                count=count+1


                        except:
                                print("下载失败")

if __name__=="__main__":
        lst=["http://xxx","http://xxx"]
        down_jpg=Down_picture(lst,"abc")
        down_jpg.down_pic()







