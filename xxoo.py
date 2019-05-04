#爬取草榴的图片，多线程改进版
import urllib.request
import requests
import bs4
import pickle #导入pickle模块
import os
from fake_useragent import UserAgent
# 屏蔽warning信息
requests.packages.urllib3.disable_warnings()
import threading

imgpath = r'static\xxoo'

ua = UserAgent()
myHead = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
def openURL(url):
    head = {'User-Agent': ua.random}

    print(url)
    res=requests.get(url, headers=head,verify=False)
    res.encoding = 'gbk'
    return res

def openUrlImg(url): #打开链接
    head={'User-Agent':ua.random}
    req=urllib.request.Request(url,headers=head)
    res=urllib.request.urlopen(req)
    html=res.read()
    return html

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, url,path):
            threading.Thread.__init__(self)
            self.url = url
            self.path=path

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        with threading.Semaphore(100):
            try:
                fileName = self.url.split("/")[-1]
                folder = os.path.exists(imgpath +"/" + self.path + "/" + fileName)
                if not folder:  # 判断文件是否已经存在
                    with open(imgpath +"/" + self.path + "/" + fileName, "wb") as f:
                        img = openUrlImg(self.url)
                        f.write(img)
                        print("保存", fileName, "完毕！")
                else:
                    print("文件已经存在")
            except Exception as e :
                print("保存文件出错"+e)


def sevMM(path,url):
    folder = os.path.exists(imgpath+"/"+path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(imgpath+"/"+path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
        #raise Exception("文件夹已经存在")
    for i in url:
        # 创建新线程
        t=myThread(i,path)
        t.start()


def getimg(imgPage,path):
    imgUrls=[]
    sup = bs4.BeautifulSoup(imgPage.text, "html.parser")
    img = sup.find_all("input",type="image")
    for i in img:
        imgUrls.append(i["data-src"])
        print(i["data-src"])
    sevMM(path,imgUrls)


def sevMenu(data):
    with open(imgpath+"\menu.dat","wb") as f:
        pickle.dump(data,f)  # 将列表倒入文件
def opeMenu():
    file = open(imgpath+"\menu.dat",'rb')
    data = pickle.load(file)
    return data

def getMenu(url):#获取目录并保存
    menu = []
    for page in range(1,10):
        res = openURL(url+"/thread0806.php?fid=16&search=&page="+str(page))
        sup = bs4.BeautifulSoup(res.text, "html.parser")
        title = sup.find_all("h3")

        for i in  title:
            if i.a["href"]=="notice.php?fid=-1#1":
                continue
            if i.a.font != None:
                if i.a.font["color"]== "blue" or i.a.font["color"]== "red" :
                    continue
            line=[]
            line.append(i.a["href"])
            line.append(i.a.text)
            menu.append(line)
        print("==============添加目录中==================")
    print(menu)
    sevMenu(menu)


def main():
    url = "https://www.t66y.com"
    try:
        menuList =opeMenu()
        print("保存的",menuList)
        print(len(menuList))
    except Exception:
        getMenu(url)
        menuList = opeMenu()
        print("保存的", menuList)
        print(len(menuList))

    tag=0
    for i in menuList:
        tag+=1
        try:
            imgPage=openURL(url+"/"+i[0])
            print(i[1])
            getimg(imgPage,i[1])
        except Exception as e :
            print("出现错误",e)
        sevMenu(menuList[tag:])



if __name__ == '__main__':
   main()