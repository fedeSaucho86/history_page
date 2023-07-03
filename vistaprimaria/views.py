from django.shortcuts import render
from django.http import HttpResponse
from vistaprimaria.models import Tema, Continente
from django.http import HttpResponse
from django.db.models import Q

#def index(request):
#  return HttpResponse("Hola Mundo")

def index(request):
     params = {}
     tema=Tema.objects.filter( Q(estado="Publicado"), )
     params['tema']=tema
     continente = Continente.objects.all()
     params['continente']=continente
     print(continente)
     return render(request, 'vistaprimaria/index.html', params)