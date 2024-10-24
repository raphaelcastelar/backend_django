from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(r'^\d{11}$', 'O CPF deve conter 11 dígitos numéricos.')]
    )
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.username

