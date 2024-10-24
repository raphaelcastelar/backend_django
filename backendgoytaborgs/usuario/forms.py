from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nome', 'email', 'cpf', 'password1', 'password2')

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve conter 11 dígitos.')
        return cpf
