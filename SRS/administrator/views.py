
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time
import pymonetdb
import psycopg2

# Create your views here.

# Supporting FUNCTIONS  ***********************************
connection = psycopg2.connect(host='localhost',
                                  database='SRS',
                                  user='postgres',
                                  password='admin')
cursor = connection.cursor()

def query_login_a(inp_u, inp_p):

    ch_u = '''         select "Admin_ID","Admin_Fname","Admin_Lname","Admin_email_ID" from "ELMS2"."Administrator" join "ELMS2"."Account"
                        on "ELMS2"."Administrator"."Admin_ID" = "ELMS2"."Account"."Username"
                       where "Username" = ''' + inp_u +\
                        ''' and "Password" = ''' + "'" + inp_p  + "'" + '''and "Role" = 'Administrator' '''
    cursor.execute(ch_u)
    # return connection.notices
    return cursor.fetchall()

# --------------------------------------------------------------------------------------------------

# ***************************** admin login page  ********************

def admlg(request):
    # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
    #                     <a href="/"> back </a> ''')
    return render(request,'admlg.html')

def admlgout(request):

    inp_u = request.POST.get('usr','default')
    inp_p = request.POST.get('psw','default')

    if (not inp_u) or (not inp_p):
        ans = {'notc_a': 'Enter Valid Username or Password'}
        return render(request, 'admlg.html', ans)

    for c in inp_u:
        if c not in '0123456789':
            ans = {'notc_a': 'Enter Valid Username or Password'}
            return render(request, 'admlg.html', ans)

    rows = query_login_a(inp_u, inp_p)
    if not rows :
        ans = {'notc_a': inp_u + ' is not valid Username or You have entered wrong Password'}
        return render(request, 'admlg.html', ans)

    r = rows[0]
    ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3])}
    return render(request, 'admlgout.html', ans)

# --------------------------------------------------------------------------------------------------

# ----------------------   ADMIN OUTPUT PAGE FUNCTIONS :: -----------------------------------#
def _admlgout_addstudent(request):

    inp_fn = request.POST.get('fname','default')
    inp_ln = request.POST.get('lname','default')
    inp_ph = request.POST.get('phn')

    # showing course names in checkbox
    ch_course = ''' select "Course_ID","Course_name","Course_credit" from "ELMS2"."Course" '''
    cursor.execute(ch_course)
    data_course = cursor.fetchall()

    course_code=[]
    for i in data_course:
        course_code.append(request.POST.get(str(i[0]),''))

    # print(course_code)
    if inp_ph == None:
        return render(request, '_admlgout_addstudent.html', {'course_dict':data_course})

    if not(inp_fn) or not(inp_ln) or not(inp_ph) or (not(course_code[0]) and not(course_code[1]) and not(course_code[2]) and not(course_code[3]) and not(course_code[4]) and not(course_code[5]) ):
        return render(request, '_admlgout_addstudent.html', {'notc_ads': "Fill the details. All Fields are mandatory", 'course_dict':data_course})

    ch_id = ''' select "Student_ID" from "ELMS2"."Student" order by "Student_ID" DESC limit 1 '''
    cursor.execute(ch_id)
    data=cursor.fetchall()
    new_id = data[0][0] +1

    ch = ''' INSERT INTO "ELMS2"."Student"(
	"Student_ID", "Student_Fname", "Student_Lname", "Student_email_ID", "Student_phno")
	VALUES (''' + str(new_id) + ", '" + inp_fn + "', '" + inp_ln + "', '" + "{}@daiict.ac.in".format(new_id) + "',"  + inp_ph + '''); '''
    cursor.execute(ch)
    # row = connection.notices
    # rows = cursor.fetchall()
    connection.commit()

    ch_pass=''' select "Password" from "ELMS2"."Account" where "Username"=''' + str(new_id)
    cursor.execute(ch_pass)
    data2 = cursor.fetchall()
    new_pass = data2[0][0]

    ch_std_enroll_course = ''' select "ELMS2".insert_into_student_enroll_course( array[ '''
    num = 1
    for i in course_code:
        if i != '':
            ch_std_enroll_course = ch_std_enroll_course + '''(''' + str(num) + ''',''' + str(new_id) +  ",'" + i + "'),"
            num=num+1
    ch_std_enroll_course = ch_std_enroll_course.rstrip(ch_std_enroll_course[-1])
    ch_std_enroll_course = ch_std_enroll_course + ''']::"ELMS2".order_input[]); '''

    cursor.execute(ch_std_enroll_course)
    connection.commit()

    return render(request, '_admlgout_addstudent.html', {'notc_ads':'data entered successfully.', 'notc_id': 'Student data Submitted with new student id : {}'.format(new_id), 'notc_ps': 'And it has password : {}'.format(new_pass)})

def _admlgout_studentlist(request):

    ch=''' select "Student_ID","Student_Fname","Student_Lname" from "ELMS2"."Student" '''
    cursor.execute(ch)
    rows=cursor.fetchall()

    d = {}
    for i in rows:
        d[i[0]]=str(i[1]+ " " + i[2])

    return render(request,'_admlgout_studentlist.html',{'data':d})

def _admlgout_proflist(request):

    ch=''' select "Prof_ID","Prof_Fname","Prof_Lname","Course_ID" from "ELMS2"."Professor" '''
    cursor.execute(ch)
    rows=cursor.fetchall()

    d = {}
    for i in rows:
        d[i[0]] = tuple(i[1:])

    return render(request,'_admlgout_proflist.html',{'data':d})

