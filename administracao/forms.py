from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    bolsista = forms.BooleanField()
    ativo = forms.BooleanField()
