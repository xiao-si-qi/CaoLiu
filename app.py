from flask import Flask,render_template
import os

app = Flask(__name__)
path = r'static\xxoo'

@app.route('/del')
def delfile():
    import delf
    delf.search(path)
    return "删除空文件夹和无效文件完成"

@app.route('/pa')
def pa():
    import xxoo
    xxoo.main()
    return "爬取中"

@app.route('/')
def imglist():
    filelist=[]
    for dirpath, dirnames, filenames in os.walk(path):
        file=[]
        file.append(dirpath)
        file.append(filenames)
        filelist.append(file)
    return render_template("listfile.html" ,filelist=filelist)

if __name__ == '__main__':
    app.run()
