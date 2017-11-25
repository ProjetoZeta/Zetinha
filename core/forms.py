from django.contrib.auth.forms import UserChangeForm
from .models import Cargo, Entidade, Funcao, Responsavel, Usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario