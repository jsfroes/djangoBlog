from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'jsfroes',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'March 16, 2021'
    },
      {
        'author': 'charlotte',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'March 18, 2021'
    },
]



def home(req):
    context = {
        'posts': posts
    }

    return render(req, 'blog/home.html', context)

def about(req):
    title = {
        'title': 'About'
    }
    
    return render(req, 'blog/about.html', title)
