from django.contrib import admin
from .models import Entidade
from .models import Cargo
from .models import Responsavel

class EntidadeAdmin(admin.ModelAdmin):
    pass

class CargoAdmin(admin.ModelAdmin):
    pass

class ResponsavelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entidade, EntidadeAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)