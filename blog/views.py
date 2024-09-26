from django.shortcuts import render
from django.views import generic

from .models import Post
# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.filter(published_status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        slug = self.kwargs['slug']
        return Post.objects.get(slug=slug)
