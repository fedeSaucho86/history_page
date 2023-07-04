from django.shortcuts import render
from django.http import HttpResponse
from vistaprimaria.models import Tema, Continente
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#def index(request):
#  return HttpResponse("Hola Mundo")



@login_required(login_url='/accounts/login/')
def index(request):
     params = {}
     tema=Tema.objects.filter( Q(estado="Publicado"), )
     params['tema']=tema
     continente = Continente.objects.all()
     params['continente']=continente
     print(continente)
     return render(request, 'vistaprimaria/index.html', params)

@login_required(login_url='/accounts/login/')
def articulos(request):
    return render(request, 'vistaprimaria/articulos.html')