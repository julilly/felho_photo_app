from django import forms
from .models import Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'image']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']