from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

#registration form with email address field

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login') #name of the url pattern for the blog homepage
    else:
        form = UserRegisterForm()

    user_form = {
        'form': form
    }

    return render(request, 'users/register.html', user_form)

@login_required()
def profile(request):
    return render(request, 'users/profile.html')

