from django.db import models
from django.utils.html import format_html

class Nivel(models.Model):
    nivel = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="nivel/%Y/%m/%d", blank=True, null=True)     

    def __str__(self,):
        return self.nivel + " lectivo" 

#AGREGAR VARIEDAD DE CURSO   
class Tema(models.Model):
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'))
    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default='Borrador')
    nombre = models.CharField(max_length=100, db_index=True)
    fecha_publicacion_tema = models.DateTimeField('Fecha de Publicación')
    slug = models.SlugField(max_length=100, db_index=True)
    #nivel = models.ManyToManyField(Nivel)
    nivel = models.ForeignKey(
        Nivel, blank=False, null=True, on_delete=models.CASCADE
    )

    def tipo_de_tema(self): #adobe kuler
        if self.estado == 'Retirado':
            return format_html('<span style="color: #f00;">{}</span>', self.estado, )
        elif self.estado == 'Borrador':
            return format_html('<span style="background-color: #f0f; padding:7px;">{}</span>', self.estado, )
        elif self.estado == 'Publicado':
            return format_html('<span style="color: #099;">{}</span>', self.estado, )

    def __str__(self):
        return '%s' % self.nombre