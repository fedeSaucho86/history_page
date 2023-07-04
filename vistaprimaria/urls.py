from django.urls import path
from vistaprimaria import views

app_name = 'vistaprimaria'

urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', views.articulos, name='articulos'),
]
