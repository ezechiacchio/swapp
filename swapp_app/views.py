import math
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,get_user
from django.core.paginator import Paginator
import requests
from imagenes.personajes import PERSONAJES
from mailer import Mailer

def home_view(request):
  	return render(request,"home.html",{})

@login_required(login_url="/swapp/login")
def detail_view(request,id):
    response = requests.get('https://swapi.dev/api/people/'+ str(id) + "/", {})
    personaje = response.json()
    vehicle = personaje.get("vehicles",None)
    personaje['image'] = PERSONAJES.get(personaje['name'])
    user = get_user(request)
    context_relacion = {"pj_name":personaje.get("name",None),
                        "user_name":str(user.username)}
    var = requests.post('http://127.0.0.1:8080/chequearrelacion', json = context_relacion)
    seguido = var.json().get("encontrado")
    try:
        vehicle  = requests.get(vehicle[0])
        vehicle = vehicle.json().get('name')    
        personaje['vehicle'] = vehicle
    except:
        personaje['vehicle'] = "Ninguno"
    context = {"personaje":personaje,
                "user":user,
                "seguido":seguido}
    print(context["seguido"])
    datos ={"pj_name":personaje.get("name",None).replace(' ','_'),
            "user_name":request.POST.get("user_name",None)}
    requests.post('http://127.0.0.1:8080/guardardatos', json = datos)
    return render(request,"detail.html",context)

@login_required(login_url="/swapp/login")
def profile_view(request):
    user = get_user(request)
    var = requests.get('http://127.0.0.1:8080/seguidos?user=' + user.username)
    lista_seguidos = (var.json()['lista_seguidos'])
    context= {"user":user,
                "lista_seguidos": lista_seguidos}
    return render(request,"profile.html",context)

def swapi_list_view(request,id):
    if id == 0:
        id = 1
    response = requests.get('https://swapi.dev/api/people?page=' + str(id), {})
    cant = response.json().get('count')
    personajes = response.json().get('results')
    personajes_lista = []
    pjs_x_pag = 10
    if response:		
        for i in range(len(personajes)):
            personajes[i]['id'] = personajes[i]['url'][-3:-1].replace("/","")
            personajes_lista.append(personajes[i])
            #print(personajes)
    p = Paginator(personajes_lista,pjs_x_pag)
    personajes_page = p.get_page(1)
    id_ = id
    cant_paginas =math.ceil(cant/pjs_x_pag) 
    if id_ >= cant_paginas:
        id_ = id_ - 1
    context = {
	"lista" : personajes_page,
	"id_next": str(id_ + 1),
    "id_prev": str(id_ - 1),
    "actual": id_,
    "cant_paginas":cant_paginas -1,

	}
#	print(personajes_lista)

    return render(request,'list.html',context)
    
def login_view(request):
    user = authenticate(request, username = request.POST.get('user'),password = request.POST.get('psw') )
    if user is not None:
        login(request, user)
        return render(request,"home.html",{})
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
