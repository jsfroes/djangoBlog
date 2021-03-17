from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#add email address field to the registration forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # nested space for configurations
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# update the user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # nested space for configurations
    class Meta:
        model = User
        fields = ['username', 'email']

#update profile image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']