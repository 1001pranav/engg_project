from django.shortcuts import render
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
except (Exception, db.DatabaseError) as error:
        print(error)
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def login(request):
	if request.method=='post':
		name=request.post['name']
		password=request.post['password']
		types=request.post['type']

	else:
    		return render(request,'login.html')
def Home(request):
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['password']
        type=request.POST['type']
        if(type=='Faculty'):
            sql="""SELECT * FROM "Faculty" WHERE "Email"=%s and "Password"=%s"""
        else:
            sql="""SELECT * FROM "Parent" WHERE "Email"=%s and "Password"=%s"""
        try:
            cur.execute(sql,(name,password))
        except (Exception, db.DatabaseError) as error:
            result="""
                <div class='alert alert-danger'>
                Error in login Password or Username(Email) is Wrong or check wether checked correct field
                </div>
            """
            return render(request,'login.html',{'result':result})

        res=cur.fetchall()
        if(len(res)>0 and type=='Faculty'):
            return render(request,'faculty.html',{'name':res[0][1],'fid':res[0][0]})
        else:
            result="""
                    <div class='container alert alert-danger'>
                    <div class='row col-6 '>Error in login Password or Username(Email) is Wrong or check wether checked correct field</div>
                    </div>"""
            return render(request,'login.html',{'result':result})
