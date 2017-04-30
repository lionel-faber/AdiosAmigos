from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

from .models import List, Bubye
from django.contrib.auth.models import User


def index(request):
    final_list = List.objects.all()
    context = {'final_list': final_list}
    return render(request, 'message/index.html', context)

def detail(request, num):
    item = List.objects.get(id=num)
    context = {'item': item}
    return render(request, 'message/write.html', context)

def submit(request, num):
    message = request.POST['msg']
    alumini = List.objects.get(id=num)
    submission = Bubye(alumini = alumini, message = message)
    submission.save()
    return render(request, 'message/thankyou.html')

def dear(request):
    return render(request, 'message/dearsenior.html')

def reg(request):
    items = List.objects.all()
    context = {"items": items}
    return render(request, 'message/signup.html', context)

def login(request):
    items = List.objects.all()
    context = {"items": items}
    return render(request, 'message/login.html', context)

def regviewmsg(request):
    usrid = request.POST['usr']
    pwd = request.POST['pwd']
    nam = List.objects.get(id=usrid)
    messages = Bubye.objects.filter(alumini=usrid)
    obj = User.objects.create_user(first_name=nam.name, username=usrid, password=pwd)
    obj.save()
    return render(request, 'message/viewmsg.html', {'messages': messages, 'nam': nam})

def loginviewmsg(request):
    usrid = request.POST['usr']
    pwd = request.POST['pwd']
    user = authenticate(username = usrid, password=pwd)
    nam = List.objects.get(id=usrid)
    messages = Bubye.objects.filter(alumini=usrid)
    if user is not None:
        return render(request, 'message/viewmsg.html', {'messages': messages, 'nam': nam})
    else:
        items = List.objects.all()
        context = {"items": items}
        return render(request, 'message/login1.html', context)
