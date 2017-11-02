from django.contrib import admin
from .models import Entidade, Cargo, Responsavel, Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)
admin.site.register(Entidade)
admin.site.register(Cargo)
admin.site.register(Responsavel)
