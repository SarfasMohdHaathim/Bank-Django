from django.forms import ModelForm,forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

