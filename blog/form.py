from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()




class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
        

class Registiration(forms.ModelForm):
    class Meta:
        model = Register
        fields = (
            'first_name',
            'last_name',
            'email',
        )