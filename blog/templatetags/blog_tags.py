from django import template

from blog.models import Comment, Post

# create your templatetags here

register = template.Library()


@register.inclusion_tag('includes/recent_post.html')
def recent_post():
    posts = Post.objects.filter(published_status=True)[:4]
    return {'posts': posts}


@register.inclusion_tag('includes/recent_comments.html')
def recent_comments_of_blog_section():
    comments = Comment.objects.select_related('user').select_related('post').all()[:4]
    return {'comments': comments}
