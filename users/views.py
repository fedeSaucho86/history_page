from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#  return HttpResponse("Hola Mundo")

def index(request):
     params = {}
     params["nombre_sitio"] = "Rochy history blog"
     return render(request, "vistaprimaria/index.html", params)