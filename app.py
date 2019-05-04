from flask import Flask,render_template,url_for,redirect
import os
import shutil

app = Flask(__name__)
path = "static"+os.sep+"xxoo"

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
    return redirect(url_for("page",p=1))
@app.route('/page/<int:p>')
def page(p):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(path):
        file=[]
        file.append(dirpath)
        file.append(filenames)
        filelist.append(file)
    s= len(filelist)-1
    return render_template("page.html" ,filelist=filelist[p],page=p,s=s)

@app.route('/delfiles/<string:path>/<int:p>')
def delfiles(path,p):
    shutil.rmtree(path)  # 递归删除文件夹
    return redirect(url_for("page",p=p))

if __name__ == '__main__':
    app.run()
