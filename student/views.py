from django.shortcuts import render
from django.http import HttpResponse
import psycopg2 as db

try:
    conn= conn=db.connect(
        host='localhost',
        database="Student",
        user='postgres',
        password='1234',
        port='6000'
    )
    cur=conn.cursor()
    curs=conn.cursor()
except (Exception, db.DatabaseError) as error:
    print(error)
success=""
suc,er=False,False
def search(request):

    res=[]
    if request.method=="POST":
        usn=request.POST['usn']

        name=request.POST['fname']
        fid=request.POST['fid']
        sql="""SELECT * from "Students","Parent" WHERE "Students"."USN" LIKE (%s) AND "Students"."USN"="Parent"."USN" AND "Parent"."USN" LIKE (%s) """
        error=" "
        try:
            cur.execute(sql,(usn,usn))
            rest=cur.fetchall()
            result=""
            res=[]
            if(len(rest)>=1):
                suc=True
                er=False
                res=rest[0]
                result={}
            else:
                er=True
                suc=False
            ers ="Coudnt Find the USN"

        except (Exception, db.DatabaseError) as error:
            er=True
            suc=False
            ers=error
        if er:
            for i in range(0,12):
                res.append(i)
            result="""<div class='container alert alert-danger'><div class='row col-6 '>""",ers,"""</div></div>"""
        return (render(request,"faculty.html",{"name":name,"fid":fid,"sus":suc,"error":er,"result":result,"usn":res[0],"sname":res[1],"sem":res[2],"year":res[3],"email":res[4],"sphone":res[6],"pphone":res[8],"pname":res[9],"pemail":res[10],"padd":res[11]}))
def Dispstd(request):
    if request.method=='GET':
        fid=int(request.GET['fid'])
        name=request.GET['name']
        sql="""SELECT "USN","Name" from "Students" WHERE "FId"=%s"""
        cur.execute(sql,(fid,))
        res=cur.fetchall()
        div=""
        rest=False

        if(len(res)>=1):
            rest=True
            return render(request,'faculty.html',{"rest":rest,"fid":fid,'name':name,"results":res})




def Addstud(request):
    met=request.POST
    if request.method=="POST":
        fid=int(met['fid'])
        usn=met['usn']
        name=met['fname']
        sname=met['name']
        brn=met['brn']
        year=int(met['year'])
        sem=int(met['sem'])
        smob=int(met['smob'])
        add=met['Add']
        pname=met['pname']
        mob=int(met['mob'])
        email=met['email']
        pas=met['pass']
        sqls="""INSERT INTO "Students" VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        sqlp="""INSERT INTO "Parent" VALUES (%s,%s,%s,%s,%s,%s)"""
        try:
            cur.execute(sqls,(usn,sname,sem,year,email,fid,smob))
            curs.execute(sqlp,(usn,mob,pname,email,add,pas))
            er=""
            success="""
                    <div class='container alert alert-success'>
                    <div class='row col-6 '>
                    Success Added Data
                    </div>
                    </div>
            """
            conn.commit()

        except (Exception, db.DatabaseError) as error:
            success="""
                    <div class='container alert alert-danger'>
                    <div class='row col-6 '>
                    Coudn't add due to an error
                    </div>
                    </div>
            """,error
        return render(request,'faculty.html',{"success":success,"name":name,"fid":fid})
def showsub(request):
    subshow=False
    if request.method=="GET":
        name=request.GET['name']
        fid=request.GET['fid']
        sql="""SELECT * FROM "Subject" """

        try:
            subshow=True
            cur.execute(sql)
            res=cur.fetchall()

        except (Exception, db.DatabaseError) as error:
            success="""
                    <div class='container alert alert-danger'>
                    <div class='row col-6 '>
                    There was an error
                    </div>
                    </div>
            """,error
        else: success="""
                <div class='container alert alert-danger'>
                <div class='row col-6 '>
                There was an error you where at wrong place
                </div>
                </div>
        """
    return render(request,'faculty.html',{"subshow":subshow,"name":name,"fid":fid,"res":res})
