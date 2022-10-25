from django.shortcuts import render
import mysql.connector as sql
n=''
uname=''
em=''
pwd=''
phone=''
adhaar=''


# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='subkripton')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                n=value
            if key=="username":
                uname=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="phone":
                phone=value
            if key=="adhaar":
                adhaar=value

        c="insert into USERINFOLST Values('{}','{}','{}','{}','{}')".format(n,uname,em,pwd,phone,adhaar)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')