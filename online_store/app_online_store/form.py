from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormProduct (forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price", "photograph" ,"description" ]

class RegisterUserForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput,help_text='')
    class Meta:
        model = User
        fields = ['username','password1','password2']
        help_texts = {
            'username':'',
            'password1':'',
            'password2': ''
        }

