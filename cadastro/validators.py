from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .utils.cpf import is_cpf_valid, is_cnpj_valid
import re

def cpf(value):
    if not is_cpf_valid(value):
        raise ValidationError(
            _('%(value)s não é um CPF válido'),
            params={'value': value},
        )

def cnpj(value):
    if not is_cnpj_valid(value):
        raise ValidationError(
            _('%(value)s não é um CNPJ válido'),
            params={'value': value},
        )

def lattes_url(value):
    pattern = re.compile("http\:\/\/lattes\.cnpq\.br\/[0-9]+$")
    if not pattern.match(value):
        raise ValidationError(
            _('A URL informada não parece um link para um currículo Lattes'),
            params={},
        )