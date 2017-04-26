from django.http import HttpResponse
from django.shortcuts import render

from .models import List, Bubye


def index(request):
    final_list = List.objects.all()
    context = {'final_list': final_list}
    return render(request, 'message/index.html', context)

def detail(request, num):
    item = List.objects.get(id=num)
    context = {'item': item}
    return render(request, 'message/write.html', context)

def submit(request,num):
    message = request.POST['msg']
    alumini = List.objects.get(id=num)
    submission = Bubye(alumini = alumini, message = message)
    submission.save()
    return render(request, 'message/thankyou.html')
