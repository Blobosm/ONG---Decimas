from django.contrib import admin
from .models import Perro, Gato, Genero, Comuna
# Register your models here.

admin.site.register(Perro)
admin.site.register(Gato)
admin.site.register(Genero)
admin.site.register(Comuna)
