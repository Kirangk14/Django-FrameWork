from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])

    if val1!=0 and val2!=0:
        res=val1+val2
    else:
        print('Missing input')
    return render(request,'result.html',{'result':res})