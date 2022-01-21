from django.urls import path
from . import views
urlpatterns=[   
    path('',views.fnhome,name='home'), 
    path('kersylb/',views.fnkersylb,name='kersylb'),
    path('master/',views.fnmaster,name='master'),
    path('teachersinfo/',views.fnteacher,name='teachersinfo'),
    path('cbsesylb/',views.fncbsesylb,name='cbsesylb'),
    path('fnk5std/',views.fnk5std,name='k5std'),
    path('contactus/',views.fncontactus,name='contactus'),
    path('usersignup/',views.fnusersignup,name="usignup"),
    path('aboutus/',views.fnaboutus,name="aboutus")
    
]