from django.urls import path
from . import views
urlpatterns=[   
    path('home/',views.fnhome,name='home'), 
    path('kersylb/',views.fnkersylb,name='kersylb'),
    path('master/',views.fnmaster,name='master'),
]