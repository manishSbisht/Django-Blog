from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]

# as_view() method converts class to a view

# <int:pk> is the variable part of URL,
# pk=primary key, int=expects the value to be integer
# name 'pk' is predefined in DetailView class
