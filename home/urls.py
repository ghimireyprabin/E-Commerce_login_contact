from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns=[

    path('',index,name="index"),
    path('services',service,name="service"),
    path('contact',contact,name="contact"),
    

    path('accounts/', include('django.contrib.auth.urls')),
    path('profile',profile,name="profile"),
    path('login',UserLogin,name="login"),
    # path('future',futures,name="future")
]