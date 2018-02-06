from django import forms
from django.contrib.auth.models import User

class addNewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
