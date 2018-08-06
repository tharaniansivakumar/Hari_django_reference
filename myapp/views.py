import urllib, json

from django.shortcuts import render
from myapp.forms import AddDetails
from myapp.forms import DispDetails
from django.http import HttpResponse,JsonResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from myapp.models import Details


def index(request):
    return render(request,"home.html",{})

def hello(request):
    text="<h1>Hello Django World</h1>"
    return HttpResponse(text)
def hello1(request):
    dic={}
    dic['name']="hari"
    dic['age']=20
    dic['dish']="Panner"
    dic['date']="19-07-2018"
    dic['details']=["City:Cbe","Native:Tirunelveli","Working:Divum"]
    return render(request,"hello.html",dic)

def crudops(request):
    det=Details(name="harimuths",age=20,dish="panner",phno=948857)
    det.save()
    return HttpResponse("Inserted")


def insert(request):
    dic={}
    ins=""
    nm=""
    if request.method== "POST":
        #ins=request.POST.get('name', None)
            ins=AddDetails(request.POST)
            if ins.is_valid():
                nm=ins.cleaned_data['name']
                ag=ins.cleaned_data['age']
                ph=ins.cleaned_data['phno']
                di=ins.cleaned_data['dish']
            dic={}
            dic['name']=nm
            det=Details(name=nm,age=ag,dish=di,phno=ph)
            det.save()
            #dic['age']=ins.age

    return render(request,'details.html',dic)





def display(request):
   ''' dic={}
    ins=""
    nm=""
    if request.method== "POST" or "PUT":
        #ins=request.POST.get('name', None)
            ins=DispDetails(request.POST)
            if ins.is_valid():
                nm=ins.cleaned_data['name']
            try:
                res=Details.objects.get(name=nm)
                dic['age'] = res.age
                dic['dish'] = res.dish
                dic['phno'] = res.phno
            except:
                dic={}
    else:
            nm=request.GET.get('name')
            try:
                res=Details.objects.get(name=nm)
                dic['age'] = res.age
                dic['dish'] = res.dish
                dic['phno'] = res.phno
            except:
                dic={}

    return render(request,'display.html',dic)'''
   all_det=Details.objects.all()
   html=""
   for det in all_det:
        url= 'http://127.0.0.1:8000/myapp/display/'+ str(det.id) + '/'
        html+=  '<h3>User :</h3><br>'  '<a href="' +url+ '">' + det.name + '</a><br><br><br>'
   return HttpResponse(html)




def update(request):
    dic={}
    ins=""
    nm=""
    if request.method== "POST":
            #print(request.get('name'))
        #ins=request.POST.get('name', None)
            ins=DispDetails(request.POST)
            if ins.is_valid():
                nm=ins.cleaned_data['name']
            try:
                res=Details.objects.get(name=nm)
                dic['age'] = res.age
                dic['dish'] = res.dish
                dic['phno'] = res.phno
            except:
                dic={}
            Details.objects.raw('insert into details values("mani",20,"panner",80)')
            Details.objects.raw('update details set dish = %s where name = %s ',[res.dish,nm] )

    return render(request,'details.html',dic)



def js(request):
    data=json.loads(request.body)
    return JsonResponse(data)

def insert(request):
    f=0
    if 'hari' or 'thar' or 'kulo' or 'radha' or 'venky' in request.POST:
        # name=request.POST.get('name')
        if 'hari' in request.POST:
            name = "hari"
            msg = request.POST.get('hari')
            f=1
        elif 'thar' in request.POST:
            name = "tharani"
            msg = request.POST.get('thar')
            f=1
        elif 'kulo' in request.POST:
            name = "kulo"
            msg = request.POST.get('kulo')
            f=1
        elif 'radha' in request.POST:
            name = "radha"
            msg = request.POST.get('radha')
            f=1
        elif 'venky' in request.POST:
            name = "venky"
            msg = request.POST.get('venky')
            f=1
        if(f==1):
            m = Message()
            m.name = name;
            m.msg = msg;
            m.save()

    ob = list(Message.objects.all().values())
    ob.reverse()
    sample = {"name": ob}
    return render(request, 'index.html', sample)