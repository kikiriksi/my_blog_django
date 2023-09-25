from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField(verbose_name='Дата рождения', default='2000-01-01')
