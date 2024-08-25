from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    cdata=category.objects.all().order_by('-id')[0:6]
    ndata=desnews.objects.all().order_by('-id')[0:4]
    datan=notification.objects.all().order_by('-id')[0:4]
    sdata=slider.objects.all().order_by('-id')

    return render(request,'user/index.html',{"data":cdata,"desnews":ndata,"notification":datan,"slider":sdata})

def contactus(request):
    status=False
    if request.method=='POST':
        Name = request.POST.get("name","")
        Email = request.POST.get("email","")
        Mobile = request.POST.get("mobile","")
        Massage = request.POST.get("msg","")
        x=contact(name=Name,email=Email,mobile=Mobile,message=Massage)
        x.save
        status=True

    return render(request,'user/contactus.html',{'S':status})

def aboutus(request):
    return render(request,'user/aboutus.html')

def videos(request):
    vdata= video.objects.all().order_by('-id')


    return render(request,'user/videos.html',{"video":vdata})

def viewnews(request):
    cdata = category.objects.all().order_by('-id')
    ndata = desnews.objects.all().order_by('-id')
    a = request.GET.get('abc')
    ndata=""
    if a is None:
        ndata = desnews.objects.all()
    else:
        ndata=desnews.objects.all().filter(ncategory=a)

    return render(request,'user/viewnews.html',{"c":cdata,"n":ndata})

def viewmore(req):
    a=req.GET.get('msg')
    ndata=desnews.objects.filter(id=a)
    return render(req,'user/viewmore.html',{"desnews":ndata})

def newsv(req):
    cdata=category.objects.all().order_by('-id')
    ndata = desnews.objects.all().order_by('-id')[0:4]
    return render(req,'user/newsv.html',{"c":cdata,"n":ndata})