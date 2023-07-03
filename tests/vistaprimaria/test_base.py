import pytest
from vistaprimaria.models import Tema
from django.contrib.auth.models import User
import datetime


@pytest.mark.django_db
def test_cambiar_estado(crear_tema):
    print("Cambio de estado de producto")
    assert crear_tema.nombre == "Producto 4"


@pytest.mark.django_db
def test_crear_producto():
    mi_tema = Tema(nombre = "burocrasia", fecha_publicacion_tema=datetime.datetime.now())
    mi_tema.save()
    print(mi_tema.nombre)
    assert mi_tema.nombre == "burocrasia"
    
