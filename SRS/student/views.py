
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

# def logout_url(request) :
#         logout(request)
#         request.session.flush()
#         # request.user = AnonymousUser
#         return render(request, 'index.html')

def query_login_s(inp_u, inp_p):

    ch_u = '''         select "Student_ID","Student_Fname","Student_Lname","Student_email_ID","Student_phno" from "ELMS2"."Student" join "ELMS2"."Account"
                        on "ELMS2"."Student"."Student_ID" = "ELMS2"."Account"."Username"
                       where "Username" = ''' + inp_u +\
                        ''' and "Password" = ''' + "'" + inp_p  + "'" + '''and "Role" = 'Student' '''
    # do $$
    #                declare
    #                op_std "ELMS2"."Student"%rowtype;
    #                i "ELMS2"."Account"."Username"%type := ''' + inp_u + ''';
    #                p "ELMS2"."Account"."Password"%type := ''' + "'" + inp_p + "';" + '''
    #                begin
    #                    select * from "ELMS2"."Student"
    #                    into op_std
    #                    where "Student_ID" = i ;
    #
    #                    if not found then
    #                         raise notice'No any Student data of this Username % is available here ', i;
    #                    else
    #                         raise notice'
    #                                         Student ID - %,
    #                                         Name -   % %,
    #                                         Email id - %,
    #                                         Phone number - %   ', op_std."Student_ID",op_std."Student_Fname",op_std."Student_Lname",op_std."Student_email_ID",op_std."Student_phno";
    #                    end if;
    #
    #             end $$
    # '''
    cursor.execute(ch_u)
    # return connection.notices
    return cursor.fetchall()

def query_stdlout_result(inp_id,flg):
    if flg==1 :     #FOR QUIZ RESULT
        ch_u = '''select "Course_ID",cast("Marks" as varchar) from "ELMS2"."Quiz_student" where "Student_ID"=''' + inp_id
        cursor.execute(ch_u)
        # return connection.notices
        return cursor.fetchall()

    if flg==2:      #FOR ASSIGNMENT RESULT
        ch_u = '''select "Course_ID","Marks" from "ELMS2"."Assignment_student" where "Student_ID"=''' + inp_id
        cursor.execute(ch_u)
        # return connection.notices
        return cursor.fetchall()

    if flg==3:      #FOR EXAM RESULT
        ch_u = '''select "Course_ID","Marks" from "ELMS2"."Exam_student" where "Student_ID"=''' + inp_id
        cursor.execute(ch_u)
        # return connection.notices
        return cursor.fetchall()

    if flg==4:      #FOR CGPA / FINAL RESULT
        ch_u = '''SELECT cast("CGPA" as varchar) FROM "ELMS2"."Final_result" where "Student_ID"=''' + inp_id
        cursor.execute(ch_u)
        # return connection.notices
        return cursor.fetchall()

# --------------------------------------------------------------------------------------------------

# ***************************** student login page  ********************

# Student page login
def stdlg(request):
    # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
    #                     <a href="/"> back </a> ''')

    return render(request,'stdlg.html')

# Student page login output
def stdlgout(request):

    inp_u = request.POST.get('usr','default')
    inp_p = request.POST.get('psw','default')

     # if str(inp_u) not in '0123456789' or not (inp_u and inp_p) :
    if (not inp_u) or (not inp_p):
        # ans = {'notc_s': 'Enter Valid Username or Password'}
        messages.error(request,'Username or Password cannot be empty')
        return render(request, 'stdlg.html') #, ans)

    for c in inp_u:
        if c not in '0123456789':
            # ans = {'notc_s': 'Enter Valid Username or Password'}
            messages.error(request, 'Enter Valid Username. Username should contain only integers')
            return render(request, 'stdlg.html') #, ans)

    rows = query_login_s(inp_u, inp_p)

    if not rows :
        # ans = {'notc_s' : inp_u + ' is not valid Username or You have entered wrong Password'}
        messages.error(request, inp_u + ' is not valid Username or You have entered wrong Password')
        return render(request, 'stdlg.html')#, ans)

    r = rows[0]

    ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3]), 'phn':str(r[4]) }
    return render(request, 'stdlgout.html', ans)

# --------------------------------------------------------------------------------------------------


#----------------------   STUDENT OUTPUT PAGE FUNCTIONS :: -----------------------------------#

def _stdlgout_registeredcourse(request):

    flag_lec=0
    flag_note=0
    if request.method=='POST' and 'lec_link' in request.POST:
        flag_lec= 1
    if request.method == 'POST' and 'note_link' in request.POST:
        flag_note=1

    inp_u = request.GET.get('usr','default')
    rows_note=[]
    rows_lec=[]
    ch_u = '''select "Course"."Course_ID","Course_name" from "ELMS2"."Student_enroll_course" join "ELMS2"."Course"
    on "ELMS2"."Student_enroll_course"."Course_ID" = "ELMS2"."Course"."Course_ID"
    where "Student_ID" = ''' + inp_u
    cursor.execute(ch_u)
    # return connection.notices
    rows = cursor.fetchall()

    # flag=Lecture_Links_fun(request)
    if flag_note :
        _course_notes_ch_u=''' select "Material"."Course_ID","Notes" from "ELMS2"."Material" join "ELMS2"."Student_enroll_course"
            on "Material"."Course_ID"="Student_enroll_course"."Course_ID"
            where "Student_ID" = ''' + inp_u
        cursor.execute(_course_notes_ch_u)
        rows_note = cursor.fetchall()

    if flag_lec:
        _course_lec_ch_u=''' select "Material"."Course_ID","Lecture" from "ELMS2"."Material" join "ELMS2"."Student_enroll_course"
            on "Material"."Course_ID"="Student_enroll_course"."Course_ID"
            where "Student_ID" = ''' + inp_u
        cursor.execute(_course_lec_ch_u)
        rows_lec = cursor.fetchall()

    return render(request, '_stdlgout_registeredcourse.html', {'data':dict(rows),'course_note':dict(rows_note),'course_lec':dict(rows_lec), 'flag_lec':flag_lec, 'flag_note':flag_note})

def _stdlgout_marks(request):

    inp_u = request.GET.get('usr','default')
    rows1 = query_stdlout_result(inp_u,1)   # flg=1 for QUIZ
    rows2 = query_stdlout_result(inp_u,2)   # flg=2 for ASSIGNMENT
    rows3 = query_stdlout_result(inp_u,3)   # flg=3 for EXAM
    rows4 = query_stdlout_result(inp_u,4)   # flg=2 for FINAL/CGPA
    return render(request,'_stdlgout_marks.html',{'params_quiz':dict(rows1),'params_ass':dict(rows2),"params_exam":dict(rows3),"params_cgpa":str(rows4[0][0])})


# --------------------------------------------------------------------------------------------------
