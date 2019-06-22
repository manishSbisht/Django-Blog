from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context, {'title': 'Home'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # default format: '<app>/<model_viewtype>.html'
    context_object_name = 'posts'  # variable to loop over posts
    ordering = ['-date_posted']  # minus sign to sort in descending order(new to old)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
