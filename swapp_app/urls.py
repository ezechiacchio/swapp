from django.contrib import admin
from django.urls import path
from swapp_app.views import home_view, detail_view, list_view , login_view, user_create_view, logout_view

urlpatterns = [
    path('',home_view, name="home"),
    path('home',home_view, name="home"),
    path('detail',detail_view, name="detail"),
    path('list',list_view, name="list"),
    path("login",login_view, name = "login"),
    path("register",user_create_view, name="register"),
    path("logout",logout_view,name="logout")
    ]
