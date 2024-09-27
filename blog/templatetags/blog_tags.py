from django import template

from blog.models import Post

# create your templatetags here

register = template.Library()


@register.inclusion_tag('includes/recent_post.html')
def recent_post():
    posts = Post.objects.filter(published_status=True)[:4]
    return {'posts': posts}
