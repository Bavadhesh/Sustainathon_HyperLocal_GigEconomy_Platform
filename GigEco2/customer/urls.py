from django.contrib import admin
from django.urls import path
from .views import getServiceProvider,signup,availability,login_view,Request

urlpatterns = [
   path('',getServiceProvider,name="list"),
   path('signup/',signup,name="signup"),
   path('signin/',login_view,name="loginUser"),
   path('available/<int:id>',availability),
   path('request/<int:id>/',Request),
  
]
