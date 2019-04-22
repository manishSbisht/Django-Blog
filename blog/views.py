from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# dummy data
post_list = [
    {
        'author': 'Manish',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 11, 1998'
    },
    {
        'author': 'Sankalp',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 12, 1998'
    },
    {
        'author': 'Ritik',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': 'August 13, 1998'
    }
]


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
