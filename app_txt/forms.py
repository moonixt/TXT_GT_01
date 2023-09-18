from django import forms

class UserLogin(forms.Form):
    usuario = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30)