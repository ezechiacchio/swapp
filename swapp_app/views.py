from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
import requests

def home_view(request):
  	return render(request,"home.html",{})

@login_required(login_url="http://127.0.0.1:8080/swapp/login")
def detail_view(request):
    return render(request,"detail.html",{})

def swapi_list_view(request,id):
	response = requests.get('https://swapi.dev/api/people', {})
	next_url = response.json().get('next')
	personajes = response.json().get('results')
	personajes_lista = []
	if response:		
		for i in range(len(personajes)):
			personajes_lista.append(personajes[i])
		while next_url != None:
			response = requests.get(next_url, {})
			next_url = response.json().get('next')
			personajes = response.json().get('results')
			if response:		
				for i in range(len(personajes)):
					personajes_lista.append(personajes[i])
			print(personajes)
	p = Paginator(personajes_lista,10)
	personajes_page = p.get_page(id+1)
	id_ = id
	if id_ >= p.num_pages -1:
		id_ = id_ - 1
	context = {
	"lista" : personajes_page,
	"id_next": id_ + 1,
    "id_prev": id_ - 1,
    "actual": id_,
    "cant_paginas":p.num_pages

	}
#	print(personajes_lista)

	return render(request,'list.html',context)
    
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
