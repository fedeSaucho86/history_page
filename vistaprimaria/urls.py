from django.urls import path
from vistaprimaria import views

urlpatterns = [
    path('', views.index, name='index'),
]
