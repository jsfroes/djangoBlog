from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('<h1>Blog Home</h1>')

def about(req):
    return HttpResponse('<h1>About Page</h1>')