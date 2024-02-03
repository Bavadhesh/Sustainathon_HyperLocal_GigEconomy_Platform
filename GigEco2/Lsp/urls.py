
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view,home_view,changeAvailable,requestBox,send_email,send_decline_email,signout,signup,create_service_provider,book_log

urlpatterns = [
   path('',login_view,name="login"),
   path('home/',home_view,name="home"),
   path('changeAvailability/<int:status>/',changeAvailable,name="changeAvailable"),
   path('reqbox/',requestBox,name="reqbox"),
   path('send_mail/<int:id>/',send_email),
   path('send_decline_mail/<int:id>/',send_decline_email),
   path('logout/',signout,name='logout' ),
   path('signup/',signup,name='signupLsp' ),
   path('profile/',create_service_provider,name='profile' ),
   path('booklogs/',book_log,name='booklogs' ),

]

