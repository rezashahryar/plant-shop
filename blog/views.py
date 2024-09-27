from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostCommentForm

from .models import Post
# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.select_related('author').filter(published_status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        slug = self.kwargs['slug']
        return Post.objects.select_related('author').get(slug=slug)
    

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
