from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from utils.cpf import is_cpf_valid

def validate_cpf(value):
    if not is_cpf_valid(value):
        raise ValidationError(
            _('%(value)s não é um CPF válido'),
            params={'value': value},
        )