from flask import Flask,render_template,url_for,redirect,request
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


@app.route('/pa2/<int:p>')
def pa2(p):
    import xxoo2
    xxoo2.main(p)
    return "爬取中"


@app.route('/')
def imglist():
    return redirect(url_for("page",p=0))
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

@app.route('/delfiles',methods=["POST"])
def delfiles():
    if request.method == "POST":
        file= request.form.get("f")
        page = request.form.get("page")
        print(file)
        if file=="static\\xxoo":
            print("不能删除此目录")
        else:
            shutil.rmtree(file)  # 递归删除文件夹
    # redirect:重定向，需要传入一个网址或路由地址
    # url_for:传入视图函数，返回该视图函数对应的路由地址
    return redirect(url_for("page",p=page))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
