from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fntadmin(request):
    return HttpResponse("Welcome to Admin")
def fnhworld(request):
    return render(request,'hello.html')
def fnadminmaster(request):
    return render(request,'adminmaster.html')
def fnadmindash(request):
    return render(request,'admindashboard.html')
def fnadminteach(request):
    return render(request,'adminteacher.html')
def fnadminstd(request):
    return render(request,'adminstudents.html')
def fnadminpay(request):
    return render(request,'adminpayments.html')
