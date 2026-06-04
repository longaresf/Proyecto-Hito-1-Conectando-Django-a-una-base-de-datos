from django.contrib import admin
from inmobiliaria_app.models import Usuario, Inmueble, Usuario_Inmueble

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(Usuario_Inmueble)
