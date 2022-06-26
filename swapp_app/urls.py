from django.contrib import admin
from django.urls import path
from swapp_app.views import *

urlpatterns = [
    path('',home_view, name="home"),
    path('home',home_view, name="home"),
    path('detail/<int:id>',detail_view, name="detail"),
    path('list/<int:id>',swapi_list_view, name="list"),
    path("login",login_view, name = "login"),
    path("register",user_create_view, name="register"),
    path("logout",logout_view,name="logout"),
    path("profile/",profile_view,name="profile")
    ]
