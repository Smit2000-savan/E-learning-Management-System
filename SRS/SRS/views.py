# CREATED BY ME - SMIT

# WORK IN PROGRESS :
# # about page for the author
# #
#
# WORK TO DO :
# # search feature in student list in admin portal
# # search feature in prof list in admin portal
# # Forget Password mail in all login page
# # add prof feature in admin login
# # mail to new student mailid with info of its id,username and password after admin adds student
# # basic HTML template for all pages


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

import time
import pymonetdb
import psycopg2

# Supporting FUNCTIONS  ***********************************
connection = psycopg2.connect(host='localhost',
                                  database='SRS',
                                  user='postgres',
                                  password='admin')
cursor = connection.cursor()

def index(request):
    # return HttpResponse('''<H1>Hello</H1><a href="https://www.google.com/"> google </a> <br>
    #                     <a href="http://127.0.0.1:8000/about"> about page </a> ''')

    #     para = {'name':'Smit','place':'India'}
        return render(request, 'index.html') #, para)

def about(request):
    # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
    #                     <a href="/"> back </a> ''')
    return render(request,'about.html')

#
# def stdlg(request):
#     # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
#     #                     <a href="/"> back </a> ''')
#
#     return render(request,'stdlg.html')
#
# def proflg(request):
#     # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
#     #                     <a href="/"> back </a> ''')
#
#     return render(request,'proflg.html')
#
# def admlg(request):
#     # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
#     #                     <a href="/"> back </a> ''')
#     return render(request,'admlg.html')

#
# def stdlgout(request):
#
#     inp_u = request.POST.get('usr','default')
#     inp_p = request.POST.get('psw','default')
#
#      # if str(inp_u) not in '0123456789' or not (inp_u and inp_p) :
#     if (not inp_u) or (not inp_p):
#         # ans = {'notc_s': 'Enter Valid Username or Password'}
#         messages.error(request,'Username or Password cannot be empty')
#         return render(request, 'stdlg.html') #, ans)
#
#     for c in inp_u:
#         if c not in '0123456789':
#             # ans = {'notc_s': 'Enter Valid Username or Password'}
#             messages.error(request, 'Enter Valid Username. Username should contain only integers')
#             return render(request, 'stdlg.html') #, ans)
#
#     rows = query_login_s(inp_u, inp_p)
#
#     if not rows :
#         # ans = {'notc_s' : inp_u + ' is not valid Username or You have entered wrong Password'}
#         messages.error(request, inp_u + ' is not valid Username or You have entered wrong Password')
#         return render(request, 'stdlg.html')#, ans)
#
#     r = rows[0]
#
#     ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3]), 'phn':str(r[4]) }
#     return render(request, 'stdlgout.html', ans)

# def proflgout(request):
#
#     inp_u = request.POST.get('usr','default')
#     inp_p = request.POST.get('psw','default')
#
#     if (not inp_u) or (not inp_p):
#         ans = {'notc_p': 'Enter Valid Username or Password'}
#         return render(request, 'proflg.html', ans)
#
#     for c in inp_u:
#         if c not in '0123456789':
#             ans = {'notc_p': 'Enter Valid Username or Password'}
#             return render(request, 'proflg.html', ans)
#
#     rows = query_login_p(inp_u, inp_p)
#     if not rows :
#         ans = {'notc_p': inp_u + ' is not valid Username or You have entered wrong Password'}
#         return render(request, 'proflg.html', ans)
#
#     r = rows[0]
#     ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3]), 'phn':str(r[4]), 'cid':str(r[5]) }
#     return render(request, 'proflgout.html', ans)

#
# def admlgout(request):
#
#     inp_u = request.POST.get('usr','default')
#     inp_p = request.POST.get('psw','default')
#
#     if (not inp_u) or (not inp_p):
#         ans = {'notc_a': 'Enter Valid Username or Password'}
#         return render(request, 'admlg.html', ans)
#
#     for c in inp_u:
#         if c not in '0123456789':
#             ans = {'notc_a': 'Enter Valid Username or Password'}
#             return render(request, 'admlg.html', ans)
#
#     rows = query_login_a(inp_u, inp_p)
#     if not rows :
#         ans = {'notc_a': inp_u + ' is not valid Username or You have entered wrong Password'}
#         return render(request, 'admlg.html', ans)
#
#     r = rows[0]
#     ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3])}
#     return render(request, 'admlgout.html', ans)

def signup(request):
    return render(request,'signup.html')

#----------------------   STUDENT OUTPUT PAGE FUNCTIONS :: -----------------------------------#
#
# def _stdlgout_registeredcourse(request):
#
#     flag_lec=0
#     flag_note=0
#     if request.method=='POST' and 'lec_link' in request.POST:
#         flag_lec= 1
#     if request.method == 'POST' and 'note_link' in request.POST:
#         flag_note=1
#
#     inp_u = request.GET.get('usr','default')
#     rows_note=[]
#     rows_lec=[]
#     ch_u = '''select "Course"."Course_ID","Course_name" from "ELMS2"."Student_enroll_course" join "ELMS2"."Course"
#     on "ELMS2"."Student_enroll_course"."Course_ID" = "ELMS2"."Course"."Course_ID"
#     where "Student_ID" = ''' + inp_u
#     cursor.execute(ch_u)
#     # return connection.notices
#     rows = cursor.fetchall()
#
#     # flag=Lecture_Links_fun(request)
#     if flag_note :
#         _course_notes_ch_u=''' select "Material"."Course_ID","Notes" from "ELMS2"."Material" join "ELMS2"."Student_enroll_course"
#             on "Material"."Course_ID"="Student_enroll_course"."Course_ID"
#             where "Student_ID" = ''' + inp_u
#         cursor.execute(_course_notes_ch_u)
#         rows_note = cursor.fetchall()
#
#     if flag_lec:
#         _course_lec_ch_u=''' select "Material"."Course_ID","Lecture" from "ELMS2"."Material" join "ELMS2"."Student_enroll_course"
#             on "Material"."Course_ID"="Student_enroll_course"."Course_ID"
#             where "Student_ID" = ''' + inp_u
#         cursor.execute(_course_lec_ch_u)
#         rows_lec = cursor.fetchall()
#
#     return render(request, '_stdlgout_registeredcourse.html', {'data':dict(rows),'course_note':dict(rows_note),'course_lec':dict(rows_lec), 'flag_lec':flag_lec, 'flag_note':flag_note})
#
# def _stdlgout_marks(request):
#
#     inp_u = request.GET.get('usr','default')
#     rows1 = query_stdlout_result(inp_u,1)   # flg=1 for QUIZ
#     rows2 = query_stdlout_result(inp_u,2)   # flg=2 for ASSIGNMENT
#     rows3 = query_stdlout_result(inp_u,3)   # flg=3 for EXAM
#     rows4 = query_stdlout_result(inp_u,4)   # flg=2 for FINAL/CGPA
#     return render(request,'_stdlgout_marks.html',{'params_quiz':dict(rows1),'params_ass':dict(rows2),"params_exam":dict(rows3),"params_cgpa":str(rows4[0][0])})

# ----------------------   ADMIN OUTPUT PAGE FUNCTIONS :: -----------------------------------#
# def _admlgout_addstudent(request):
#
#     inp_fn = request.POST.get('fname','default')
#     inp_ln = request.POST.get('lname','default')
#     inp_ph = request.POST.get('phn')
#
#     # showing course names in checkbox
#     ch_course = ''' select "Course_ID","Course_name","Course_credit" from "ELMS2"."Course" '''
#     cursor.execute(ch_course)
#     data_course = cursor.fetchall()
#
#     course_code=[]
#     for i in data_course:
#         course_code.append(request.POST.get(str(i[0]),''))
#
#     # print(course_code)
#     if inp_ph == None:
#         return render(request, '_admlgout_addstudent.html', {'course_dict':data_course})
#
#     if not(inp_fn) or not(inp_ln) or not(inp_ph) or (not(course_code[0]) and not(course_code[1]) and not(course_code[2]) and not(course_code[3]) and not(course_code[4]) and not(course_code[5]) ):
#         return render(request, '_admlgout_addstudent.html', {'notc_ads': "Fill the details. All Fields are mandatory", 'course_dict':data_course})
#
#     ch_id = ''' select "Student_ID" from "ELMS2"."Student" order by "Student_ID" DESC limit 1 '''
#     cursor.execute(ch_id)
#     data=cursor.fetchall()
#     new_id = data[0][0] +1
#
#     ch = ''' INSERT INTO "ELMS2"."Student"(
# 	"Student_ID", "Student_Fname", "Student_Lname", "Student_email_ID", "Student_phno")
# 	VALUES (''' + str(new_id) + ", '" + inp_fn + "', '" + inp_ln + "', '" + "{}@daiict.ac.in".format(new_id) + "',"  + inp_ph + '''); '''
#     cursor.execute(ch)
#     # row = connection.notices
#     # rows = cursor.fetchall()
#     connection.commit()
#
#     ch_pass=''' select "Password" from "ELMS2"."Account" where "Username"=''' + str(new_id)
#     cursor.execute(ch_pass)
#     data2 = cursor.fetchall()
#     new_pass = data2[0][0]
#
#     ch_std_enroll_course = ''' select "ELMS2".insert_into_student_enroll_course( array[ '''
#     num = 1
#     for i in course_code:
#         if i != '':
#             ch_std_enroll_course = ch_std_enroll_course + '''(''' + str(num) + ''',''' + str(new_id) +  ",'" + i + "'),"
#             num=num+1
#     ch_std_enroll_course = ch_std_enroll_course.rstrip(ch_std_enroll_course[-1])
#     ch_std_enroll_course = ch_std_enroll_course + ''']::"ELMS2".order_input[]); '''
#
#     cursor.execute(ch_std_enroll_course)
#     connection.commit()
#
#     return render(request, '_admlgout_addstudent.html', {'notc_ads':'data entered successfully.', 'notc_id': 'Student data Submitted with new student id : {}'.format(new_id), 'notc_ps': 'And it has password : {}'.format(new_pass)})
#
# def _admlgout_studentlist(request):
#
#     ch=''' select "Student_ID","Student_Fname","Student_Lname" from "ELMS2"."Student" '''
#     cursor.execute(ch)
#     rows=cursor.fetchall()
#
#     d = {}
#     for i in rows:
#         d[i[0]]=str(i[1]+ " " + i[2])
#
#     return render(request,'_admlgout_studentlist.html',{'data':d})
#
# def _admlgout_proflist(request):
#
#     ch=''' select "Prof_ID","Prof_Fname","Prof_Lname","Course_ID" from "ELMS2"."Professor" '''
#     cursor.execute(ch)
#     rows=cursor.fetchall()
#
#     d = {}
#     for i in rows:
#         d[i[0]] = tuple(i[1:])
#
#     return render(request,'_admlgout_proflist.html',{'data':d})
#
















# --------------------------------------------------------------------------------------
# def query_login(inp_u, inp_p):
#     connection = psycopg2.connect(host='localhost', database='SRS', user='postgres', password='admin')
#     cursor = connection.cursor()
#
#     ch_u = '''
#
#             do $$
#                    declare
#                    tmp "ELMS2"."Account"%rowtype;
#                    i "ELMS2"."Account"."Username"%type := ''' + inp_u + ''';
#                    p "ELMS2"."Account"."Password"%type := ''' + "'" + inp_p + "';" + '''
#                    begin
#                        select * from "ELMS2"."Account"
#                        into tmp
#                        where "Username" = i and "Password"=p ;
#
#                        if not found then
#                             raise notice'The Username % could not be found', i;
#                        else
#                             if tmp."Role" = 'Student' then
#                                 raise notice'1';
#                             elseif tmp."Role" = 'Professor' then
#                                 raise notice'2';
#                             else
#                                 raise notice'3';
#                        end if;
#                   end if;
#             end $$
#     '''
#     cursor.execute(ch_u)
#     return connection.notices

# ---------------------------------------------------------------------
# import time
# import pymonetdb
# import psycopg2
#
# connection = psycopg2.connect(host="localhost", database="SRS", user="postgres", password="admin")
#
# cursor = connection.cursor()
# cursor.execute('SELECT version()')
#
# db_version = cursor.fetchone()
# print(db_version)
#
# def fun(request):
#     ch = "select * from \"ELMS2\".\"Professor\" "
#     cursor.execute(ch)
#     rows = cursor.fetchall()
#     return HttpResponse(rows)
#     # for r in rows:
#     #     print("ID - ", r[1],r[0])
#
# # print(len(rows[0]))       # shows number of columns  and len(rows) shows number of entries in table

# ------------------------------------------------
# import time
# import pymonetdb
# import psycopg2
#
# connection = psycopg2.connect(host='localhost',
#                                             database='Lab_201901086',
#                                             user='postgres',
#                                             password='admin')
# cursor = connection.cursor()
#
#
# query = " select\"Student_Fname\",\"Student_Lname\",g1.id,g1.assignment,g1.quiz" \
#        " from \"ELMS2\".\"Student\","\
#        " (select \"Quiz_student\".\"Student_ID\" as id,\"Assignment_student\".\"Marks\" as assignment, \"Quiz_student\".\"Marks\" as quiz" \
#        " from \"ELMS2\".\"Assignment_student\" join \"ELMS2\".\"Quiz_student\"" \
#        " on \"ELMS2\".\"Assignment_student\".\"Student_ID\" = \"ELMS2\".\"Quiz_student\".\"Student_ID\" " \
#        " where \"ELMS2\".\"Assignment_student\".\"Student_ID\" = '201901039' and  \"Assignment_student\".\"Course_ID\"='CS309' and \"Quiz_student\".\"Course_ID\"='CS309') as g1" \
#        " where \"ELMS2\".\"Student\".\"Student_ID\" = g1.id "
#
# cursor.execute(query)
# data = cursor.fetchall()
# print(data)
# # --------------------------------------------------------
# inp_u = input("Enter your Username :")
# inp_p = input("Enter your Password :")
#
# ch_u = "do $$ " \
#       "declare " \
#       "tmp \"ELMS2\".\"Account\"%rowtype; " \
#       "i \"ELMS2\".\"Account\".\"Username\"%type :=" + inp_u + ";" \
#       "p \"ELMS2\".\"Account\".\"Password\"%type := '" + inp_p + "';" \
#       "begin " \
#       "select * from \"ELMS2\".\"Account\" " \
#       "  into tmp " \
#       "  where \"Username\" = i and \"Password\" = p ; " \
#       "  if not found then " \
#       "raise notice'The User % Does not exist', i; " \
#       "else " \
#       "raise notice'This account is a % account', tmp.\"Role\"; " \
#       "  end if; " \
#       "end $$ "
# cursor.execute(ch_u)
# for notice in connection.notices:
#    print(notice)

