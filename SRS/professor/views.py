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

def query_login_p(inp_u, inp_p):
    connection = psycopg2.connect(host='localhost', database='SRS', user='postgres', password='admin')
    cursor = connection.cursor()

    ch_u = '''         select "Prof_ID","Prof_Fname","Prof_Lname","Prof_email_ID","Prof_phno","Course_ID" from "ELMS2"."Professor" join "ELMS2"."Account"
                        on "ELMS2"."Professor"."Prof_ID" = "ELMS2"."Account"."Username"
                       where "Username" = ''' + inp_u +\
                        '''and "Password" = ''' + "'" + inp_p  + "'" + '''and "Role" = 'Professor' '''

    cursor.execute(ch_u)
    # return connection.notices
    return cursor.fetchall()

# --------------------------------------------------------------------------------------------------

# ***************************** Prof login page  ********************

def proflg(request):
    # return HttpResponse('''<H1>This is about page </H1> <a href="http://127.0.0.1:8000/">home </a> <br>
    #                     <a href="/"> back </a> ''')

    return render(request,'proflg.html')

def proflgout(request):

    inp_u = request.POST.get('usr','default')
    inp_p = request.POST.get('psw','default')

    if (not inp_u) or (not inp_p):
        ans = {'notc_p': 'Enter Valid Username or Password'}
        return render(request, 'proflg.html', ans)

    for c in inp_u:
        if c not in '0123456789':
            ans = {'notc_p': 'Enter Valid Username or Password'}
            return render(request, 'proflg.html', ans)

    rows = query_login_p(inp_u, inp_p)
    if not rows :
        ans = {'notc_p': inp_u + ' is not valid Username or You have entered wrong Password'}
        return render(request, 'proflg.html', ans)

    r = rows[0]
    ans = {'id':str(r[0]), 'name':str(r[1])+' '+str(r[2]), 'email':str(r[3]), 'phn':str(r[4]), 'cid':str(r[5]) }
    return render(request, 'proflgout.html', ans)

# --------------------------------------------------------------------------------------------------

