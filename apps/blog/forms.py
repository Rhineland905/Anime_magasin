from django import forms
from apps.blog.models import BlogComets

class CreatCommets(forms.ModelForm):
    article = forms.CharField
    class Meta:
        model = BlogComets
        fields = ['name','e_mail','text','article']