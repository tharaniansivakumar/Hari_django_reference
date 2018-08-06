
import urllib, json, uuid
from io import BytesIO

from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import get_authorization_header

from models import Workout, File, Products, Phone, Lap, dateSample, userDetails, parent, child, manyparent, manychild,csvData
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response,HttpRequest
from django.template import Context, loader
from django.shortcuts import render_to_response

from rest_framework.decorators import api_view
from datetime import date, time, datetime
from django.core.files.storage import FileSystemStorage
import sys, requests
from myproject.settings import SALT_KEY, PROJECT_ROOT
import jwt
from workout import Authenticate
from django.shortcuts import redirect
from rest_framework import HTTP_HEADER_ENCODING
from workout import tok_det
import background_task
from background_task import background
import os,time
import csv ,reportlab
from reportlab.pdfgen import canvas

from workout.tasks import add, ml


def token_value(request):
    auth = request.META.get('HTTP_AUTHORIZATION')
    token = auth.split()
    payload = dict(jwt.decode(token[1], "SECRET_KEY"))
    return payload

def keynotfound(v):
    dic = {}
    dic["message"] = "content not found"
    dic["status"] = 400
    dic['key'] = v
    return dic


def successInsert(li):
    dic = {}
    dic['status'] = 201
    dic['message'] = "Record Inserted"
    li.append(dic)
    return li


#################################################  POST   ##################################################3


@api_view(['POST', 'DELETE', 'PUT'])
def delete(request):
    js = json.loads(request.body)
    if (js.has_key('name') == False):
        return JsonResponse({"status": 400, "message": "Empty String"}, status=400)

    if (Workout.objects.filter(name=js['name'])):
        Workout.objects.filter(name=js['name']).delete()
        dic = {}
        dic['status'] = 200
        dic['message'] = "Record Deleted"
        return JsonResponse(dic, status=200)
    else:
        dic = {}
        dic['status'] = 404
        dic['message'] = "Record Not Found"
        return JsonResponse(dic, status=404)


def indexCreate(request):
    s = set()
    s.add("name")
    s.add("age")
    s.add("dish")
    js2 = list(json.loads(request.body))
    for js in js2:
        js = dict(js)
        s1 = js.keys()
        s1 = set(s1)
        s2 = s - s1
        res = list(Workout.objects.filter(name=js['name']).values())

        ##################    For UPDATING the content and REJECTING if ALREADY FOUND    ##########################3

        if (len(res) != 0 and len(js) == 3):
            js1 = dict(res[0])
            js['id'] = js1['id']
            if (cmp(js, js1) == 0):
                dic = {}
                dic['message'] = "Content already Found"
                return JsonResponse(dic)
            else:
                Workout.objects.filter(id=js['id']).update(age=js['age'], dish=js['dish'])
                dic = {}
                dic['message'] = "Content updated"
                return JsonResponse(dic, status=200)

        '''if(js.has_key('name')==False or  js.has_key('dish')==False or ja.has_key('age')==False):
            dic={}
            dic['message']="Contents Missing"
            return JsonResponse(dic,status=400)'''

        ####################        Finding the MISSING PARAMETERS           ##############################
        if (len(s2) != 0):
            dic = {}
            ans = ""
            for i in s2:
                ans += i + " "
            dic['message'] = ans + "Missing"
            return JsonResponse(dic, status=400)

        # All Conditions SATISFIED

        ob = Workout(name=js['name'], age=js['age'], dish=js['dish'])
        ob.save()

    return JsonResponse(successInsert(js2), status=201, safe=False)


############################################# Splitting the values from Response to know the unleft fields####################################33

def verify(request):
    js = json.loads(request.body)
    st = js['message']
    st = str(st)
    li = st.split(' ')
    ans = ""
    for i in range(0, len(li) - 1):
        ans += li[i] + "  "
    ans += " are missing"
    return HttpResponse(ans, status=400)


def fileRead(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ob = File(path="/home/divum/Desktop/django/myproject" + uploaded_file_url)
        ob.save()
        dic = {}
        dic['status'] = 200
        dic['message'] = "File Stored"
        dic['url'] = "/home/divum/Desktop/django/myproject" + uploaded_file_url
        return JsonResponse(dic, status=200)


def imageRes(request):
    js = json.loads(request.body)
    nm = js['name']
    res = list(File.objects.filter(path__icontains=nm).values())
    if (len(res) != 0):
        source = res[0]['path']
        html = "<img src='" + source + "' alt='Problem'>"
        return HttpResponse(source)


def userdet(request):
    js = json.loads(request.body)
    if (js["status"] == "ins"):
        ud = userDetails()
        ud.username = js["un"]
        ud.password = make_password(js["pw"], salt=SALT_KEY)
        ud.save()
        msg = "created"
    else:
        if (userDetails.objects.filter(username=js["un"], password=make_password(js["pw"], salt=SALT_KEY))):
            msg = "Checked"
            request.session["username"] = js["un"]
        else:
            msg = "Failed"
    return HttpResponse(msg)


#######################################################################  GET  ####################################################3


@api_view(['POST', 'GET'])
def index(request):
    idval = request.GET.get('id')
    js = list(Workout.objects.filter(id=idval).values())
    if len(js) == 0:
        return JsonResponse(keynotfound(idval), status=400, safe=True)

    return JsonResponse(js, safe=False)


def indexId(request):
    idval = int(request.GET.get('id'))
    js = list(Workout.objects.filter(id__gt=idval - 1).values())
    #request.session["id"]=1
    if len(js) == 0:
        return JsonResponse(keynotfound(idval), status=400, safe=True)

    return JsonResponse(js, safe=False)


def indexDish(request):
    idval = request.GET.get('dish')
    js = list(Workout.objects.filter(dish__startswith=idval).values())
    if len(js) == 0:
        return JsonResponse(keynotfound(idval), status=400, safe=True)

    return JsonResponse(js, safe=False)


def indexAll(request, id=None, attr=None):
    req_dic = json.loads(request.body)
    if (id == None and attr == None):
        js = list(
            Workout.objects.filter(id__gt=3).order_by('-' + req_dic[0]['sort']).values('name', 'dish', 'id', 'age'))
        return JsonResponse(js, safe=False)
    if (attr == None):
        js = list(Workout.objects.filter(id=id).values())
        return JsonResponse(js, safe=False)
    else:
        js = list(Workout.objects.filter(id=id).values(attr))
        return JsonResponse(js, safe=False)


def orderid(request):
    js = json.loads(request.body)
    if (js['cancel'] == "true"):
        dateSample.objects.filter(order_id=js['id']).update(cancel_date=datetime.now())
        return HttpResponse("updated")
    ob = dateSample(order_id=js['id'])
    ob.save()
    return HttpResponse("Inserted")


def product(request, name=None, id=None):
    js = json.loads(request.body)
    sb = js[0]['sort_brand']
    splh = js[0]['sort_price_ltoh']
    sphl = js[0]['sort_price_htol']
    sn = js[0]['sort_newest']
    fb = js[1]['filter_brand']
    fpa = js[1]['filter_price_above']
    fpb = js[1]['filter_price_below']
    price_order = ""
    id_order = "id"
    if (splh == "true"):
        price_order = "asc"
    if (sphl == "true"):
        price_order = "desc"
    if (sn == "true"):
        id_order = '-' + "id"
    if (name == None and id == None):
        js = list(Products.objects.values())
        return JsonResponse(js, safe=False)
    if (fb == "null"):
        fb = ""
    if (fpa == "null"):
        fpa = 0
    if (fpb == "null"):
        fpb = sys.maxint
    if (name == "phone"):
        if (id == None):
            if (sb == "true"):
                if (price_order == "asc"):
                    js = list(Phone.objects.filter(ph_brand__icontains=fb, ph_price__gt=fpa, ph_price__lt=fpb).order_by(
                        "ph_brand", id_order).values('ph_brand', 'ph_name', 'ph_price'))
                    return JsonResponse(js, safe=False)
                else:
                    js = list(Phone.objects.filter(ph_brand__icontains=fb, ph_price__gt=fpa, ph_price__lt=fpb).order_by(
                        "ph_brand", '-' + "ph_price", id_order).values('ph_brand', 'ph_name', 'ph_price'))
                    return JsonResponse(js, safe=False)
            if (price_order == "asc"):
                js = list(Phone.objects.filter(ph_brand__icontains=fb, ph_price__gt=fpa, ph_price__lt=fpb).order_by(
                    "ph_price", id_order).values('ph_brand', 'ph_name', 'ph_price'))
                return JsonResponse(js, safe=False)
            if (price_order == "desc"):
                js = list(Phone.objects.filter(ph_brand__icontains=fb, ph_price__gt=fpa, ph_price__lt=fpb).order_by(
                    '-' + "ph_price", id_order).values('ph_brand', 'ph_name', 'ph_price'))
                return JsonResponse(js, safe=False)
            else:
                js = list(Phone.objects.filter(ph_brand__icontains=fb, ph_price__gt=fpa, ph_price__lt=fpb).order_by(
                    id_order).values('ph_brand', 'ph_name', 'ph_price'))
                return JsonResponse(js, safe=False)
        else:
            js = list(Phone.objects.filter(id=id).order_by(id_order).values())
            return JsonResponse(js, safe=False)
    if (name == "lap"):
        if (id == None):
            if (sb == "true"):
                if (price_order == "asc"):
                    js = list(Lap.objects.filter(lp_brand__icontains=fb, lp_price__gt=fpa, lp_price__lt=fpb).order_by(
                        "lp_brand", id_order).values('lp_brand', 'lp_name', 'lp_price'))
                    return JsonResponse(js, safe=False)
                else:
                    js = list(Lap.objects.filter(lp_brand__icontains=fb, lp_price__gt=fpa, lp_price__lt=fpb).order_by(
                        "lp_brand", '-' + "lp_price", id_order).values('lp_brand', 'lp_name', 'lp_price'))
                    return JsonResponse(js, safe=False)
            if (price_order == "asc"):
                js = list(Lap.objects.filter(lp_brand__icontains=fb, lp_price__gt=fpa, lp_price__lt=fpb).order_by(
                    "lp_price", id_order).values('lp_brand', 'lp_name', 'lp_price'))
                return JsonResponse(js, safe=False)
            if (price_order == "desc"):
                js = list(Lap.objects.filter(lp_brand__icontains=fb, lp_price__gt=fpa, lp_price__lt=fpb).order_by(
                    '-' + "lp_price", id_order).values('lp_brand', 'lp_name', 'lp_price'))
                return JsonResponse(js, safe=False)
            else:
                js = list(
                    Lap.objects.filter(lp_brand__icontains=fb, lp_price__gt=fpa, lp_price__lt=fpb).order_by(
                        id_order).values('lp_brand', 'lp_name', 'lp_price'))
                return JsonResponse(js, safe=False)
        else:
            js = list(Lap.objects.filter(id=id).values())
            return JsonResponse(js, safe=False)




def showcolor(request):
    try:
        if (request.session["username"] == "muths"):
            # del request.session["uname"]
            if "favorite_color" in request.COOKIES:
                return HttpResponse("Your favorite color is %s" % \
                                    request.COOKIES["favorite_color"])
            else:
                request.session.flush()
                return HttpResponse("Logged out")

    except:
        return HttpResponse("Logged In to continue")


def forgetpassword(request):
    # js=json.loads(request.body)
    to_user = "harimuths98@gmail.com"
    val = str(uuid.uuid1())
    email = EmailMessage('Password Change', 'http://127.0.0.1:8000/workout/confirmpassword/' + to_user + '/' + val + '',
                         to=[to_user])
    if email.send():
        '''response = HttpResponse('Mail sent')
        response.set_cookie('pasret'
                            , ''+val+'',max_age=180)
        return response'''
        request.session[to_user] = val
        return HttpResponse("Mail sent")
    else:
        return HttpResponse("Failed")


def confirmpassword(request, mail=None, id=None):
    try:

        if id == None:
            return HttpResponse("Not found")
        elif (id == request.session[mail]):
            # del request.session[mail]
            return HttpResponse("Changed Successfully")
        else:
            return HttpResponse("Invalid access")

    except:
        return HttpResponse("Invalid access")


'''
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
'''


def thirdparty(request):
    js = json.loads(request.body)
    val = int(js['num'])
    r = requests.get('http://127.0.0.1:8000/UltraTech_POC/fun_loc/%d' % val)
    result = json.loads(r.text)
    if (result['response']['statuscode'] == 200):
        return HttpResponse("Success")
    return HttpResponse("Failed")


def parchild(request):
    res = list(child.objects.filter(value=101).values('info__name', 'child_id'))
    return JsonResponse(res, safe=False)


def manyparchild(request):
    res = list(manychild.objects.filter(info=1).values('value', 'info__name'))
    res1 = list(manyparent.objects.filter(id=1).values('manychild__value', 'name'))
    res2 = list(manychild.objects.select_related('info').all().values())
    return JsonResponse(res, safe=False)


def email(request):
    email = EmailMessage('Hello', 'World', to=['user@gmail.com'])
    email.send()







def auth(request):
    tok = {'token':jwt.encode({'id': "abc","name":"hari"},"SECRET_KEY")}
    return JsonResponse(tok,safe=False)

def verifytoken(request):
    api=request.get_full_path().split('/')


    return HttpResponse(api[2])
    auth = request.META.get('HTTP_AUTHORIZATION')
    token=[]
    token = auth.split()
    payload=dict(jwt.decode(token[1],"SECRET_KEY"))
    id=payload["id"]
    name=payload["name"]
    return JsonResponse(payload)



def login(request):
    '''
    if "favorite_color" in request.GET:
        # Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" % \
                                request.GET["favorite_color"])gt

        # ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            request.GET["favorite_color"], max_age=60)

        return response
    '''

    js=json.loads(request.body)
    un=js["username"]
    ps=js["password"]
    ob=list(userDetails.objects.filter(username=un,password=ps).values())
    if len(ob):
        if(ob[0]['token']==''):
            id=ob[0]['username']
            tok_val=jwt.encode({'id':id}, "SECRET_KEY")
            tok = {'token': "Token "+tok_val}
            userDetails.objects.filter(username=un,password=ps).update(token=tok_val)
            return JsonResponse(tok, safe=False)
        else:
            ''' ob=tok_det.tok_det()
            name=ob.getId()
            return HttpResponse(name)'''
            dic=token_value(request)
            #return JsonResponse(dic,safe=False)
            return HttpResponse("Already logged in")

    else:
        return HttpResponse("invalid credentials")



def logout(request):
    return HttpResponse("Logged out successful",content_type='application/json')



@background(schedule=10)
def wait(value):
    print(value)


def mail(request):
    try:
            '''
            return JsonResponse({"Success":"True"},safe=False)

            with open(os.path.join(PROJECT_ROOT, 'task.txt')) as f:
                to=f.readline().strip()
                val=to.split(',')
                #return HttpResponse(len(val))
                subject=f.readline().strip()
                content=f.read()
                if(len(val)==1):
                    email = EmailMessage(subject, content, to=[to])
                else:
                    email = EmailMessage(subject, content, to=val)
                if(email.send()):
                    return HttpResponse("Mail Successfully sent")
                else:
                    return HttpResponse("Failed")
            '''
            js=json.loads(request.body)
            tme=str(js["time"])
            cur=datetime.now().time()
            tme=str(cur.hour) +":"+ str(cur.minute)
            cur=str(cur)
            return HttpResponse(tme)
            li=cur.split(":")
            hr=int(li[0])
            min=int(li[1])
            li1=tme.split(":")
            hr1=int(li1[0])
            min1=int(li1[1])
            hr2=(hr1-hr)*60
            min2=(min-min1)
            value=hr2+min2
            value=abs(value)*60
            if value==0:
                return HttpResponse("Not a valid time")
            ml.delay(value)
            return HttpResponse("Sent")


    except Exception as e:
        return HttpResponse(str(e))



def readcsv(request):
    field=[]
    rows=[]
    with open(os.path.join(PROJECT_ROOT, 'datas.csv')) as f:
        ob=csvData()
        field.append(f.next())
        for row in f:
            rows=row.split(',')
            ob.rollno = rows[0]
            ob.name = rows[1]
            ob.age = rows[2]
            ob.gender = rows[3][0]
            ob.save()

    return HttpResponse("Inserted")


def writecsv(request):
    add.delay(value=5)
    field=['rollno','name','age','gender']
    data=list(csvData.objects.values().all())
    filename="datas.csv"
    with open(os.path.join(PROJECT_ROOT,filename),'w+') as f:
        writer = csv.DictWriter(f, fieldnames=field)
        writer.writeheader()
        writer.writerows(data)
    data = open(os.path.join(PROJECT_ROOT, 'datas.csv'), 'r').read()
    resp = HttpResponse(data, content_type='application/force-download')
    resp['Content-Disposition'] = 'attachment;filename="data.csv"'
    os.remove(PROJECT_ROOT+"/"+filename)
    return resp




def writepdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['content-Disposition']='attachment;filename="info.pdf"'
    '''p=canvas.Canvas(response)
    p.drawString(100,100,"Hellooo Python !!!!")
    p.showPage()
    p.save()
    return response
    '''
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    for i in range(1,20):
        p.drawString(i*100,100, "Testing" )
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

