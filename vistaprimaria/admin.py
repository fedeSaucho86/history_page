from django.contrib import admin
from vistaprimaria.models import Continente, Tema, Epoca

class TemaInline(admin.TabularInline):

    model = Tema
    extra = 0

class EpocaInline(admin.TabularInline):

    model = Epoca
    extra = 0

class ContinenteAdmin(admin.ModelAdmin):
    inlines = [EpocaInline]

class EpocaAdmin(admin.ModelAdmin):
    inlines = [TemaInline]

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    #fields =['nombre', "Continente"]
    #video 1, clase 3
    fieldsets = [
        ("Tema", {"fields": ["nombre"]}),
        ("Epoca", {"fields": ["epoca"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'estado', 'fecha_publicacion_tema', 'imagen'
                ]
            },
        ),


    ]
    list_display = ["nombre", "tipo_de_tema","fecha_publicacion_tema", "upper_case_name"]
    ordering = ["fecha_publicacion_tema"]
    list_filter = ("nombre", "estado", "fecha_publicacion_tema")
    search_fields=("nombre", "estado")
    list_display_links = ("nombre", "tipo_de_tema")

    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.nombre, obj.estado)).upper()




admin.site.register(Continente, ContinenteAdmin)
admin.site.register(Epoca, EpocaAdmin)
#admin.site.register(Tema, TemaAdmin)