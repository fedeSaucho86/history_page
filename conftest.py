import pytest
from vistaprimaria.models import Tema
from django.contrib.auth.models import User
import datetime

@pytest.fixture()
def crear_tema(db):
    tema = Tema(nombre="Hitler", fecha_publicacion_tema=datetime.datetime.now())
    tema.save()

    return tema