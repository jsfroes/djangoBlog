from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# function based views 
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

# class based views
# there are different kinds of class based views - List views, update views, delete views, detail views

from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html - standard path
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    # set the author for the blog post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)