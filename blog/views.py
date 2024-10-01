from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch

from blog.forms import PostCommentForm

from .models import CategoryPost, Comment, Post
# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.select_related('author').filter(published_status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryPost.objects.all()

        return context


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        slug = self.kwargs['slug']
        return Post.objects.select_related('author') \
            .prefetch_related(
                Prefetch(
                    'comments',
                    queryset=Comment.objects.select_related('user')
                )
            ).get(slug=slug)
    

class CommentCreateView(LoginRequiredMixin, generic.FormView):
    form_class = PostCommentForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']

        form_obj = form.save(commit=False)
        form_obj.post_id = post_pk
        form_obj.user_id = self.request.user.pk
        form_obj.save()
        
        self.request.user.email = form.cleaned_data['email']
        self.request.user.save()

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        post_pk = self.kwargs['post_pk']
        return Post.objects.get(pk=post_pk).get_absolute_url()
    

class FilterPostsByCategory(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(category__slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryPost.objects.all()

        return context
