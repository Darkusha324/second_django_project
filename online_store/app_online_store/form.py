from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validate_english_username

class FormProduct (forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price", "photograph" ,"description","category" ]

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=150,validators=[validate_english_username])
    password1 = forms.CharField(widget=forms.PasswordInput,help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput,help_text='')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''