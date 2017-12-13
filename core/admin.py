from django.contrib import admin
from .models import Entidade, Cargo, Responsavel, Usuario, Bolsista, Documento
from .forms import UsuarioChangeForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('no_completo', 'email')}),
        ('Latitude', {'fields': ('ic_ativo', 'ic_bolsista')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Entidade)
admin.site.register(Cargo)
admin.site.register(Responsavel)
admin.site.register(Bolsista)
admin.site.register(Documento)

