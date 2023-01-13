from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('signup',signup,name="signup"),
    path('userlogin',userlogin,name="userlogin"),
    path('userlogout',userlogout,name="userlogout"),
    path('profile',profile,name="profile"),
]
