from django.contrib import admin
from .models import Producto, Categoria, DatosPersonales
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    

admin.site.register(Producto)

admin.site.register(Categoria)

admin.site.register(DatosPersonales)
