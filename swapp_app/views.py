from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home_view(request):
  	return render(request,"home.html",{})

@login_required(login_url="http://127.0.0.1:8080/swapp/login")
def detail_view(request):
    return render(request,"detail.html",{})

def list_view(request):
    return render(request,"list.html",{})
    
def login_view(request):
    user = authenticate(request, username = request.POST.get('user'),password = request.POST.get('psw') )
    if user is not None:
        login(request, user)
    print(request.user.is_authenticated)
    return render(request,"login.html",{})

def logout_view(request):
    logout(request)
    return render(request,"home.html",{})

def user_create_view(request):
    print(request.POST)
    context = {}
    try:
        user = User.objects.create_user(request.POST.get('user'), request.POST.get('mail'), request.POST.get('psw'))
        user.save()
    except:
        return render(request,"error_registro.html",{})
    return render(request,"register.html",{})
