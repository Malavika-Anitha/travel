from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team
# Create your views here.
# def demo(request):
#     return HttpResponse('hello')

def index(request):
    # name='mala'
    # return render(request,'index.html',{'obj':name})
    obj=Place.objects.all()
    tobj=Team.objects.all()


    return render(request,'index.html',{'result':obj,'tresult':tobj})


def add(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    sum=num1 + num2

    return render(request, 'about.html',{'objsum':sum})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')