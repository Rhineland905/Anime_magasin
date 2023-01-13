from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=64)
    pasword = forms.CharField(required=True,max_length=32, widget=forms.PasswordInput)