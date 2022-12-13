import os
from werkzeug.utils import *

from flask import*

from src.classify import predct
from src.dbconnection import*
app=Flask(__name__)
app.secret_key="something"

import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('login.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def Login():
    return render_template("Login.html")

@app.route('/SignIn')
def SignIn():
    return render_template('/SignIn.html')

@app.route('/log',methods=['post'])
def log():
    Username =request.form['textfield']
    print(Username)
    Password =request.form['textfield2']
    qry="select * from login where User_Name=%s and Password=%s"
    val = (Username,Password)
    res = selectone(qry,val)
    print(res)
    if res is None:
        return'''<script>alert("Invalid");window.location = "/" </script>'''
    elif res['Login_Type']=="admin":
        session['lid'] = res['Login_id']
        return redirect('/Home')
    elif res['Login_Type'] == "user":
        session['lid']=res['Login_id']
        return redirect('/User_Home')
    else:
        return'''<script>alert("Invalid,,,,,,,,,,,,,,");window.location = "/" </script>'''

@app.route('/Home')
def Home():
    return render_template('/Home.html')

@app.route('/Add_Recipie')
@login_required
def Add_Recipie():
    return render_template('/Add Recipie.html')

@app.route('/add',methods=['post'])
def add():
    Recipie=request.form['textfield']
    print(Recipie)
    Description = request.form['textarea']
    print(Description)
    qry = "insert into recipie values(null,%s,%s)"
    val = (Recipie, Description)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/Home" </script>'''


@app.route('/View_Feedback')
@login_required
def View_Feedback():

    qry = "SELECT * FROM `feedback` JOIN `user` ON `feedback`.`User_id`=`user`.`Login_id`"
    res = selectall(qry)
    return render_template('/View Feedback.html',data = res)

@app.route('/Add_Tips')
@login_required
def Add_Tips():
    return render_template('/Add Tips.html')

@app.route('/tips',methods=['post'])
def tips():
    Tips=request.form['textarea']
    print(tips)
    qry = "insert into tips values(null,%s,curdate())"
    val = (Tips)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/Home" </script>'''

@app.route('/View_Post')
@login_required
def View_Post():

    qry = "SELECT `post`.*,`user`.`First_Name`,`Last_Name` FROM `user` JOIN `post` ON `user`.`Login_id`=`post`.`User_id`"
    res = selectall(qry)
    return render_template('/View Post.html', data=res)

    return render_template('/View Post.html')


@app.route('/View_Help')
@login_required
def View_Help():
    qry = "SELECT `help`.*,`user`.`First_Name`,`Last_Name` FROM `user` JOIN `help` ON `user`.`Login_id`=`help`.`User_id`"
    res = selectall(qry)
    return render_template('/View Help.html',val = res)

@app.route('/Send_Reply')
@login_required
def Send_reply():
    id=request.args.get('hid')
    session['helpid']=id


    return render_template('/Send reply.html')

@app.route('/reply',methods=['post'])
def reply():
    Reply=request.form['textarea']
    print(Reply)
    qry = "update help set Answer=%s where Help_id=%s"
    val = (Reply,session['helpid'])
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/Home" </script>'''


@app.route('/Recipie')
@login_required
def Recipie():
    return render_template('/Recipie.html')

@app.route('/View_Recipie')
@login_required
def View_Recipie():

    qry = "SELECT * from recipie"
    res = selectall(qry)
    return render_template('/Edit Recipie.html', data=res)

@app.route('/RecipieEdit')
@login_required
def RecipieEdit():
    id = request.args.get('id')

    session['rid']=id
    qry = "SELECT * from recipie where Recipie_id=%s"
    val = (id)
    res = selectone(qry,val)
    print(res)
    return render_template('/RecipieEdit.html', data=res)

@app.route('/Incredients',methods=['get','post'])
@login_required
def Incredients():
    id = request.args.get('id')
    if request.method=="POST":
        i = request.form['i']
        iud("INSERT INTO `incredient_list` VALUES(NULL,%s,%s)",(id,i))
        return "<script>alert('Successfully Added');window.location = '/Incredients?id="+id+"' </script>"

    else:

        session['rid']=id
        qry = "SELECT * FROM `incredient_list` WHERE `rid`=%s"
        val = (id)
        res = selectall2(qry,val)
        print(res)
        return render_template('/Incredients.html', data=res)



@app.route('/update',methods=['post'])
def update():
    Rec=request.form['textfield']
    print(Rec)
    Desc = request.form['textarea']
    print(Desc)
    qry = "UPDATE recipie SET Recipie_Name=%s, Recipie_Description=%s WHERE Recipie_id=%s"
    val = (Rec,Desc,session['rid'])
    iud(qry,val)
    return '''<script>alert("Successfully Updated");window.location = "/View_Recipie" </script>'''

# @app.route('/deleteRecipie')
# @login_required
# def deleteRecipie():
#     id = request.args.get('id')
#     qry = "SELECT * from recipie where Recipie_id=%s"
#     # val = (id)
#     res = selectone(qry,str(id))
#     # print(res)
#     return render_template('/Edit Recipie.html', data=res)


@app.route('/deleteincr')
def deleteincr():
    id = request.args.get('id')
    qry = "DELETE FROM incredient_list WHERE id=%s"
    # val = (session['did'])
    iud(qry,id)
    return '''<script>alert("Successfully deleted");window.location = "/View_Recipie" </script>'''



@app.route('/delete')
def delete():
    id = request.args.get('id')
    qry = "DELETE FROM recipie WHERE Recipie_id=%s"
    # val = (session['did'])
    iud(qry,id)
    return '''<script>alert("Successfully deleted");window.location = "/View_Recipie" </script>'''

@app.route('/signup',methods=['post'])
def signup():
    First_Name=request.form['textfield']
    print(First_Name)

    Last_Name = request.form['textfield2']
    print(Last_Name)

    Adrress=request.form['textarea']
    print(Adrress)

    Gender = request.form['mm']
    print(Gender)

    Date_Of_Birth=request.form['textfield13']
    print(Date_Of_Birth)

    Phone_Number = request.form['textfield3']
    print(Phone_Number)

    E_Mail = request.form['textfield4']
    print(E_Mail)

    Level = request.form['RadioGroup2']
    print(Level)

    Set_Password = request.form['textfield5']
    print(Set_Password)

    Confirm_Password = request.form['textfield6']
    print(Confirm_Password)
    if(Set_Password==Confirm_Password):
        q="INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
        v=(E_Mail,Confirm_Password)
        id=iud(q,v)

        qry = "insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(id),First_Name,Adrress,Date_Of_Birth,Level,Phone_Number,Gender,Last_Name,E_Mail)
        iud(qry,val)
        return '''<script>alert("Successfully Sign In");window.location = "/" </script>'''
    else:
        return '''<script>alert("password doesn't match");window.location = "/" </script>'''



@app.route('/User_Home')
@login_required
def User_Home():
    return render_template('/User Home.html')

@app.route('/Search_Recipie')
@login_required
def Search_Recipie():
    return render_template('/Search Recipie.html',status='no')

@app.route('/fileupload_post',methods=['post'])
def fileupload_post():
    img = request.files['fileup']
    img.save("static/1.jpg")
    a = predct()
    print("aaaaaaaaaaa",a)

    recid = []
    for i in a.keys():
        re = selectall2("select * from `incredient_list` where `incredient`=%s",i)
        for ii in re:
            recid.append(ii['rid'])
    print([*set(recid)])


    recp = []
    reclist=[]
    # recid=[1,2,3]
    for ij in recid:
        if ij not in reclist:
            reclist.append(ij)
            ree = selectall2("select * from `recipie` where `Recipie_id`=%s", ij)
            print(ree)

            reciepe = {}
            for qq in ree:

                reciepe['Recipie_Name']=qq['Recipie_Name']
                reciepe['Recipie_Description']=qq['Recipie_Description']
                recp.append(reciepe)

    print(recp,"aaaaaaaaaaaaaaaaaaaa")

    # con = pymysql.connect(host='localhost', user='root', password='', port=3306, db='recipie')
    # cmd = con.cursor()
    #
    # for aa in a:
    #     cmd.execute("SELECT DISTINCT `incredient` FROM `incredient_list` ORDER BY `incredient`")
    #     s = cmd.fetchall()
    #     dsym = []
    #     for i in s:
    #         dsym.append(i[0])
    #     row = []
    #     for w in dsym:
    #         if w in aa:
    #             row.append(1)
    #         else:
    #             row.append(0)
    #
    #     print("aaaaaaa",row)

        # qry = "SELECT `diease` FROM `disease` WHERE id=%s"
        # res = selectone(qry, res)

    return render_template('/Search Recipie.html',data = a,status = 'ok',data1 = recp)



@app.route('/Add_Post')
@login_required
def Add_Post():
    return render_template('/Add Post.html')
class Secure_filename:
    pass


@app.route('/post',methods=['post'])
def post():
    Caption=request.form['textarea']
    print(Caption)
    img = request.files['Submit']
    image = secure_filename(img.filename)
    img.save(os.path.join('static/image',image))
    qry = "insert into post values(null,%s,%s,%s,curdate())"
    val = (session['lid'],Caption,image)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/User_Home" </script>'''

@app.route('/View_Tips')
@login_required
def View_Tips():
    qry = "SELECT * FROM tips"
    res = selectall(qry)
    return render_template('/View Tips.html',data=res)

@app.route('/Ask_Help')
@login_required
def Ask_Help():
    return render_template('/Ask Help.html')

@app.route('/help',methods=['post'])
def help():
    # id=request.args.get('User_id')
    Question=request.form['textarea']
    print(Question)
    qry = "INSERT INTO `help`VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val = (session['lid'],Question)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/User_Home" </script>'''

@app.route('/View_Reply')
@login_required
def View_Reply():
    qry = "SELECT * FROM help"
    res = selectall(qry)
    return render_template('/View Reply.html',data=res)

@app.route('/Feed_Back')
@login_required
def Feed_Back():
    return render_template('/Add Feedback.html')

@app.route('/feedback',methods=['post'])
def feedback():
    # id=request.args.get('User_id')
    Feedback=request.form['textfield']
    print(Feedback)
    Rating = request.form['textfield2']
    print(Rating)
    qry = "INSERT INTO `feedback`VALUES(NULL,%s,%s,%s,CURDATE())"
    val = (session['lid'],Feedback,Rating)
    iud(qry,val)
    return '''<script>alert("Successfully Added");window.location = "/User_Home" </script>'''

@app.route('/View_Post_User')
@login_required
def View_Post_User():
    qry = "SELECT `post`.*,`user`.`First_Name`,`Last_Name` FROM `user` JOIN `post` ON `user`.`Login_id`=`post`.`User_id`"
    res = selectall(qry)
    return render_template('/view post user.html', data=res)
    # return render_template('/view post user.html')

app.run(debug=True)