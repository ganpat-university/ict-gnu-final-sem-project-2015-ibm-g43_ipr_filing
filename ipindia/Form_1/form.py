from django import forms
from .models import Form1

class Form(forms.ModelForm):
    class Meta:
        model=Form1
        fields="__all__"