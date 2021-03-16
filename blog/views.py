from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(req):
    context = {
        'posts': Post.objects.all()
    }

    return render(req, 'blog/home.html', context)

def about(req):
    title = {
        'title': 'About'
    }
    
    return render(req, 'blog/about.html', title)
