from dataclasses import fields
from django import forms
from .models import Register

class Registiration(forms.ModelForm):
    class Meta:
        model = Register
        fields = (
            'first_name',
            'last_name',
            'email',
        )