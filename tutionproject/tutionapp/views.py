from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'home.html')
def fnkersylb(request):
    return render(request,'kersylb.html')
def fnmaster(request):
    return render(request,'master.html')
def fnteacher(request):
    return render(request,'teachers.html')
def fncbsesylb(request):
    return render(request,'cbsesylb.html')
def fnk5std(request):
    return render(request,'k5std.html')
def fncontactus(request):
    return render(request,'contactus.html')
def fnusersignup(request):
    return render(request,'usersignup.html')
def fnaboutus(request):
    return render(request,'aboutus.html')
def fnc8std(request):
    return render(request,'c8std.html')


