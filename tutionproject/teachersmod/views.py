from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fndemo(request):
    return render(request,'demo.html')
    
    