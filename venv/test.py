from flask import Flask,render_template,request,flash,session
import sqlite3
app = Flask(__name__,static_url_path='')
app.secret_key = "aneha"

#初始界面
@app.route('/',methods=['GET','POST'])
def hello_world():
    if(request.method=='POST'):
        return 'success'
    return  render_template('index.html')

#用户登录
@app.route('/login',methods=['GET','POST'])
def hello_world2():

    if (request.method == 'POST'):
        name = request.form["name"]
        id = request.form['id']
        password = request.form['password']
        conn = sqlite3.connect('oj.db')
        cursor = conn.cursor()
        s = "SELECT * from user where ID = '{}'".format(id)

        values = list(cursor.execute(s).fetchall()[0])
        if(values[2]==password and values[1]==name):
            return "success"
        else:
            return "error"
    else:
        return  render_template('login.html')

#管理员登录

@app.route('/adlogin', methods=['GET', 'POST'])
def hello_world4():
    if (request.method == 'POST'):
        name = request.form["name"]
        id = request.form['id']
        password = request.form['password']
        conn = sqlite3.connect('oj.db')
        cursor = conn.cursor()
        s = "SELECT * from administrator where ID = '{}'".format(id)

        # values = list(cursor.execute(s).fetchall()[0])
        values = cursor.execute(s).fetchall();
        print(values)
        if (values and list(values[0])[2] == password and list(values[0])[1] == name):
            return render_template('problems.html')

        else:
            flash("用户名或密码错误，请重新输入", category='notequal')
            print("444444")
            return render_template('adlogin.html')
    else:
        return render_template('adlogin.html')


#用户注册信息
@app.route('/register',methods=['GET','POST'])
def hello_world3():
    #注册用户
    conn = sqlite3.connect('oj.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE if not exists user
           (ID TEXT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           PASSWORD       TEXT    NOT NULL);''')



    if(request.method=='POST'):
        name = request.form['name']
        id=request.form['id']
        password = request.form['password']
        password2 = request.form['password2']
        # if not all([name,id,password,password2]):
        #     flash("param error")
        if(id==""):
            flash("学号不能为空",category='idnull')
        if (name == ""):
            flash("姓名不能为空", category='namenull')
        if (password == ""):
            flash("密码不能为空", category='passwordnull')
        if (password2 == ""):
            flash("确认密码不能为空", category='password2null')
        if(password!=password2):
            flash("两次输入密码不同，请重新输入",category='notequal')

        elif(id and  name and password and password2 and (password==password2)):
            s = "insert into {} values ('{}', '{}', '{}')".format('user', id, name, password)
            cursor.execute(s)



        # s = cursor.execute("SELECT * from user where ID = '001'")
        # values = s.fetchall()
        # print(values)
        conn.commit()

        cursor.close()
        conn.close()
    return  render_template('register.html')

#题目制作
@app.route('/makeproblem',methods=['GET','POST'])
def make_problem():
    conn = sqlite3.connect('oj.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE if not exists problems
           (PROBLEMID TEXT PRIMARY KEY     NOT NULL,
          PROBLEMTITLE           TEXT    NOT NULL,
          CONTENT     TEXT    NOT NULL,
          INPUTTYPE     TEXT,
          OUTPUTTYPE TEXT);''')



    if(request.method=='POST'):
        problemid = request.form['problemId']
        problemTitle=request.form['problemTitle']
        content = request.form['content']
        inputtype = request.form['inputType']
        outputtype = request.form['outputType']

        if not all([problemid,problemTitle,content,inputtype,outputtype]):
            flash("请补全信息",category='nullexist')

        elif(id and  name and password and password2 and (password==password2)):
            s = "insert into {} values ('{}', '{}', '{}')".format('problems', id, name, password)
            cursor.execute(s)
        conn.commit()
        cursor.close()
        conn.close()
    return  render_template('makeproblem.html')

  

if __name__ == '__main__':
    app.run(debug=True)
    # app.config['SEND_FILE_MAX_AGE_DEFAULT']= timedelta(seconds = 1)

