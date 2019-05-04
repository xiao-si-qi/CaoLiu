#清除空文件夹和无效文件
import os
import imghdr
import shutil
def search(path):
  files=os.listdir(path)   #查找路径下的所有的文件夹及文件
  print(files)
  for filee in  files:
      f=str(path+"\\"+filee)    #使用绝对路径
      print(f)
      if os.path.isdir(f):  #判断是文件夹还是文件
            if not os.listdir(f):  #判断文件夹是否为空
              print(str(filee),"空")
              shutil.rmtree(f)
            else:
               files = os.listdir(f)
               for i in files:
                   typr = imghdr.what(f+"\\" + i)
                   if typr == None:
                       print("文件不完整删除：", f+"\\" + i)
                       os.remove(f+"\\" + i)

if __name__ =='__main__':
  path = r'static\xxoo'  #raw_input 函数数从命令输入
  search(path)
