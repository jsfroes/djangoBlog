from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#add email address field to the registration forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # nested space for configurations
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
