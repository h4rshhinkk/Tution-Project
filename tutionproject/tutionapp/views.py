from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'home.html')
def fnkersylb(request):
    return render(request,'kersylb.html')
def fnmaster(request):
    return render(request,'master.html')