from django.contrib import admin
from vistaprimaria.models import Nivel, Tema

class TemaInline(admin.TabularInline):

    model = Tema
    extra = 0

class NivelAdmin(admin.ModelAdmin):
    inlines = [TemaInline]


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    #fields =['nombre', "nivel"]
    #video 1, clase 3
    fieldsets = [
        ("Tema", {"fields": ["nombre"]}),
        ("Nivel", {"fields": ["nivel"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'estado', 'fecha_publicacion_tema'
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




admin.site.register(Nivel, NivelAdmin)
#admin.site.register(Tema, TemaAdmin)