from django.shortcuts import render
import mysql.connector as sql
webname=''
ssh=''
balance=''

def credentials(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd=" ",database='subkripton')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                webname=value
            if key=="ssh":
                ssh=value
            if key=="balance":
                balance=value
        c="insert into USERINFOLST Values('{}','{}')".format(webname,ssh,balance)
        cursor.execute(c)
        m.commit()

    return render(request,'credentials.html')