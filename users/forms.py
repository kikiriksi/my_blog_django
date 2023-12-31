from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'gender', 'birth_date')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'gender', 'birth_date')


class LogForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
