from django.shortcuts import render
from django.views import generic

from .models import Post
# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.filter(published_status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
