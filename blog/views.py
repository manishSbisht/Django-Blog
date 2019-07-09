from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class PostDetailView(DetailView):
    model = Post
    # Rest of the variable will have their default values
    # template used should be present at: '<app>/<model_viewtype>.html'
    # context object is named: "object"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # defualt template name is: <model>_form.html

    # overriding form_valid() method to set the author of new post
    def form_valid(self, form):
        # set current user as the author of newly created post
        form.instance.author = self.request.user

        # now run the modified form_valid() method after above change
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # all the inherited mixins should be passed to the left of 'UpdateView'

    model = Post
    fields = ['title', 'content']
    # defualt template name is: <model>_form.html

    # overriding form_valid() method to set the author of new post
    def form_valid(self, form):
        # set current user as the author of newly created post
        form.instance.author = self.request.user

        # now run the modified form_valid() method after above change
        return super().form_valid(form)

    # test the current object against a condition
    def test_func(self):
        post = self.get_object()  # return the object view is displaying

        # if current user is author of current post
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
